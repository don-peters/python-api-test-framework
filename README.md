API Testing Framework
A clean, maintainable Python API testing framework demonstrating best practices for automated API testing. Built with pytest, requests, and Allure reporting.

✨ Features
Clean Test Patterns - Simple arrange/act/assert structure
JSON Schema Validation - Comprehensive response validation
Beautiful Reports - Rich Allure HTML reports with detailed failure analysis
Easy to Extend - Add new endpoints and tests effortlessly
Beginner Friendly - Clear, readable code with extensive documentation
Professional Patterns - Industry best practices for API testing
🚀 Quick Start
Prerequisites
Python 3.8+
pip (Python package manager)
Installation
Clone the repository:
bash
git clone <your-repo-url>
cd api-testing-framework
Create a virtual environment:
bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
Install dependencies:
bash
pip install -r requirements.txt
Running Tests
Option 1: Simple test run

bash
pytest
Option 2: With Allure reporting

bash
pytest --alluredir=reports/allure-results -v
allure serve reports/allure-results
Option 3: Using the test runner (recommended)

bash
python run_tests.py
📁 Project Structure
api-testing-framework/
├── README.md
├── requirements.txt
├── pytest.ini                 # Pytest configuration
├── conftest.py                # Global test fixtures
├── run_tests.py              # Test runner script
│
├── clients/                   # API client classes
│   ├── __init__.py
│   ├── base_client.py        # Base HTTP client
│   └── jsonplaceholder_client.py  # JSONPlaceholder API client
│
├── schemas/                   # JSON schema definitions
│   ├── user.json             # User object schema
│   ├── user_partial.json     # Partial user schema (for updates)
│   └── users_list.json       # Users array schema
│
├── test_data/                 # Test data factories
│   ├── __init__.py
│   └── users.py              # User test data
│
├── tests/                     # Test files
│   ├── __init__.py
│   ├── test_users_api.py     # User API endpoint tests
│   └── test_schema_validation.py  # Schema validation tests
│
├── utils/                     # Utility functions
│   ├── __init__.py
│   └── assertions.py         # Custom assertion helpers
│
└── reports/                   # Generated test reports
    └── allure-results/       # Allure test results
🧪 Test Examples
Simple API Test
python
def test_get_single_user_success(self):
    """Test retrieving single user by ID."""
    # Arrange
    user_id = 1
    
    # Act
    response = self.client.get_user(user_id)
    
    # Assert
    assert_status_code(response, 200)
    assert_response_time(response, 2.0)
    
    user_data = response.json()
    assert_contains_keys(user_data, ["id", "name", "username", "email"])
    assert_json_schema(user_data, "user")
    assert user_data["id"] == user_id
Schema Validation Test
python
def test_valid_user_passes_schema(self):
    """Test that properly structured user data passes validation."""
    # Arrange
    user_data = {
        "id": 1,
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com"
    }
    
    # Act & Assert
    assert_json_schema(user_data, "user")
📊 Reports
The framework generates detailed Allure reports that include:

Test Results Overview - Pass/fail summary with trends
Detailed Test Steps - Clear breakdown of each test action
Request/Response Data - Full HTTP details for debugging
Schema Validation Results - Detailed validation failure information
Performance Metrics - Response time tracking
Historical Trends - Test result history over time
Viewing Reports
After running tests with Allure:

bash
allure serve reports/allure-results
This opens an interactive HTML report in your browser with:

📈 Test execution trends
🔍 Detailed failure analysis
📝 Request/response logging
⚡ Performance metrics
🛠️ Adding New Tests
1. Add New API Client Method
python
# In clients/jsonplaceholder_client.py
def get_posts(self) -> requests.Response:
    """Get all posts."""
    return self.get("posts")
2. Create Test Data
python
# In test_data/posts.py
class PostTestData:
    @staticmethod
    def valid_post():
        return {
            "title": "Test Post",
            "body": "This is a test post",
            "userId": 1
        }
3. Add JSON Schema
json
// In schemas/post.json
{
  "type": "object",
  "properties": {
    "id": {"type": "integer"},
    "title": {"type": "string"},
    "body": {"type": "string"},
    "userId": {"type": "integer"}
  },
  "required": ["id", "title", "body", "userId"]
}
4. Write Tests
python
# In tests/test_posts_api.py
def test_get_all_posts_success(self):
    """Test retrieving all posts."""
    # Arrange - no setup needed
    
    # Act
    response = self.client.get_posts()
    
    # Assert
    assert_status_code(response, 200)
    assert_json_schema(response.json(), "posts_list")
🎯 Design Philosophy
This framework prioritizes:

Simplicity - Easy to understand, even for beginners
Maintainability - Clear separation of concerns
Readability - Self-documenting test structure
Extensibility - Simple patterns for adding new functionality
Professional Quality - Industry best practices
Key Patterns
Arrange/Act/Assert - Clear test structure
Page Object Model - For API clients
Factory Pattern - For test data generation
Custom Assertions - For descriptive failures
Schema-First Validation - Comprehensive response verification
📚 Dependencies
pytest - Test framework
requests - HTTP client library
jsonschema[format] - JSON schema validation with format support
allure-pytest - Rich HTML reporting
🤝 Contributing
This project demonstrates API testing best practices. When contributing:

Follow the existing patterns and structure
Keep tests simple and readable
Add appropriate documentation
Ensure all tests pass
Update schemas when adding new endpoints
📝 License
MIT License - feel free to use this framework as a starting point for your own API testing projects.

🎓 Learning Resources
This framework demonstrates several important concepts:

API Testing Fundamentals - HTTP methods, status codes, response validation
Test Automation Patterns - Page objects, test data factories, custom assertions
JSON Schema Validation - Structure and format validation
Test Reporting - Rich HTML reports with debugging information
Python Testing - pytest features, fixtures, parameterization
Perfect for developers looking to learn professional API testing practices!
