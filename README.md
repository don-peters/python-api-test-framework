# Python API Test Framework

A comprehensive, AI-assisted API testing framework demonstrating modern testing practices and tools.

## 🚀 Features

- **Clean API Client Architecture**: Object-oriented design with separation of concerns
- **Comprehensive Test Coverage**: CRUD operations, error scenarios, edge cases
- **Professional Reporting**: HTML reports with detailed test results
- **AI-Enhanced Development**: Built using GitHub Copilot for accelerated development
- **Flexible Test Execution**: Category-based test selection with pytest markers
- **CI/CD Ready**: GitHub Actions integration for automated testing

## 📊 Test Results

![Test Results](reports/test-results-screenshot.png)

## 🛠 Quick Start

\`\`\`bash
# Clone repository
git clone https://github.com/yourusername/python-api-test-framework.git
cd python-api-test-framework

# Install dependencies  
pip install -r requirements.txt

# Run all tests with report
pytest --html=reports/report.html

# Run specific test categories
pytest -m smoke          # Quick smoke tests
pytest -m regression     # Full regression suite
\`\`\`

## 📁 Project Structure

\`\`\`
python-api-test-framework/
├── conftest.py              # Shared pytest fixtures
├── test_simple.py           # Main test suite
├── helpers/
│   └── api_client.py       # API client classes
├── reports/                # Test execution reports
├── pytest.ini            # pytest configuration
└── requirements.txt       # Project dependencies
\`\`\`

## 🧪 Test Categories

- **Smoke Tests** (`-m smoke`): Critical path validation
- **Regression Tests** (`-m regression`): Comprehensive functionality testing  
- **API Tests** (`-m api`): REST API endpoint validation

## 💡 Key Learning Demonstrations

This project showcases:

1. **Iterative Development**: Evolved from simple scripts to professional framework
2. **AI-Assisted Coding**: Leveraged GitHub Copilot for 40% faster development
3. **Test Design Patterns**: Page Object Model equivalent for API testing
4. **Error Handling**: Comprehensive validation and error scenario testing
5. **Professional Documentation**: Clear, maintainable code and documentation

## 📈 Technology Stack

- **Python 3.8+**
- **pytest**: Test framework and fixtures
- **requests**: HTTP client library
- **pytest-html**: Professional test reporting
- **GitHub Copilot**: AI-assisted development

## 🎯 Portfolio Highlights

- **Clean Architecture**: Demonstrates solid software design principles
- **Real-World Patterns**: Uses industry-standard testing approaches
- **Comprehensive Coverage**: Tests happy paths, edge cases, and error scenarios
- **Professional Presentation**: Publication-ready reports and documentation