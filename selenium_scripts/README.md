#  Selenium Automation Testing Suite

This directory contains the complete Selenium test suite for the Student Registration and Login Portal. The automation is designed to verify UI elements, form logic, and end-to-end user flows.

---

##  Test Categories

###  Registration Suite (7 Tests)
1. **test_ui.py**: Verifies page title, layout, and visual elements.
2. **test_mandatory.py**: Ensures the system identifies and marks all required fields.
3. **test_register_number.py**: Validates strict registration number patterns (e.g., 202*).
4. **test_password.py**: Tests password complexity rules (length, upper, lower, special).
5. **test_email.py**: Checks for valid institutional email formats.
6. **test_name_validation.py**: Ensures names contain only alphabetic characters.
7. **test_form_behavior.py**: Verifies form reset and submission logic.

###  Login Suite (7 Tests)
1. **login_test_ui.py**: Checks the login page layout and branding.
2. **login_test_mandatory.py**: Tests field requirement enforcement on login.
3. **login_test_email_format.py**: Validates email input field on the login page.
4. **login_test_password_rules.py**: Ensures login password field follows security masks.
5. **login_test_invalid_credentials.py**: Verifies correct error handling for wrong data.
6. **login_test_successful_login.py**: End-to-end flow from login to the dashboard.
7. **login_test_form_behavior.py**: Validates UI feedback during authentication attempts.

---

##  Execution Instructions

### Prerequisites
Ensure you have the following installed:
- **Python 3.x**
- **Selenium Library**: `pip install selenium`
- **ChromeDriver**: Compatible with your installed version of Google Chrome.

### Running all tests in one go
Execute the master runner script:
```bash
python run_tests.py
```

### Running individual test suites
You can run any specific suite by calling it directly via Python:
```bash
python test_name_validation.py
```
*(Example: Verifying student name validation)*

---

## 📊 Test Observation

All tests use the `unittest` framework. Upon execution, the console will display:
- **`.`**: Test passed successfully.
- **`F`**: Assertion failure (logic mismatch).
- **`E`**: Software error (e.g., element not found).

A summary report will be generated at the end of the execution showing the total time and pass/fail count.
