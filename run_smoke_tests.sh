#!/bin/bash
# Additional test runner scripts for different scenarios

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PYTHON="$SCRIPT_DIR/.venv/bin/python"

# Run smoke tests only
echo "Running smoke tests..."
"$VENV_PYTHON" -m pytest -m smoke -v
