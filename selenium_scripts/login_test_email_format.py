from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import os

class LoginTestEmailFormat(unittest.TestCase):

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

    def test_invalid_login_email(self):
        def logic():
            d = self.driver
            d.find_element(By.ID, "email").send_keys("invalidemail")
            d.find_element(By.ID, "password").send_keys("Pass@123")
            d.find_element(By.ID, "loginBtn").click()

            email_field = d.find_element(By.ID, "email")
            validity = email_field.get_attribute("validationMessage")
            assert validity != ""  

        self.run_test("LGN_TC_03", "Enter invalid email format in login", logic)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
