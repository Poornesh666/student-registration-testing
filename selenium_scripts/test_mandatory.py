from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import os

class TestMandatory(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, ".."))
        html_file = os.path.join(project_root, "student_registration.html")

        self.driver.get("file:///" + html_file.replace("\\", "/"))

    def run_test(self, tc_id, description, test_logic):
        print(f"\n{tc_id}: {description}")
        try:
            test_logic()
            print(f"{tc_id}: PASS")
        except AssertionError as e:
            print(f"{tc_id}: FAIL")
            raise e

    # TC_02
    def test_empty_form(self):
        def logic():
            d = self.driver
            d.find_element(By.TAG_NAME, "button").click()
            msg = d.find_element(By.ID, "message").text
            assert "All fields are mandatory!" in msg

        self.run_test("TC_02", "Submit empty form", logic)

    # TC_03
    def test_partial_form(self):
        def logic():
            d = self.driver
            d.find_element(By.ID, "name").send_keys("Poornesh")
            d.find_element(By.TAG_NAME, "button").click()
            msg = d.find_element(By.ID, "message").text
            assert "All fields are mandatory!" in msg

        self.run_test("TC_03", "Submit partially filled form (only name)", logic)

    # TC_12
    def test_department_not_selected(self):
        def logic():
            d = self.driver
            d.find_element(By.ID, "name").send_keys("Amal")
            d.find_element(By.ID, "regno").send_keys("23MIS0146")
            d.find_element(By.ID, "email").send_keys("a@gmail.com")
            d.find_element(By.ID, "password").send_keys("Abc@123")  # fixed
            d.find_element(By.ID, "gender").send_keys("Male")
            d.find_element(By.TAG_NAME, "button").click()
            msg = d.find_element(By.ID, "message").text
            assert "All fields are mandatory!" in msg

        self.run_test("TC_12", "Submit form without selecting department", logic)

    # TC_13
    def test_gender_not_selected(self):
        def logic():
            d = self.driver
            d.find_element(By.ID, "name").send_keys("Aman")
            d.find_element(By.ID, "regno").send_keys("23MIS0146")
            d.find_element(By.ID, "email").send_keys("a@gmail.com")
            d.find_element(By.ID, "password").send_keys("Abc@123")  # fixed
            d.find_element(By.ID, "department").send_keys("CSE")
            d.find_element(By.TAG_NAME, "button").click()
            msg = d.find_element(By.ID, "message").text
            assert "All fields are mandatory!" in msg

        self.run_test("TC_13", "Submit form without selecting gender", logic)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()