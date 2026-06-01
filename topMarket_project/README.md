🛒 TopMarket Automation Project
End-to-End Testing with Python & Playwright
This repository contains a professional automation framework for testing the TopMarket e-commerce platform. The project is built using the Page Object Model (POM) pattern to ensure maintainability, scalability, and clean code.

🛠 Tech Stack
Language: Python 3.12+

Testing Framework: Pytest

Automation Tool: Playwright (Fast, reliable, and supports modern web apps)

Reporting: Allure Reports (Detailed visual execution logs)

CI/CD: GitHub Actions (Automated test runs on every push)

🏗 Project Structure
pages/: Contains Page Objects (e.g., item_page.py, cart_page.py) with encapsulated locators and actions.

tests/: Test suites categorized by functionality (e.g., test_add_to_cart.py).

conftest.py: Global fixtures, including browser setup and function-level scoping.

github/workflows/: CI configuration for running tests in the cloud.

🚀 Recent Improvements
Strict Mode Stability: Refined locators using get_by_role to prevent "Multiple elements found" errors.

Overlay Handling: Implemented force=True and explicit popup closures to handle intermittent UI notifications in CI environments.

Enhanced Timeouts: Optimized conftest.py with 15s timeouts to support stable execution on GitHub Actions runners.

🚦 How to Run
Install dependencies:

Bash
pip install -r requirements.txt
playwright install
Run tests:

Bash
   pytest --alluredir=allure-results
View Report:

Bash
allure serve allure-results