import unittest

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# --- REGISTRATION TESTS ---
# 1. UI
suite.addTests(loader.loadTestsFromName("test_ui"))

# 2. Mandatory
suite.addTests(loader.loadTestsFromName("test_mandatory"))

# 3. Register Number
suite.addTests(loader.loadTestsFromName("test_register_number"))

# 4. Password
suite.addTests(loader.loadTestsFromName("test_password"))

# 5. Email
suite.addTests(loader.loadTestsFromName("test_email"))

# 6. Name Validation
suite.addTests(loader.loadTestsFromName("test_name_validation"))

# 7. Form Behavior
suite.addTests(loader.loadTestsFromName("test_form_behavior"))

# --- LOGIN TESTS ---
# 1. UI
suite.addTests(loader.loadTestsFromName("login_test_ui"))

# 2. Mandatory
suite.addTests(loader.loadTestsFromName("login_test_mandatory"))

# 3. Email Format
suite.addTests(loader.loadTestsFromName("login_test_email_format"))

# 4. Password Rules
suite.addTests(loader.loadTestsFromName("login_test_password_rules"))

# 5. Invalid Credentials
suite.addTests(loader.loadTestsFromName("login_test_invalid_credentials"))

# 6. Successful Login (End-to-End)
suite.addTests(loader.loadTestsFromName("login_test_successful_login"))

# 7. Form Behavior
suite.addTests(loader.loadTestsFromName("login_test_form_behavior"))

# --- RUNNER ---
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)