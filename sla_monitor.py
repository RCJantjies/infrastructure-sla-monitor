"""Infrastructure SLA Monitor.

Core calculations for evaluating infrastructure availability against
service-level agreement (SLA) targets.
"""


def calculate_uptime(reporting_minutes: float, downtime_minutes: float) -> float:
    """Return infrastructure uptime as a percentage.

    Args:
        reporting_minutes: Total minutes in the reporting period.
        downtime_minutes: Minutes the asset or service was unavailable.

    Raises:
        ValueError: If the reporting period or downtime is invalid.
    """
    if reporting_minutes <= 0:
        raise ValueError("Reporting minutes must be greater than zero.")
    if downtime_minutes < 0:
        raise ValueError("Downtime minutes cannot be negative.")
    if downtime_minutes > reporting_minutes:
        raise ValueError("Downtime cannot exceed the reporting period.")

    uptime_minutes = reporting_minutes - downtime_minutes
    return (uptime_minutes / reporting_minutes) * 100


if __name__ == "__main__":
    example_uptime = calculate_uptime(43_200, 2)
    print("Infrastructure SLA Monitor")
    print("-" * 26)
    print(f"Example uptime: {example_uptime:.5f}%")
