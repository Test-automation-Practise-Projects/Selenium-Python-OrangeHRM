import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from tests.Login.test_login_valid_credentials import TestLoginValidCredentials

class TestDashboardHeaderActions(TestLoginValidCredentials):
    @pytest.mark.usefixtures("successful_login")

    def test_header_actions(self):

        dashboard_page = DashboardPage(self.driver)

        # Header actions
        dashboard_page.click_dropdown_icon()
        dashboard_page.click_support_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/help/support"),
            "URL did not change to support page after clicking support option"
        )

        time.sleep(2)
        self.driver.back()
        time.sleep(2)

        dashboard_page.click_dropdown_icon()
        dashboard_page.click_changePassword_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/pim/updatePassword"),
            "URL did not change to Change password page after clicking change password option"
        )
        time.sleep(2)
        self.driver.back()

        dashboard_page.click_dropdown_icon()
        dashboard_page.click_upgrade_button()

        # Wait for the new tab to open and get the window handles
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        # Get the current window handles (tabs)
        original_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        # Switch to the new tab
        self.driver.switch_to.window(all_windows[1])
        # Verify the URL of the new tab
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://orangehrm.com/open-source/upgrade-to-advanced"),
            "URL did not change to the expected upgrade page"
        )
        time.sleep(2)
        # Close the new tab and switch back to the original tab
        self.driver.close()
        self.driver.switch_to.window(original_window)

        # dashboard_page.click_sidebar_toggle()
        # time.sleep(2)
        # dashboard_page.click_sidebar_toggle()


        dashboard_page.click_dropdown_icon()

        dashboard_page.click_about_option()
        time.sleep(2)
        dashboard_page.click_about_close_button()


        dashboard_page.click_help_button()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        original_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://starterhelp.orangehrm.com/hc/en-us"),
            "URL did not change to the expected help page"
        )
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(original_window)

        dashboard_page.click_dropdown_icon()

        dashboard_page.click_logout_option()


