import pytest
from selenium.webdriver import Keys
from pages.login_page import LoginPage
from util.base import BaseTest
import time

class TestLogin(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.load()  # Load the login page for every test

    # Helper method to clear input field (username or password) using backspace
    def clear_input(self, element, input_text):
        input_length = len(input_text)
        for _ in range(input_length):
            element.send_keys(Keys.BACKSPACE)
        time.sleep(1)

    # Helper method to verify error message visibility and disappearance
    def verify_error_message(self, field_type, expected_visible=True):
        if field_type == "username":
            if expected_visible:
                assert self.loginpage.is_username_required_error_displayed(), "Username required message not displayed"
            else:
                assert self.loginpage.is_username_error_message_not_visible(), "Error message should not be visible after typing"
        elif field_type == "password":
            if expected_visible:
                assert self.loginpage.is_password_required_error_displayed(), "Password required message not displayed"
            else:
                assert self.loginpage.is_password_error_message_not_visible(), "Error message should not be visible after typing"

    @pytest.mark.login
    def test_clear_username(self):
        # Enter a username and clear it
        self.loginpage.enter_username("Ad")
        time.sleep(1)

        # Clear the username using the helper method
        username_element = self.driver.find_element(*self.loginpage.username_field)
        self.clear_input(username_element, "Ad")

        # Verify the error message is displayed
        self.verify_error_message("username")

        # Start typing again and check if the error message disappears
        self.loginpage.enter_username("Admin")
        self.verify_error_message("username", expected_visible=False)

    @pytest.mark.login
    def test_clear_password(self):
        # Enter a password and clear it
        self.loginpage.enter_password("Ad")
        time.sleep(1)

        # Clear the password using the helper method
        password_element = self.driver.find_element(*self.loginpage.password_field)
        self.clear_input(password_element, "Ad")

        # Verify the error message is displayed
        self.verify_error_message("password")

        # Start typing again and check if the error message disappears
        self.loginpage.enter_password("Admin")
        self.verify_error_message("password", expected_visible=False)
