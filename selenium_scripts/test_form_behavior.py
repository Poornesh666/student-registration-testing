from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import os

class TestFormBehavior(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, ".."))
        html_file = os.path.join(project_root, "student_registration.html")

        self.driver.get("file:///" + html_file.replace("\\", "/"))

    def fill_valid(self):
        d = self.driver
        d.find_element(By.ID, "name").send_keys("Jyothiswar")
        d.find_element(By.ID, "regno").send_keys("23MIS0146")
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

    # TC_14
    def test_success(self):
        def logic():
            d = self.driver
            self.fill_valid()
            d.find_element(By.ID, "registerBtn").click()
            time.sleep(0.5)
            msg = d.find_element(By.ID, "message").text
            assert "Successfully" in msg

        self.run_test("TC_14", "Submit form with valid inputs", logic)

    # TC_18
    def test_multiple_submit(self):
        def logic():
            d = self.driver
            self.fill_valid()

            for _ in range(2):
                d.find_element(By.TAG_NAME, "button").click()
                time.sleep(0.1) 

            time.sleep(0.4)
            msg = d.find_element(By.ID, "message").text
            assert "Successfully" in msg

        self.run_test("TC_18", "Submit form multiple times consecutively", logic)

    # TC_19
    def test_error_message(self):
        def logic():
            d = self.driver
            d.find_element(By.TAG_NAME, "button").click()

            msg = d.find_element(By.ID, "message").text
            assert "All fields are mandatory!" in msg

        self.run_test("TC_19", "Verify error message is displayed for invalid input", logic)

    # TC_20
    def test_success_message(self):
        def logic():
            d = self.driver
            self.fill_valid()
            d.find_element(By.TAG_NAME, "button").click()
            time.sleep(0.5)
            msg = d.find_element(By.ID, "message").text
            assert "Successfully" in msg

        self.run_test("TC_20", "Verify success message is displayed for valid input", logic)

    # TC_21
    def test_error_message_styling(self):
        def logic():
            d = self.driver
            d.find_element(By.TAG_NAME, "button").click()
            msg_el = d.find_element(By.ID, "message")
            assert "error" in msg_el.get_attribute("class")

        self.run_test("TC_21", "Verify error message styling (red color)", logic)

    # TC_22
    def test_no_reload(self):
        def logic():
            d = self.driver
            url_before = d.current_url

            self.fill_valid()
            d.find_element(By.TAG_NAME, "button").click()

            url_after = d.current_url
            assert url_before == url_after

        self.run_test("TC_22", "Verify form does not reload after submit", logic)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()