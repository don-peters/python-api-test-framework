#!/usr/bin/env python3
"""
Test runner script for API testing framework.
Ensures proper Allure report generation.
"""
import os
import sys
import subprocess
from pathlib import Path


def main():
    """Run tests and generate Allure reports."""
    
    # Ensure reports directory exists
    reports_dir = Path("reports/allure-results")
    reports_dir.mkdir(parents=True, exist_ok=True)
    
    # Clean previous results
    if reports_dir.exists():
        for file in reports_dir.glob("*"):
            file.unlink()
    
    print("🚀 Running API tests with Allure reporting...")
    
    # Run pytest with Allure
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        "--alluredir=reports/allure-results",
        "-v"
    ])
    
    if result.returncode == 0:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed. Check the results above.")
    
    # Generate Allure report
    print("\n📊 Generating Allure report...")
    try:
        subprocess.run([
            "allure", "generate", "reports/allure-results", 
            "--output", "reports/allure-report", "--clean"
        ], check=True)
        print("✅ Allure report generated at: reports/allure-report/")
        print("To view report: allure serve reports/allure-results")
    except subprocess.CalledProcessError:
        print("⚠️  Allure command not found. Install with: pip install allure-pytest")
        print("Or view results in reports/allure-results/")
    except FileNotFoundError:
        print("⚠️  Allure CLI not installed. Results saved to reports/allure-results/")
        print("Install Allure CLI for HTML reports: https://docs.qameta.io/allure/#_installing_a_commandline")


if __name__ == "__main__":
    main()