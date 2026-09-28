"""Password hashing and one-time-password primitives for the application."""

from __future__ import annotations

import base64
import hashlib
import hmac
import math
import secrets
import time
from dataclasses import dataclass
from enum import Enum


PASSWORD_SCHEME = "pbkdf2_sha256"
PASSWORD_VERSION = "v1"
DEFAULT_PBKDF2_ITERATIONS = 600_000
PASSWORD_SALT_BYTES = 16


def _encode_bytes(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).decode("ascii")


def _decode_bytes(value: str) -> bytes:
    return base64.b64decode(value.encode("ascii"), altchars=b"-_", validate=True)


def hash_password(
    password: str,
    *,
    iterations: int = DEFAULT_PBKDF2_ITERATIONS,
    salt: bytes | None = None,
) -> str:
    """Return a versioned PBKDF2-SHA256 password representation."""
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    if iterations <= 0:
        raise ValueError("iterations must be positive")

    salt = secrets.token_bytes(PASSWORD_SALT_BYTES) if salt is None else salt
    derived_key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        iterations,
    )
    return "$".join(
        (
            PASSWORD_SCHEME,
            PASSWORD_VERSION,
            str(iterations),
            _encode_bytes(salt),
            _encode_bytes(derived_key),
        )
    )


def is_password_hash(stored_value: str) -> bool:
    """Return whether a value declares the application's password-hash scheme."""
    return isinstance(stored_value, str) and stored_value.startswith(
        f"{PASSWORD_SCHEME}${PASSWORD_VERSION}$"
    )


def verify_password(password: str, stored_value: str) -> bool:
    """Verify a password against a structured PBKDF2 representation."""
    if not isinstance(password, str) or not is_password_hash(stored_value):
        return False

    try:
        scheme, version, iteration_text, salt_text, expected_text = stored_value.split("$")
        if scheme != PASSWORD_SCHEME or version != PASSWORD_VERSION:
            return False
        iterations = int(iteration_text)
        if iterations <= 0:
            return False
        salt = _decode_bytes(salt_text)
        expected = _decode_bytes(expected_text)
    except (TypeError, ValueError):
        return False

    candidate = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        iterations,
    )
    return hmac.compare_digest(candidate, expected)


def verify_and_upgrade_password(password: str, stored_value: str) -> tuple[bool, str | None]:
    """Verify a stored password and return a replacement hash when migration is needed.

    Values using the current structured format are verified normally and never
    downgraded. Any other value is treated as legacy plaintext only for a
    constant-time comparison. A matching legacy value is immediately returned
    with a secure replacement hash for the caller to persist.
    """
    if not isinstance(password, str) or not isinstance(stored_value, str):
        return False, None

    if is_password_hash(stored_value):
        return verify_password(password, stored_value), None

    legacy_matches = hmac.compare_digest(
        password.encode("utf-8"),
        stored_value.encode("utf-8"),
    )
    if not legacy_matches:
        return False, None
    return True, hash_password(password)


class OTPStatus(str, Enum):
    SUCCESS = "success"
    INVALID = "invalid"
    EXPIRED = "expired"
    ATTEMPTS_EXCEEDED = "attempts_exceeded"


@dataclass
class OTPChallenge:
    """An expiring, attempt-limited OTP challenge stored only in memory."""

    _code_digest: bytes
    created_at: float
    expires_in_seconds: int = 300
    max_attempts: int = 3
    attempts: int = 0
    active: bool = True

    @classmethod
    def create(
        cls,
        *,
        expires_in_seconds: int = 300,
        max_attempts: int = 3,
        now: float | None = None,
    ) -> tuple["OTPChallenge", str]:
        if expires_in_seconds <= 0:
            raise ValueError("expires_in_seconds must be positive")
        if max_attempts <= 0:
            raise ValueError("max_attempts must be positive")

        code = f"{secrets.randbelow(1_000_000):06d}"
        challenge = cls(
            _code_digest=hashlib.sha256(code.encode("ascii")).digest(),
            created_at=time.monotonic() if now is None else now,
            expires_in_seconds=expires_in_seconds,
            max_attempts=max_attempts,
        )
        return challenge, code

    def seconds_remaining(self, *, now: float | None = None) -> int:
        if not self.active:
            return 0
        current_time = time.monotonic() if now is None else now
        elapsed = current_time - self.created_at
        return max(0, math.ceil(self.expires_in_seconds - elapsed))

    def verify(self, candidate: str, *, now: float | None = None) -> OTPStatus:
        if not self.active or self.seconds_remaining(now=now) <= 0:
            self.clear()
            return OTPStatus.EXPIRED

        self.attempts += 1
        candidate_digest = hashlib.sha256(candidate.encode("utf-8")).digest()
        if hmac.compare_digest(candidate_digest, self._code_digest):
            self.clear()
            return OTPStatus.SUCCESS

        if self.attempts >= self.max_attempts:
            self.clear()
            return OTPStatus.ATTEMPTS_EXCEEDED
        return OTPStatus.INVALID

    def clear(self) -> None:
        self._code_digest = b""
        self.active = False

