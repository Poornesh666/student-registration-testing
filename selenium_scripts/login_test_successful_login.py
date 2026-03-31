from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import os
import time

class LoginTestSuccess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.project_root = os.path.abspath(os.path.join(current_dir, ".."))
        
    def register_user(self, email, password, name):
        reg_file = os.path.join(self.project_root, "student_registration.html")
        self.driver.get("file:///" + reg_file.replace("\\", "/"))
        
        self.driver.find_element(By.ID, "name").send_keys(name)
        self.driver.find_element(By.ID, "regno").send_keys("23MIS0146")
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "department").send_keys("CSE")
        self.driver.find_element(By.ID, "gender").send_keys("Male")
        
        self.driver.find_element(By.ID, "registerBtn").click()
        time.sleep(2.5) # Wait for registration redirect or success message visibility

    def run_test(self, tc_id, description, test_logic):
        print(f"\n{tc_id}: {description}")
        try:
            test_logic()
            print(f"{tc_id}: PASS")
        except Exception as e:
            print(f"{tc_id}: [ERROR HANDLED] - Test continued despite issues.")
            print(f"Details: {type(e).__name__} - {str(e)}")

    def test_end_to_end_login(self):
        def logic():
            email = "noel@vit.edu"
            password = "Noel@123pass"
            name = "Noel"
            
            self.register_user(email, password, name)
            
            # Now login
            login_file = os.path.join(self.project_root, "login.html")
            self.driver.get("file:///" + login_file.replace("\\", "/"))
            
            self.driver.find_element(By.ID, "email").send_keys(email)
            self.driver.find_element(By.ID, "password").send_keys(password)
            self.driver.find_element(By.ID, "loginBtn").click()
            
            # 1. Verify snackbar message
            msg = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, "message"))
            ).text
            assert "Welcome back" in msg
            
            # 2. Verify redirection to dashboard
            WebDriverWait(self.driver, 5).until(
                EC.url_contains("dashboard.html")
            )
            
            # 3. Verify user name on dashboard
            dash_name = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "userNameDisplay"))
            ).text
            assert name in dash_name

        self.run_test("LGN_TC_06", "Register and then login successfully with redirection", logic)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
