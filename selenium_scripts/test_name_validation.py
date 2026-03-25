from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import os

class TestNameValidation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, ".."))
        html_file = os.path.join(project_root, "student_registration.html")

        self.driver.get("file:///" + html_file.replace("\\", "/"))

    def fill_required_fields(self):
        d = self.driver
        d.find_element(By.ID, "regno").send_keys("23MIS0146")
        d.find_element(By.ID, "email").send_keys("test@gmail.com")
        d.find_element(By.ID, "password").send_keys("Abc@123")  # strong password
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

    # TC_14
    def test_numeric_name(self):
        def logic():
            d = self.driver
            d.find_element(By.ID, "name").send_keys("12345")
            self.fill_required_fields()
            d.find_element(By.TAG_NAME, "button").click()

            msg = d.find_element(By.ID, "message").text
            assert "Name must contain only alphabets!" in msg

        self.run_test("TC_14", "Enter numeric values in name field", logic)

    # TC_15
    def test_special_char_name(self):
        def logic():
            d = self.driver
            d.find_element(By.ID, "name").send_keys("@#$%")
            self.fill_required_fields()
            d.find_element(By.TAG_NAME, "button").click()

            msg = d.find_element(By.ID, "message").text
            assert "Name must contain only alphabets!" in msg

        self.run_test("TC_15", "Enter special characters in name field", logic)

    # TC_16
    def test_spaces_only(self):
        def logic():
            d = self.driver
            d.find_element(By.ID, "name").send_keys("   ")
            self.fill_required_fields()
            d.find_element(By.TAG_NAME, "button").click()

            msg = d.find_element(By.ID, "message").text
            assert "All fields are mandatory!" in msg

        self.run_test("TC_16", "Enter only spaces in name field", logic)

    # TC_17
    def test_long_name(self):
        def logic():
            d = self.driver
            d.find_element(By.ID, "name").send_keys("A"*100)
            self.fill_required_fields()
            d.find_element(By.TAG_NAME, "button").click()

            msg = d.find_element(By.ID, "message").text
            assert "Successfully" in msg

        self.run_test("TC_17", "Enter very long name input", logic)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()