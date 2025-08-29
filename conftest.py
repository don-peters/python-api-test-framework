# conftest.py
import pytest
from helpers.api_client import JSONPlaceholderClient, HTTPBinClient

@pytest.fixture(scope="session")
def api_client():
    """Shared API client for all tests"""
    return JSONPlaceholderClient()

@pytest.fixture(scope="session")
def httpbin_client():
    """Shared HTTPBin client for error testing"""
    return HTTPBinClient()