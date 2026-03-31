from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import os

class LoginTestInvalidCredentials(unittest.TestCase):

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
        except AssertionError as e:
            print(f"{tc_id}: FAIL")
            raise e

    def test_wrong_credentials(self):
        def logic():
            d = self.driver
            d.find_element(By.ID, "email").send_keys("unknown_user@example.com")
            d.find_element(By.ID, "password").send_keys("NoPass123!@")
            d.find_element(By.ID, "loginBtn").click()

            msg = d.find_element(By.ID, "message").text
            assert "Invalid credentials" in msg

        self.run_test("LGN_TC_05", "Login with unregistered email", logic)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
