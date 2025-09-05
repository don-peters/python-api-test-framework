#!/bin/bash
# Run tests with Allure report generation

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PYTHON="$SCRIPT_DIR/.venv/bin/python"

echo "Running tests with Allure results..."
"$VENV_PYTHON" -m pytest --alluredir=allure-results -v

echo "Generating Allure report..."
if command -v allure &> /dev/null; then
    allure generate allure-results --clean -o allure-report
    echo "Allure report generated in allure-report/"
    echo "To view the report, run: allure open allure-report"
else
    echo "Allure CLI not installed. Install it with:"
    echo "brew install allure (on macOS)"
    echo "Then run: allure serve allure-results"
fi
