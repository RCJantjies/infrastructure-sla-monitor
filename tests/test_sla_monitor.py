"""Tests for the Infrastructure SLA Monitor."""

import tempfile
import unittest
from pathlib import Path

from sla_monitor import calculate_uptime, evaluate_sla, load_availability_data


class TestSLAMonitor(unittest.TestCase):
    """Test uptime calculations, SLA evaluation, and CSV processing."""

    def test_zero_downtime_returns_full_uptime(self) -> None:
        self.assertEqual(calculate_uptime(43_200, 0), 100.0)

    def test_normal_downtime_calculation(self) -> None:
        uptime = calculate_uptime(43_200, 2)
        self.assertAlmostEqual(uptime, 99.9953703704)

    def test_uptime_above_sla_passes(self) -> None:
        self.assertEqual(evaluate_sla(99.995, 99.99), "PASS")

    def test_uptime_below_sla_fails(self) -> None:
        self.assertEqual(evaluate_sla(99.97, 99.99), "FAIL")

    def test_downtime_cannot_exceed_reporting_period(self) -> None:
        with self.assertRaises(ValueError):
            calculate_uptime(60, 61)

    def test_negative_downtime_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            calculate_uptime(60, -1)

    def test_invalid_sla_target_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            evaluate_sla(99.9, 101)

    def test_csv_data_is_loaded_and_evaluated(self) -> None:
        csv_content = (
            "site,reporting_minutes,downtime_minutes,sla_target\n"
            "Test-DC,43200,15,99.99\n"
        )

        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "availability.csv"
            csv_path.write_text(csv_content, encoding="utf-8")
            records = load_availability_data(csv_path)

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["site"], "Test-DC")
        self.assertEqual(records[0]["status"], "FAIL")


if __name__ == "__main__":
    unittest.main()
