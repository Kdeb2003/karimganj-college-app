# Karimganj College Placement Application

A legacy campus placement and recruitment application developed during my bachelor's studies using Python, Kivy, KivyMD, and MySQL. The project supports students, recruiters, placement officers, and administrators through role-specific workflows.

## Overview

The application was created to bring common campus recruitment activities into one desktop/mobile-style interface. It provides separate experiences for four primary roles:

- Students can maintain their profiles, explore opportunities, and apply for jobs.
- Companies can publish recruitment opportunities and manage applicants.
- Placement officers can coordinate placement information and recruitment activities.
- Administrators can oversee users and application data.

## Main Features

### Student

- Registration and account management
- Student profile management
- Job browsing and applications
- Access to placement information and notices

### Company / Recruiter

- Company registration and profile management
- Recruitment opportunity publishing
- Applicant review
- Shortlisting and recruitment workflow support

### Placement Officer

- Placement-related management workflows
- Access to student and company information
- Notice management
- Recruitment coordination support

### Administrator

- Administrative oversight
- User and application-data management

## Technology Stack

### Application

- Python
- Kivy
- KivyMD

### Database

- MySQL
- `mysql-connector-python`

### Supporting Tools

- SMTP email integration
- Pillow
- Python standard-library security primitives

## Security and Maintenance Improvements

I later revisited this student project to apply stronger repository hygiene and authentication practices while preserving its original functionality and architecture. The maintenance work includes:

- Environment-variable-based database and email configuration
- PBKDF2-HMAC-SHA256 password hashing with random salts
- Automatic migration of matching legacy plaintext passwords during login
- Cryptographically secure OTP generation
- Hashed in-memory OTP handling, expiration, and attempt limits
- Password-reset authorization and state management
- Parameterized database operations in authentication-related flows
- Removal of generated builds, IDE metadata, and temporary files from version control
- A safer `.gitignore` and placeholder-only `.env.example`
- Focused unit tests for authentication and OTP behavior

These changes improve the presentation and maintainability of the legacy codebase without representing it as a production-ready system.

## Testing

Run the authentication and security tests with:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

The authentication/security module currently has nine passing tests covering:

- Password hashing and verification
- Random salt behavior
- Failed password verification
- Legacy plaintext-password migration behavior
- OTP success and state clearing
- OTP expiration
- OTP attempt limits

The tests focus on the security functionality introduced during maintenance and do not constitute comprehensive coverage of the complete legacy application.

## Configuration

The application reads database and SMTP configuration from environment variables:

| Variable | Purpose |
| --- | --- |
| `KARIMGANJ_DB_HOST` | MySQL server host |
| `KARIMGANJ_DB_USER` | MySQL user |
| `KARIMGANJ_DB_PASSWORD` | MySQL password |
| `KARIMGANJ_DB_NAME` | MySQL database name |
| `KARIMGANJ_SMTP_EMAIL` | Email address used for SMTP messages |
| `KARIMGANJ_SMTP_PASSWORD` | SMTP or email application password |

See [`.env.example`](.env.example) for placeholder values. Do not commit real credentials or a populated `.env` file.

## Project Background

This repository preserves a project originally created as part of my bachelor's studies. Revisiting it provided an opportunity to improve credential handling, password storage, OTP behavior, SQL safety in authentication flows, automated testing, and repository hygiene while retaining the original user experience.

The original architecture allows the Kivy client to communicate directly with MySQL. This reflects the project's academic context, but it is not the preferred design for a modern production deployment; a backend API should mediate authentication, authorization, validation, and database access.

## Modern Rebuild

A separate modern version of the Karimganj Placement Platform is being developed and planned independently from this repository. Its intended architecture includes:

- React Native with Expo for the client
- FastAPI for the backend
- PostgreSQL for data storage
- REST API communication
- Role-based authorization
- Private object storage
- Automated backend testing
- Clearer application lifecycle management

This modern rebuild is not presented as complete or deployed.

## Project Status

This repository is maintained as a legacy portfolio project for learning, historical reference, and demonstration of continued software-engineering development. It is not currently deployed and should not be considered production-ready.
