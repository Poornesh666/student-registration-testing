import unittest

loader = unittest.TestLoader()
suite = unittest.TestSuite()

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

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)