import pytest
from pages.login_page import LoginPage
from util.base import BaseTest

class TestLoginInvalidCredentials(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.loginpage = LoginPage(self.driver)  # Initialize LoginPage
        self.loginpage.load()  # Load the login page for each test

    @pytest.mark.login
    def test_login_invalid_username(self):
        # Enter invalid username and valid password
        self.loginpage.enter_username("InvalidUser")
        self.loginpage.enter_password("admin123")
        self.loginpage.click_login_button()

        # Assert invalid credentials error is displayed
        assert self.loginpage.is_invalid_credentials_error_displayed(), "Invalid credentials message not displayed"

    @pytest.mark.login
    def test_login_invalid_password(self):
        # Enter valid username and invalid password
        self.loginpage.enter_username("Admin")
        self.loginpage.enter_password("InvalidPass")
        self.loginpage.click_login_button()

        # Assert invalid credentials error is displayed
        assert self.loginpage.is_invalid_credentials_error_displayed(), "Invalid credentials message not displayed"

    @pytest.mark.login
    def test_login_invalid_username_and_password(self):
        # Enter invalid username and invalid password
        self.loginpage.enter_username("InvalidUser")
        self.loginpage.enter_password("InvalidPass")
        self.loginpage.click_login_button()

        # Assert invalid credentials error is displayed
        assert self.loginpage.is_invalid_credentials_error_displayed(), "Invalid credentials message not displayed"
