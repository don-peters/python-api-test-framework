"""
Custom assertion utilities for clear, descriptive test failures.
Makes test assertions readable and provides detailed error messages.
"""
import json
import jsonschema
from pathlib import Path
from typing import Dict, Any, Union
import requests
import allure


def assert_status_code(response: requests.Response, expected_code: int) -> None:
    """Assert response has expected status code with clear error message."""
    actual_code = response.status_code
    
    # Attach response details to allure report
    allure.attach(
        json.dumps({
            "status_code": actual_code,
            "url": response.url,
            "headers": dict(response.headers),
            "body": response.text[:1000]  # First 1000 chars
        }, indent=2),
        name="Response Details",
        attachment_type=allure.attachment_type.JSON
    )
    
    assert actual_code == expected_code, (
        f"Expected status code {expected_code}, but got {actual_code}. "
        f"URL: {response.url}, Response: {response.text[:200]}"
    )


def assert_response_time(response: requests.Response, max_seconds: float) -> None:
    """Assert response time is under threshold."""
    actual_time = response.elapsed.total_seconds()
    assert actual_time <= max_seconds, (
        f"Response took {actual_time:.2f}s, expected under {max_seconds}s"
    )


def assert_json_schema(data: Union[Dict, list], schema_name: str) -> None:
    """Assert data matches JSON schema with descriptive error."""
    schema_path = Path(__file__).parent.parent / "schemas" / f"{schema_name}.json"
    
    if not schema_path.exists():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")
    
    with open(schema_path, 'r') as f:
        schema = json.load(f)
    
    try:
        # Enable format validation for email, etc.
        jsonschema.validate(data, schema, format_checker=jsonschema.FormatChecker())
        allure.attach(
            f"✓ Data matches {schema_name} schema",
            name="Schema Validation",
            attachment_type=allure.attachment_type.TEXT
        )
    except jsonschema.ValidationError as e:
        # Attach validation details to report
        allure.attach(
            json.dumps({
                "schema": schema_name,
                "error": str(e),
                "failed_data": data
            }, indent=2),
            name="Schema Validation Failure",
            attachment_type=allure.attachment_type.JSON
        )
        raise AssertionError(f"Data does not match {schema_name} schema: {e.message}")


def assert_contains_keys(data: Dict[str, Any], required_keys: list) -> None:
    """Assert dictionary contains all required keys."""
    missing_keys = [key for key in required_keys if key not in data]
    assert not missing_keys, (
        f"Missing required keys: {missing_keys}. Available keys: {list(data.keys())}"
    )


def assert_not_empty(data: Union[Dict, list, str]) -> None:
    """Assert data is not empty with type-specific error message."""
    if isinstance(data, dict):
        assert data, "Dictionary is empty"
    elif isinstance(data, list):
        assert data, "List is empty"
    elif isinstance(data, str):
        assert data.strip(), "String is empty or whitespace"
    else:
        assert data, f"Data is empty: {data}"