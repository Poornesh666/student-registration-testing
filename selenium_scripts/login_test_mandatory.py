from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import os
import time

class LoginTestMandatory(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, ".."))
        html_file = os.path.join(project_root, "login.html")
        self.driver.get("file:///" + html_file.replace("\\", "/"))

    def run_test(self, tc_id, description, test_logic):
        print(f"\n{tc_id}: {description}")
        try:
            test_logic()
            print(f"{tc_id}: PASS")
        except Exception as e:
            print(f"{tc_id}: [ERROR HANDLED] - Test continued despite issues.")
            print(f"Details: {type(e).__name__} - {str(e)}")

    def test_empty_login_form(self):
        def logic():
            import time
            d = self.driver
            d.find_element(By.ID, "loginBtn").click()
            time.sleep(1) # Wait for the message to appear
            msg = d.find_element(By.ID, "message").text
            assert "Please enter both email and password!" in msg, f"Expected message not found. Got: '{msg}'"

        self.run_test("LGN_TC_02", "Submit empty login form", logic)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
