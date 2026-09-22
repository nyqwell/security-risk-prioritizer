# Security Risk Prioritizer

A small Python project that turns a security risk register into a prioritized, leadership-friendly report.

I built this project to practice **security risk management, GRC concepts, data analysis, process automation, and technical-to-business communication**.

## What it does

The tool:

- reads security risks from a CSV risk register
- validates likelihood and impact ratings
- calculates **inherent risk**
- applies a simple control-effectiveness model
- calculates **residual risk**
- ranks risks by priority
- generates an executive-style Markdown report

## Why I built it

Security teams do more than identify technical problems—they also need to explain which risks matter most and help decision-makers prioritize resources.

This project models that process using a simple and transparent scoring method.

## Risk model

**Inherent risk**

`Likelihood × Impact`

Both values are rated from 1–5.

**Residual risk**

`Inherent Risk × Control Multiplier`

| Control Status | Multiplier |
|---|---:|
| Implemented | 0.4 |
| Partial | 0.7 |
| None | 1.0 |

Risk levels:

- Low: 1–5
- Medium: 6–10
- High: 11–15
- Critical: 16–25

> This project uses a simplified educational scoring model and synthetic data. It is not intended to represent a production enterprise risk methodology.

## Example

Input:

```csv
R-002,Cloud Storage,Misconfigured storage exposes sensitive data,Cloud Security,3,5,None,Cloud Team
```

The script calculates:

- inherent risk = `3 × 5 = 15`
- no implemented control means multiplier = `1.0`
- residual risk = `15`
- priority = **High**

## Run the project

Requires Python 3. No third-party packages are needed.

```bash
python risk_analyzer.py
```

The program reads `risks.csv` and creates:

```text
risk_report.md
```

## Project structure

```text
security-risk-prioritizer/
├── risk_analyzer.py
├── risks.csv
├── risk_report.md
├── README.md
└── .gitignore
```

## Skills demonstrated

- Python
- Security Risk Management
- Governance, Risk & Compliance (GRC)
- Risk Assessment
- Data Analysis
- Process Automation
- Security Controls
- Identity & Access Risk
- Cloud Security Risk
- Vulnerability Management
- Stakeholder Communication

## What I would add next

Future improvements could include:

- configurable risk thresholds
- risk trends over time
- CSV export of prioritized risks
- a dashboard
- mappings between risks and security controls
- integration with vulnerability or cloud-security data sources
