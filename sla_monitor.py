"""Infrastructure SLA Monitor.

Load infrastructure availability records, calculate uptime, and identify
service-level agreement (SLA) breaches.
"""

import csv
from pathlib import Path


def calculate_uptime(reporting_minutes: float, downtime_minutes: float) -> float:
    """Return infrastructure uptime as a percentage."""
    if reporting_minutes <= 0:
        raise ValueError("Reporting minutes must be greater than zero.")
    if downtime_minutes < 0:
        raise ValueError("Downtime minutes cannot be negative.")
    if downtime_minutes > reporting_minutes:
        raise ValueError("Downtime cannot exceed the reporting period.")

    uptime_minutes = reporting_minutes - downtime_minutes
    return (uptime_minutes / reporting_minutes) * 100


def evaluate_sla(uptime: float, sla_target: float) -> str:
    """Return PASS when uptime meets the SLA target, otherwise FAIL."""
    if not 0 <= uptime <= 100:
        raise ValueError("Uptime must be between 0 and 100 percent.")
    if not 0 <= sla_target <= 100:
        raise ValueError("SLA target must be between 0 and 100 percent.")

    return "PASS" if uptime >= sla_target else "FAIL"


def load_availability_data(file_path: str | Path) -> list[dict[str, float | str]]:
    """Load and validate infrastructure availability records from a CSV file."""
    records: list[dict[str, float | str]] = []

    with open(file_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        required_fields = {
            "site",
            "reporting_minutes",
            "downtime_minutes",
            "sla_target",
        }
        if not reader.fieldnames or not required_fields.issubset(reader.fieldnames):
            raise ValueError("CSV file is missing one or more required columns.")

        for row in reader:
            site = row["site"].strip()
            if not site:
                raise ValueError("Site name cannot be empty.")

            try:
                reporting_minutes = float(row["reporting_minutes"])
                downtime_minutes = float(row["downtime_minutes"])
                sla_target = float(row["sla_target"])
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Invalid numeric data for site: {site}") from exc

            uptime = calculate_uptime(reporting_minutes, downtime_minutes)
            status = evaluate_sla(uptime, sla_target)

            records.append(
                {
                    "site": site,
                    "reporting_minutes": reporting_minutes,
                    "downtime_minutes": downtime_minutes,
                    "sla_target": sla_target,
                    "uptime": uptime,
                    "status": status,
                }
            )

    return records


if __name__ == "__main__":
    data_path = Path(__file__).parent / "data" / "sample_availability.csv"
    records = load_availability_data(data_path)

    print("Infrastructure SLA Monitor")
    print("-" * 70)
    print(f"{'Site':<20}{'Uptime':>12}{'SLA':>12}{'Status':>12}")
    print("-" * 70)

    for record in records:
        print(
            f"{record['site']:<20}"
            f"{record['uptime']:>11.5f}%"
            f"{record['sla_target']:>11.3f}%"
            f"{record['status']:>12}"
        )
