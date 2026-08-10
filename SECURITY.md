# Security Policy

## Overview

The `python-basics` repository is an educational project designed to help beginners learn Python programming.

Although this repository primarily contains learning materials and beginner-friendly projects, security issues and vulnerabilities should still be reported responsibly.

---

## Supported Versions

This repository is continuously developed on the main branch.

| Version        | Supported |
| -------------- | --------- |
| Latest version | ✅ Yes     |
| Older versions | ❌ No      |

Only the latest version of the repository is actively maintained.

---

## Reporting a Security Issue

If you discover a potential security vulnerability in this repository, please report it privately rather than creating a public GitHub issue.

When reporting a security issue, please provide:

* A clear description of the vulnerability
* The affected file or project
* Steps to reproduce the issue
* The potential impact
* Any suggested solution, if available

Please avoid publicly sharing sensitive information, credentials, API keys, or other secrets.

---

## API Keys and Secrets

Some projects may use external services or APIs.

Never commit:

* API keys
* Passwords
* Access tokens
* Private credentials
* `.env` files containing secrets
* Other sensitive configuration data

Use environment variables or a `.env` file for local development.

For example:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

A `.env.example` file may be provided as a safe template.

---

## Security Best Practices

When working with this repository:

1. Never commit secrets to GitHub.
2. Keep dependencies updated.
3. Validate user input.
4. Handle exceptions appropriately.
5. Review third-party packages before installing them.
6. Do not expose API keys in source code.
7. Use environment variables for sensitive configuration.
8. Avoid sharing sensitive information in issues or pull requests.

---

## Educational Purpose

The projects in this repository are designed for learning purposes. Some projects intentionally use simplified implementations to make concepts easier for beginners to understand.

These projects should not be used as production-ready implementations of security-sensitive systems such as banking, authentication, payment processing, or financial services.

---

## Responsible Disclosure

Please allow maintainers reasonable time to investigate and address a reported security issue before publicly disclosing it.

Thank you for helping keep this project safe and educational for everyone.
