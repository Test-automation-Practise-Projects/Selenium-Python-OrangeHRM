from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time
from pages.login_page import LoginPage
from util.base import BaseTest

class TestLogin(BaseTest):
    def test_login(self):
        self.keep_browser_open = True  # Set flag to keep the browser open
        self.loginpage = LoginPage(self.driver)

        # Step 1: Load the login page
        self.loginpage.load()

        # Step 2: Keep both fields empty and click on the login button
        self.loginpage.click_login_button()
        time.sleep(1)  # Wait for error messages to appear
        assert self.loginpage.is_username_required_error_displayed(), "Username required message not displayed"
        assert self.loginpage.is_password_required_error_displayed(), "Password required message not displayed"


        # Step 3: Enter only username and click on the login button
        self.loginpage.enter_username("Admin")
        self.loginpage.click_login_button()
        time.sleep(1)
        assert self.loginpage.is_password_required_error_displayed(), "Password required message not displayed"

        # Step 4: Enter only password and click on the login button
        self.loginpage.load()
        self.loginpage.enter_password("admin123")
        self.loginpage.click_login_button()
        time.sleep(1)
        assert self.loginpage.is_username_required_error_displayed(), "Username required message not displayed"


        # Step 5: Enter a username and clear it to trigger the error again
        self.loginpage.enter_username("Ad")
        time.sleep(1)
        # Simulate backspacing all the letters typed
        username_element = self.driver.find_element(*self.loginpage.username_field)
        username_length = len("Ad")
        # Use backspace to remove all characters
        for _ in range(username_length):
            username_element.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        # Verify the error message is displayed again
        assert self.loginpage.is_username_required_error_displayed(), "Username required message not displayed"
        #Start typing again to check if error message disappears
        self.loginpage.enter_username("Admin")
        assert self.loginpage.is_username_error_message_not_visible(), "Error message should not be visible after typing."


        # Step 6: Enter a password and clear it to trigger the error again
        self.loginpage.load()
        self.loginpage.enter_password("Ad")
        time.sleep(1)
        # Simulate backspacing all the letters typed
        password_element = self.driver.find_element(*self.loginpage.password_field)
        password_length = len("Ad")
        # Use backspace to remove all characters
        for _ in range(password_length):
            password_element.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        # Verify the error message is displayed again
        assert self.loginpage.is_password_required_error_displayed(), "Password required message not displayed"
        #Start typing again to check if error message disappears
        self.loginpage.enter_password("Admin")
        assert self.loginpage.is_password_error_message_not_visible(), "Error message should not be visible after typing."


        # Step 7: Click on the login button after entering an incorrect username
        self.loginpage.load()
        self.loginpage.enter_username("InvalidUser")
        self.loginpage.enter_password("admin123")
        self.loginpage.click_login_button()
        time.sleep(1)
        assert self.loginpage.is_invalid_credentials_error_displayed(), "Invalid credentials message not displayed"

        # Step 8: Click on the login button after entering an incorrect password
        self.loginpage.load()
        self.loginpage.enter_username("Admin")
        self.loginpage.enter_password("InvalidPass")
        self.loginpage.click_login_button()
        time.sleep(1)
        assert self.loginpage.is_invalid_credentials_error_displayed(), "Invalid credentials message not displayed"

        # Step 9: Click on the login button after entering an incorrect username and password
        self.loginpage.load()
        self.loginpage.enter_username("InvalidUser")
        self.loginpage.enter_password("InvalidPass")
        self.loginpage.click_login_button()
        time.sleep(1)
        assert self.loginpage.is_invalid_credentials_error_displayed(), "Invalid credentials message not displayed"


        # Step 10: Click on the login button after entering valid credentials
        self.loginpage.load()
        self.loginpage.enter_username("Admin")
        self.loginpage.enter_password("admin123")
        self.loginpage.click_login_button()
        time.sleep(2)

        # Verify successful login by checking the URL
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        ), "URL did not change to dashboard after successful login"