import driver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.directory_page import DirectoryPage
from tests.Login.test_login_valid_credentials import TestLoginValidCredentials


@pytest.mark.usefixtures("successful_login")
class TestNavigateToDirectory(TestLoginValidCredentials):

    def test_navigate_to_directory(self):
        directory_page = DirectoryPage(self.driver)


        # Use the method from the page object to navigate to the directory page
        directory_page.click_directory_option()

        # Validate if the Directory page is loaded (example: check URL or some element on the page)
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory"),
            "URL did not change to dashboard after successful login"
        )
