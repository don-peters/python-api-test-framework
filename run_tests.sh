#!/bin/bash
# Test runner script for python-api-test-framework
# This ensures tests run with the correct virtual environment

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Path to the virtual environment Python
VENV_PYTHON="$SCRIPT_DIR/.venv/bin/python"

# Check if virtual environment exists
if [ ! -f "$VENV_PYTHON" ]; then
    echo "Error: Virtual environment not found at $VENV_PYTHON"
    echo "Please create a virtual environment first:"
    echo "python -m venv .venv"
    echo "source .venv/bin/activate"
    echo "pip install -r requirements.txt"
    exit 1
fi

# Run pytest with the virtual environment's Python
echo "Running tests with virtual environment Python..."
"$VENV_PYTHON" -m pytest "$@"
