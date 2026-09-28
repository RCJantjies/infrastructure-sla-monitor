# Infrastructure SLA Monitor

A Python command-line tool for monitoring infrastructure availability, calculating uptime, and identifying service-level agreement (SLA) breaches.

## Business Problem

Infrastructure and facilities teams often manage services against contractual or internal availability targets. Reviewing downtime records manually can make it harder to identify exceptions consistently. This project demonstrates a simple, repeatable workflow for converting availability records into SLA performance results.

## Features

- Loads infrastructure availability records from CSV
- Calculates uptime percentages from reporting and downtime minutes
- Compares actual uptime with an SLA target
- Classifies each record as `PASS` or `FAIL`
- Validates invalid reporting periods, downtime values, and SLA percentages
- Includes automated unit tests for calculations, validation, and CSV processing

## Repository Structure

```text
infrastructure-sla-monitor/
├── data/
│   └── sample_availability.csv
├── tests/
│   └── test_sla_monitor.py
├── sla_monitor.py
├── README.md
├── .gitignore
└── LICENSE
```

## Sample Data

The included dataset contains fictional infrastructure records with:

- Site name
- Reporting period in minutes
- Downtime in minutes
- SLA target percentage

**All infrastructure records in this repository are synthetic and are provided solely for demonstration purposes. No employer, client, or production operational data is used.**

## Requirements

- Python 3.9 or later
- No third-party packages

## Usage

Clone or download the repository, open a terminal in the project directory, and run:

```bash
python sla_monitor.py
```

Example output:

```text
Infrastructure SLA Monitor
----------------------------------------------------------------------
Site                      Uptime         SLA      Status
----------------------------------------------------------------------
DC-East                99.99537%     99.990%        PASS
DC-West                99.96528%     99.990%        FAIL
Office-North           99.91898%     99.900%        PASS
```

## Testing

Run the automated test suite with:

```bash
python -m unittest discover -s tests
```

The current test suite covers uptime calculations, SLA pass/fail evaluation, invalid operational inputs, SLA validation, and CSV ingestion.

Local validation on 28 September 2026 confirmed that all eight automated tests passed.

## Technical Design

The application separates the workflow into three core functions:

- `calculate_uptime()` validates availability inputs and calculates uptime.
- `evaluate_sla()` validates percentage values and evaluates SLA compliance.
- `load_availability_data()` ingests CSV records and applies the calculation and evaluation logic.

Python's standard library is used deliberately so the initial version remains lightweight and demonstrates core language capabilities.

## Limitations

This version uses a static CSV dataset and terminal output. It does not provide persistent storage, trend analysis, visualization, alerting, live infrastructure integrations, or predictive analytics.

## Future Development

Potential future milestones include:

- Historical SLA trend analysis
- Data visualization and dashboards
- Persistent storage
- Automated exception reporting
- Infrastructure monitoring integrations
- Anomaly detection or predictive analysis

Future capabilities will be added only where they provide a meaningful engineering increment.

## Project Status

**Version 0.1 — portfolio release**

The application has been functionally tested locally and its eight automated tests pass.

## License

Released under the MIT License.
