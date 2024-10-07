import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from util.base_withoutbrowserclose import BaseTestBrowser

class TestNavigationToForgotPasswordPage(BaseTestBrowser):
    def test_navigate_to_forgot_password_page(self):
        self.keep_browser_open = True
        self.loginpage = LoginPage(self.driver)

        # Step 1: Load the login page
        self.loginpage.load()

        # Step 2: Click on the 'Forgot Password' link
        self.loginpage.click_forgot_password()

        # Step 3: Wait for the URL to change to the forgot password page
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
        )

        # Step 4: Verify the current URL
        current_url = self.driver.current_url
        assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode", \
            f"Expected URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode, but got {current_url}"
