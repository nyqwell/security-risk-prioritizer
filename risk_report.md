# Security Risk Report

This report was generated from a sample security risk register.

## Executive Summary

- Total risks reviewed: **6**
- Critical residual risks: **0**
- High residual risks: **2**
- Medium residual risks: **2**
- Low residual risks: **2**

## Prioritized Risk Register

| ID | Asset | Risk | Category | Inherent | Controls | Residual | Level | Owner |
|---|---|---|---|---:|---|---:|---|---|
| R-002 | Cloud Storage | Misconfigured storage exposes sensitive data | Cloud Security | 15 | None | 15.0 | High | Cloud Team |
| R-001 | Customer Web App | Weak administrator authentication | Identity & Access | 20 | Partial | 14.0 | High | Security Engineering |
| R-004 | Internal API | Excessive service-account permissions | Identity & Access | 12 | Partial | 8.4 | Medium | Platform Engineering |
| R-003 | Employee Accounts | Phishing leads to account compromise | Human Risk | 16 | Implemented | 6.4 | Medium | Security Operations |
| R-006 | Vendor SaaS | Third-party outage interrupts business process | Third-Party Risk | 6 | Partial | 4.2 | Low | Business Operations |
| R-005 | Laptop Fleet | Delayed security patching leaves known vulnerabilities | Vulnerability Management | 9 | Implemented | 3.6 | Low | IT Operations |

## Top Risks Requiring Attention

- **R-002 – Misconfigured storage exposes sensitive data**: residual score 15.0 (High); owner: Cloud Team.
- **R-001 – Weak administrator authentication**: residual score 14.0 (High); owner: Security Engineering.

## Scoring Method

- Inherent risk score = Likelihood × Impact (each rated 1–5).
- Residual risk applies a simple control-effectiveness multiplier:
  - Implemented = 0.4
  - Partial = 0.7
  - None = 1.0
- Risk levels: Low 1–5, Medium 6–10, High 11–15, Critical 16–25.

> Note: This is an educational model using synthetic data, not a production risk methodology.
