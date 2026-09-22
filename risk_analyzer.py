import csv
from pathlib import Path

INPUT_FILE = Path("risks.csv")
OUTPUT_FILE = Path("risk_report.md")

CONTROL_MULTIPLIERS = {
    "implemented": 0.4,
    "partial": 0.7,
    "none": 1.0,
}

def risk_level(score: float) -> str:
    if score >= 16:
        return "Critical"
    if score >= 11:
        return "High"
    if score >= 6:
        return "Medium"
    return "Low"

def load_risks(path: Path):
    risks = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        required = {
            "id", "asset", "risk", "category", "likelihood",
            "impact", "control_status", "owner"
        }
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

        for row in reader:
            likelihood = int(row["likelihood"])
            impact = int(row["impact"])

            if not 1 <= likelihood <= 5 or not 1 <= impact <= 5:
                raise ValueError(
                    f"{row['id']}: likelihood and impact must be between 1 and 5."
                )

            control_status = row["control_status"].strip().lower()
            if control_status not in CONTROL_MULTIPLIERS:
                raise ValueError(
                    f"{row['id']}: control_status must be Implemented, Partial, or None."
                )

            inherent_score = likelihood * impact
            residual_score = round(
                inherent_score * CONTROL_MULTIPLIERS[control_status], 1
            )

            row["likelihood"] = likelihood
            row["impact"] = impact
            row["inherent_score"] = inherent_score
            row["inherent_level"] = risk_level(inherent_score)
            row["residual_score"] = residual_score
            row["residual_level"] = risk_level(residual_score)
            risks.append(row)

    return risks

def build_report(risks):
    ranked = sorted(risks, key=lambda r: r["residual_score"], reverse=True)

    counts = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0}
    for risk in ranked:
        counts[risk["residual_level"]] += 1

    lines = [
        "# Security Risk Report",
        "",
        "This report was generated from a sample security risk register.",
        "",
        "## Executive Summary",
        "",
        f"- Total risks reviewed: **{len(ranked)}**",
        f"- Critical residual risks: **{counts['Critical']}**",
        f"- High residual risks: **{counts['High']}**",
        f"- Medium residual risks: **{counts['Medium']}**",
        f"- Low residual risks: **{counts['Low']}**",
        "",
        "## Prioritized Risk Register",
        "",
        "| ID | Asset | Risk | Category | Inherent | Controls | Residual | Level | Owner |",
        "|---|---|---|---|---:|---|---:|---|---|",
    ]

    for r in ranked:
        lines.append(
            f"| {r['id']} | {r['asset']} | {r['risk']} | {r['category']} | "
            f"{r['inherent_score']} | {r['control_status']} | {r['residual_score']} | "
            f"{r['residual_level']} | {r['owner']} |"
        )

    lines += [
        "",
        "## Top Risks Requiring Attention",
        "",
    ]

    top = [r for r in ranked if r["residual_level"] in {"Critical", "High"}]
    if not top:
        lines.append("No Critical or High residual risks were identified.")
    else:
        for r in top:
            lines.append(
                f"- **{r['id']} – {r['risk']}**: residual score "
                f"{r['residual_score']} ({r['residual_level']}); owner: {r['owner']}."
            )

    lines += [
        "",
        "## Scoring Method",
        "",
        "- Inherent risk score = Likelihood × Impact (each rated 1–5).",
        "- Residual risk applies a simple control-effectiveness multiplier:",
        "  - Implemented = 0.4",
        "  - Partial = 0.7",
        "  - None = 1.0",
        "- Risk levels: Low 1–5, Medium 6–10, High 11–15, Critical 16–25.",
        "",
        "> Note: This is an educational model using synthetic data, not a production risk methodology.",
    ]

    return "\n".join(lines)

def main():
    risks = load_risks(INPUT_FILE)
    report = build_report(risks)
    OUTPUT_FILE.write_text(report, encoding="utf-8")

    print(f"Analyzed {len(risks)} risks.")
    print(f"Report created: {OUTPUT_FILE.resolve()}")

if __name__ == "__main__":
    main()
