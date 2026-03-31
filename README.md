# 🎓 Student Registration & Login Portal

A premium, modern web application for student registration and authentication. This project features a high-end Glassmorphism UI, robust client-side validation, and a comprehensive Selenium-based automation test suite to ensure system reliability.

---

## ✨ Features

### 🖥️ High-End User Interface
- **Modern Glassmorphism UI**: High-impact design with sleek transparency and professional aesthetics.
- **Dynamic Gradients**: Vibrant and accessible color schemes for a premium feel.
- **Responsive Layout**: Designed to work seamlessly across different device screen sizes.

### 📝 Student Registration
- **Strict Validation**: Real-time validation for mandatory fields, name formats, and institutional registration numbers.
- **Password Security Checks**: Built-in logic to ensure strong passwords (length, special characters, cases).
- **Email Validation**: Automated format checks to ensure institutional email compliance.

### 🔐 Authentication & Portal
- **Secure Login**: Responsive login interface with advanced error messaging.
- **Persistence**: Uses `localStorage` for data persistence, allowing immediate login after registration.
- **User Dashboard**: Personalized student view upon successful authentication.

### 🧪 Automation Suite
- **14+ Test Suites**: Comprehensive coverage of both Registration and Login modules.
- **Validated Cross-Browser Logic**: Selenium scripts designed for consistent execution and verification.
- **Master Runner**: Single-command execution for the entire test ecosystem.

---

## 📁 Project Structure

```text
├── css/                   # Stylesheets for glassmorphism and components
├── js/                    # Core logic and storage management
├── selenium_scripts/      # Automated testing suite
│   ├── run_tests.py       # Master test runner
│   └── *.py               # Individual test modules
├── test_cases/            # Documentation for quality assurance
├── login.html             # Entry point: Student portal login
├── student_registration.html # Student onboarding portal
├── dashboard.html         # Post-authentication student dashboard
└── README.md              # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- **Web Browser**: Latest version of Chrome or Firefox.
- **Python (for testing)**: Version 3.8+ for running automation.
- **WebDriver**: Relevant driver (e.g., ChromeDriver) placed in your system path.

### Installation
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Poornesh666/student-registration-testing.git
    cd student-registration-testing
    ```
2.  **Open the App**:
    Simply open `login.html` in your favorite browser.

---

## 🧪 Automation & Testing

We maintain a high-quality codebase through automated verification.

### Setup Testing Environment
1.  Navigate to the `selenium_scripts` directory.
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running Tests
To execute the full suite (14 tests), run the master script from the `selenium_scripts` folder:
```bash
python run_tests.py
```

For more details on individual test cases, see [selenium_scripts/README.md](file:///c:/Users/VICTUS/student-registration-testing/selenium_scripts/README.md).

---

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3 (Custom Glassmorphism), Vanilla JavaScript.
- **Storage**: Browser LocalStorage.
- **Testing Engine**: Selenium WebDriver (Python).
- **Reporting**: Python Unit Testing Framework.

---

## 👤 Credits

Developed as part of a high-end Software Quality Assurance and Web Development project. Special focus on Noel, Amal, Poornesh, and Jyothiswar for the modern test data integration.
