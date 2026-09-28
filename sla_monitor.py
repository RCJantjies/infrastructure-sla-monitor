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


def evaluate_sla(uptime: float, sla_target: float) -> str:
    """Return PASS when uptime meets the SLA target, otherwise FAIL."""
    if not 0 <= uptime <= 100:
        raise ValueError("Uptime must be between 0 and 100 percent.")
    if not 0 <= sla_target <= 100:
        raise ValueError("SLA target must be between 0 and 100 percent.")

    return "PASS" if uptime >= sla_target else "FAIL"


if __name__ == "__main__":
    example_uptime = calculate_uptime(43_200, 2)
    example_status = evaluate_sla(example_uptime, 99.99)

    print("Infrastructure SLA Monitor")
    print("-" * 26)
    print(f"Example uptime: {example_uptime:.5f}%")
    print(f"SLA target:     {99.99:.3f}%")
    print(f"SLA status:     {example_status}")
