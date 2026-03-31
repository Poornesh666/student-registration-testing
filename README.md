# Student Registration & Login Portal

A modern, professional student registration and login application built with HTML, CSS (Glassmorphism), and Vanilla JavaScript. Includes a comprehensive Selenium automation test suite.

## 🚀 Features

- **Premium UI**: Sleek, responsive design with glassmorphism and modern gradients.
- **Login Portal**: Secure-looking login interface with credential validation and feedback.
- **Registration Form**: Comprehensive form for new students with strict validation rules.
- **Form Validation**: Real-time feedback for mandatory fields, name formats, register numbers, and complex passwords.
- **Automation Ready**: Dedicated Selenium test scripts for all critical user flows.

## 📁 Project Structure

- `login.html`: The main entry point for existing students.
- `student_registration.html`: Registration portal for new students.
- `css/style.css`: Unified premium styling (Footlight MT Light).
- `js/script.js`: Core logic, validation, and **localStorage persistence**.
- `selenium_scripts/`: 
    - `test_*.py`: 7 Registration test suites.
    - `login_test_*.py`: 7 Login test suites.
    - `run_tests.py`: Master script to run all 14 test suites.

## 🛠️ Testing Suite

The automation suite has been expanded to **14 individual test suites** (7 for Registration, 7 for Login), covering UI, mandatory fields, format validations, and end-to-end flows.

### Student Names in Tests
The test data has been diversified using:
- **Noel**
- **Amal**
- **Poornesh**
- **Jyothiswar**

### Running all tests:
Navigate to the `selenium_scripts` directory and run:
```bash
python run_tests.py
```

## 🔒 Persistence
Credentials are now stored in an array within the browser's `localStorage`. When a student registers, they are automatically stored on the device, allowing them to login immediately after.

## 📝 Test Case Document
Detailed test case definitions can be found in [test_cases/README.md](file:///c:/Users/VICTUS/student-registration-testing/test_cases/README.md).
