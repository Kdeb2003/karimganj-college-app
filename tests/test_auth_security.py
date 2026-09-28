import unittest

from auth_security import (
    OTPChallenge,
    OTPStatus,
    hash_password,
    verify_and_upgrade_password,
    verify_password,
)


class PasswordSecurityTests(unittest.TestCase):
    def test_password_is_stored_as_a_structured_hash(self):
        stored = hash_password("correct horse battery staple", iterations=1_000)

        self.assertTrue(stored.startswith("pbkdf2_sha256$v1$1000$"))
        self.assertNotIn("correct horse battery staple", stored)

    def test_successful_password_verification(self):
        stored = hash_password("valid-password", iterations=1_000)

        self.assertTrue(verify_password("valid-password", stored))

    def test_failed_password_verification(self):
        stored = hash_password("valid-password", iterations=1_000)

        self.assertFalse(verify_password("wrong-password", stored))

    def test_different_salts_produce_different_hashes(self):
        first = hash_password("same-password", iterations=1_000)
        second = hash_password("same-password", iterations=1_000)

        self.assertNotEqual(first, second)
        self.assertTrue(verify_password("same-password", first))
        self.assertTrue(verify_password("same-password", second))

    def test_matching_legacy_plaintext_is_upgraded(self):
        verified, replacement = verify_and_upgrade_password(
            "legacy-password", "legacy-password"
        )

        self.assertTrue(verified)
        self.assertIsNotNone(replacement)
        self.assertTrue(verify_password("legacy-password", replacement))

    def test_failed_legacy_plaintext_is_not_upgraded(self):
        verified, replacement = verify_and_upgrade_password(
            "wrong-password", "legacy-password"
        )

        self.assertFalse(verified)
        self.assertIsNone(replacement)


class OTPChallengeTests(unittest.TestCase):
    def test_otp_expires_and_clears_state(self):
        challenge, code = OTPChallenge.create(expires_in_seconds=30, now=100.0)

        result = challenge.verify(code, now=131.0)

        self.assertEqual(OTPStatus.EXPIRED, result)
        self.assertFalse(challenge.active)

    def test_otp_attempts_are_limited(self):
        challenge, code = OTPChallenge.create(max_attempts=2, now=100.0)

        self.assertEqual(OTPStatus.INVALID, challenge.verify("wrong", now=101.0))
        self.assertEqual(
            OTPStatus.ATTEMPTS_EXCEEDED,
            challenge.verify("still-wrong", now=102.0),
        )
        self.assertFalse(challenge.active)
        self.assertEqual(OTPStatus.EXPIRED, challenge.verify(code, now=103.0))

    def test_successful_otp_clears_state(self):
        challenge, code = OTPChallenge.create(now=100.0)

        self.assertEqual(OTPStatus.SUCCESS, challenge.verify(code, now=101.0))
        self.assertFalse(challenge.active)


if __name__ == "__main__":
    unittest.main()
