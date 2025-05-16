# Selenium Python Automation Framework

This is an automated test framework built with Selenium WebDriver and Python, designed to demonstrate end-to-end web UI testing using pytest and data-driven techniques.

## Features
- Supports Chrome, Firefox, and Edge browsers
- Browser notifications are disabled for cleaner test runs
- Tests are parameterized and configurable via command-line arguments
- Logs and reports for better debugging and analysis

## Important Notes

- This framework is intentionally designed so that **one test case will fail** due to an assertion error, while another will pass. This demonstrates handling of both passing and failing scenarios.

- Occasionally, when running tests, you might encounter an **"element not interactable"** error caused by cookie pop-ups or page state.  
  In such cases, please **rerun the tests** after the first run, as cookies and session data will be saved, helping avoid this issue.

## Project Structure

selenium-python-test-framework
/
│
├── base/
│   ├── base_driver.py
│
├── pages/
│   ├── yatra_launch_page.py
│   └── search_flights_results_page.py
│
├── testcases/
│   ├── conftest.py
│   └── test_searchflights.py
│
├── testdata/
│   ├── testdatacsv.csv    # CSV test data
│   ├── testdataexcel.xlsx     # Excel test data
│   ├── testyaml.yaml         # YAML test data
│   └── testdata.json         # JSON test data
│
├── utilities/
│   └── utils.py
│
└── automation.log

## How to Run

```bash
pytest --browser chrome --url https://www.yatra.com/ --html=Automation_report.html

