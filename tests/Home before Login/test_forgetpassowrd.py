import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.forgetPassword_page import ForgetPasswordPage
from util.base import BaseTest
from util.base_withoutbrowserclose import BaseTestBrowser


class TestForgetPassword(BaseTestBrowser):
    def test_forget_password(self):
        self.keep_browser_open = True
        self.loginpage = LoginPage(self.driver)
        self.forgetpasswordpage = ForgetPasswordPage(self.driver)

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
        time.sleep(2)

        # Step 5: Click on 'Cancel' to navigate back to the login screen
        self.forgetpasswordpage.click_cancel_button()
        time.sleep(2)

        self.loginpage.click_forgot_password()
        time.sleep(2)

        # Step 6: Click on 'Reset' without entering a username
        self.forgetpasswordpage.click_reset_button()
        time.sleep(2)

        # Step 7: Verify the error message is displayed
        assert self.forgetpasswordpage.is_error_message_visible(), "Error message should be visible."
        assert self.forgetpasswordpage.get_error_message() == "Required", "Unexpected error message."

        # Step 8: Enter a username and clear it to trigger the error again
        self.forgetpasswordpage.enter_username("Ad")
        time.sleep(1)

        # Simulate backspacing all the letters typed
        username_element = self.driver.find_element(*self.forgetpasswordpage.username_field)
        username_length = len("Ad")

        # Use backspace to remove all characters
        for _ in range(username_length):
            username_element.send_keys(Keys.BACKSPACE)

        time.sleep(1)

        # Step 9: Verify the error message is displayed again
        assert self.forgetpasswordpage.is_error_message_visible(), "Error message should be visible."
        assert self.forgetpasswordpage.get_error_message() == "Required", "Unexpected error message."


        # Step 10: Start typing again to check if error message disappears
        self.forgetpasswordpage.enter_username("Admin")
        assert self.forgetpasswordpage.is_error_message_not_visible(), "Error message should not be visible after typing."

        # Step 11: Click on 'Reset' after entering a username
        self.forgetpasswordpage.click_reset_button()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset")
        )

        current_url = self.driver.current_url
        assert current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset", \
            f"Expected URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset, but got {current_url}"

        time.sleep(2)