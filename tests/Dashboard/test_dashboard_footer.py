import logging
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.dashboard_page import DashboardPage
from tests.Login.test_login_valid_credentials import TestLoginValidCredentials
from util.base_withoutbrowserclose import BaseTestBrowser

class TestDashboardFooterActions(TestLoginValidCredentials):

    @pytest.mark.usefixtures("successful_login")
    def test_footer_actions(self):
        dashboard_page = DashboardPage(self.driver)

        # Footer actions
        dashboard_page.click_footer_link()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        original_window = self.driver.current_window_handle

        # Switch to new window
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])

        # Verify URL
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://www.orangehrm.com/"),
            "URL did not change to the expected site page"
        )

        self.driver.close()
        self.driver.switch_to.window(original_window)

        # Click logo and verify URL
        dashboard_page.click_logo()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://www.orangehrm.com/"),
            "URL did not change to home page of OrangeHRM"
        )
