import pytest
from selenium.webdriver import Keys
from pages.login_page import LoginPage
from pages.forgetPassword_page import ForgetPasswordPage
from util.base_withoutbrowserclose import BaseTestBrowser
import time

class TestErrorValidations(BaseTestBrowser):

    # Setup method for common actions
    @pytest.fixture(autouse=True)
    def setup(self):
        self.keep_browser_open = True
        self.loginpage = LoginPage(self.driver)
        self.forgetpasswordpage = ForgetPasswordPage(self.driver)

        # Load the login page and navigate to Forgot Password page
        self.loginpage.load()
        self.loginpage.click_forgot_password()
        time.sleep(2)

    # Helper function to clear the username using backspace
    def clear_username(self, username):
        username_element = self.driver.find_element(*self.forgetpasswordpage.username_field)
        username_length = len(username)
        for _ in range(username_length):
            username_element.send_keys(Keys.BACKSPACE)
        time.sleep(1)

    # Helper function to verify the error message
    def verify_error_message(self, expected_message="Required"):
        assert self.forgetpasswordpage.is_error_message_visible(), "Error message should be visible."
        assert self.forgetpasswordpage.get_error_message() == expected_message, f"Unexpected error message. Expected: {expected_message}"

    # Step 2: Click on 'Reset' without entering a username and verify error message
    def test_reset_without_username(self):
        self.forgetpasswordpage.click_reset_button()
        time.sleep(2)

        # Verify error message
        self.verify_error_message()

    # Step 3: Enter and clear username to trigger error again
    def test_clear_username_triggers_error(self):
        # Enter a username and clear it
        self.forgetpasswordpage.enter_username("Ad")
        time.sleep(1)

        # Clear the username using the helper function
        self.clear_username("Ad")

        # Verify error message
        self.verify_error_message()

    # Test error clearance when entering valid data after triggering error
    def test_error_clearance(self):
        # Enter and clear a username
        self.forgetpasswordpage.enter_username("Ad")
        time.sleep(1)

        # Clear the username using the helper function
        self.clear_username("Ad")

        # Verify the error message is displayed again
        self.verify_error_message()

        # Start typing again to check if error message disappears
        self.forgetpasswordpage.enter_username("Admin")
        assert self.forgetpasswordpage.is_error_message_not_visible(), "Error message should not be visible after typing."
