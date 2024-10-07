import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from util.base_withoutbrowserclose import BaseTestBrowser

class TestLoginValidCredentials(BaseTestBrowser):

    @pytest.fixture(scope="class")
    def successful_login(self):
        self.loginpage = LoginPage(self.driver)

        # Load the login page
        self.loginpage.load()

        # Enter valid username and password
        self.loginpage.enter_username("Admin")
        self.loginpage.enter_password("admin123")
        self.loginpage.click_login_button()

        # Verify successful login by checking the URL
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/dashboard/index"),
            "URL did not change to dashboard after successful login"
        )
