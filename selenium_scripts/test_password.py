from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPassword(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, ".."))
        html_file = os.path.join(project_root, "student_registration.html")

        self.driver.get("file:///" + html_file.replace("\\", "/"))

    def fill_required_fields(self):
        d = self.driver
        d.find_element(By.ID, "name").send_keys("Amal")
        d.find_element(By.ID, "regno").send_keys("23MIS0146")
        d.find_element(By.ID, "email").send_keys("test@gmail.com")
        d.find_element(By.ID, "department").send_keys("CSE")
        d.find_element(By.ID, "gender").send_keys("Male")

    def run_test(self, tc_id, description, test_logic):
        print(f"\n{tc_id}: {description}")
        try:
            test_logic()
            print(f"{tc_id}: PASS")
        except AssertionError as e:
            print(f"{tc_id}: FAIL")
            raise e

    # TC_08
    def test_short_password(self):
        def logic():
            d = self.driver
            d.find_element(By.ID, "password").send_keys("123")
            self.fill_required_fields()
            d.find_element(By.TAG_NAME, "button").click()

            msg = d.find_element(By.ID, "message").text
            assert "Password must be at least 6 characters" in msg

        self.run_test("TC_08", "Enter weak password", logic)

    # TC_09
    def test_valid_password(self):
        def logic():
            d = self.driver
            d.find_element(By.ID, "password").send_keys("Abc@123")  # strong password
            self.fill_required_fields()
            d.find_element(By.TAG_NAME, "button").click()

            msg = d.find_element(By.ID, "message").text
            assert "Successfully" in msg

        self.run_test("TC_09", "Enter valid strong password", logic)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)