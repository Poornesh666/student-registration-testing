from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegisterNumber(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, ".."))
        html_file = os.path.join(project_root, "student_registration.html")

        self.driver.get("file:///" + html_file.replace("\\", "/"))

        # wait for page load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "regno"))
        )

    def fill_common(self):
        d = self.driver
        d.find_element(By.ID, "name").send_keys("Noel")
        d.find_element(By.ID, "email").send_keys("a@gmail.com")
        d.find_element(By.ID, "password").send_keys("Abc@123")  # fixed
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

    # TC_04
    def test_invalid_format(self):
        def logic():
            d = self.driver
            self.fill_common()
            d.find_element(By.ID, "regno").send_keys("ABC123")
            d.find_element(By.TAG_NAME, "button").click()

            msg = d.find_element(By.ID, "message").text
            assert "Register Number must be in format" in msg

        self.run_test("TC_04", "Enter completely invalid register number", logic)

    # TC_05
    def test_lowercase(self):
        def logic():
            d = self.driver
            self.fill_common()
            d.find_element(By.ID, "regno").send_keys("23mis0146")
            d.find_element(By.TAG_NAME, "button").click()

            msg = d.find_element(By.ID, "message").text
            assert "Register Number must be in format" in msg

        self.run_test("TC_05", "Enter lowercase register number", logic)

    # TC_06
    def test_extra_digits(self):
        def logic():
            d = self.driver
            self.fill_common()
            d.find_element(By.ID, "regno").send_keys("23MIS01467")
            d.find_element(By.TAG_NAME, "button").click()

            msg = d.find_element(By.ID, "message").text
            assert "Register Number must be in format" in msg

        self.run_test("TC_06", "Enter register number with extra digits", logic)

    # TC_07
    def test_special_chars(self):
        def logic():
            d = self.driver
            self.fill_common()
            d.find_element(By.ID, "regno").send_keys("23@IS0146")
            d.find_element(By.TAG_NAME, "button").click()

            msg = d.find_element(By.ID, "message").text
            assert "Register Number must be in format" in msg

        self.run_test("TC_07", "Enter register number with special characters", logic)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)