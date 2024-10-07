from telnetlib import EC

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from util.base import BaseTest

class TestHomeActions(BaseTest):
    def test_home_actions(self):
        self.keep_browser_open = True  # Set flag to keep the browser open
        self.loginpage = LoginPage(self.driver)

        self.loginpage.load()

        #Click on 'Forgot Password' and navigate back to the login screen
        self.loginpage.click_forgot_password()
        time.sleep(2)
        self.driver.back()  # Go back to the login page
        time.sleep(1)

        # Click on the LinkedIn icon, which opens a new tab
        self.loginpage.click_linkedin_icon()
        time.sleep(3)

        # Switch to the LinkedIn tab (second tab)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])  # Switch to the newly opened tab
        time.sleep(2)

        # Switch back to the original login tab
        self.driver.switch_to.window(windows[0])


        self.loginpage.click_facebook_icon()
        time.sleep(3)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.switch_to.window(windows[0])

        self.loginpage.click_twitter_icon()
        time.sleep(3)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.switch_to.window(windows[0])

        self.loginpage.click_youtube_icon()
        time.sleep(3)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.switch_to.window(windows[0])