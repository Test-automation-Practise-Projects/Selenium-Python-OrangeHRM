import os
import pytest
from pages.login_page import LoginPage
from util.base import BaseTest


class TestLogin(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.loginpage = LoginPage(self.driver)  # Common setup
        self.loginpage.load()  # Load the login page for every test

    @pytest.mark.login
    def test_login_empty_fields(self):
        # Click on the login button with both fields empty
        self.loginpage.click_login_button()

        # Assert username and password required errors are displayed
        assert self.loginpage.is_username_required_error_displayed(), "Username required message not displayed"
        assert self.loginpage.is_password_required_error_displayed(), "Password required message not displayed"

    @pytest.mark.login
    def test_login_only_username(self):
        # Enter only the username and click login
        self.loginpage.enter_username("Admin")
        self.loginpage.click_login_button()

        # Assert password required error is displayed
        assert self.loginpage.is_password_required_error_displayed(), "Password required message not displayed"

    @pytest.mark.login
    def test_login_only_password(self):
        # Enter only the password and click login
        self.loginpage.enter_password("admin123")
        self.loginpage.click_login_button()

        # Assert username required error is displayed
        assert self.loginpage.is_username_required_error_displayed(), "Username required message not displayed"
