from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import os

class LoginTestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, ".."))
        html_file = os.path.join(project_root, "login.html")
        self.driver.get("file:///" + html_file.replace("\\", "/"))

        # wait for page load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginBtn"))
        )

    def run_test(self, tc_id, description, test_logic):
        print(f"\n{tc_id}: {description}")
        try:
            test_logic()
            print(f"{tc_id}: PASS")
        except AssertionError as e:
            print(f"{tc_id}: FAIL")
            raise e

    def test_login_page_load(self):
        def logic():
            page_source = self.driver.page_source
            assert "Welcome Back" in page_source
            assert self.driver.find_element(By.ID, "email").is_displayed()
            assert self.driver.find_element(By.ID, "password").is_displayed()

        self.run_test("LGN_TC_01", "Verify login page elements are present", logic)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
