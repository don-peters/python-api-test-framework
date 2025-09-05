#!/bin/bash
# Run tests with HTML report

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PYTHON="$SCRIPT_DIR/.venv/bin/python"

echo "Running tests with HTML report..."
"$VENV_PYTHON" -m pytest --html=report/report.html --self-contained-html -v
