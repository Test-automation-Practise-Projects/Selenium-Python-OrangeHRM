import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.forgetPassword_page import ForgetPasswordPage
from util.base_withoutbrowserclose import BaseTestBrowser
import time

class TestResetFunctionality(BaseTestBrowser):
    def test_reset_button(self):
        self.keep_browser_open = True
        self.loginpage = LoginPage(self.driver)
        self.forgetpasswordpage = ForgetPasswordPage(self.driver)

        # Step 1: Load the login page and navigate to Forgot Password page
        self.loginpage.load()
        self.loginpage.click_forgot_password()
        time.sleep(2)

        # Step 2: Enter valid username and click 'Reset'
        self.forgetpasswordpage.enter_username("Admin")
        self.forgetpasswordpage.click_reset_button()

        # Step 3: Wait for the URL to change to password reset confirmation page
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset")
        )

        # Step 4: Verify the current URL
        current_url = self.driver.current_url
        assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset", \
            f"Expected URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset, but got {current_url}"
