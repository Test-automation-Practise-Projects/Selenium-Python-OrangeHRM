# helpers/maintenance_helpers.py

import time
from selenium.webdriver import Keys
from pages.login_page import LoginPage
from pages.maintenance_page import MaintenancePage

class MaintenanceHelpers:
    def __init__(self, driver):
        self.driver = driver
        self.loginpage = LoginPage(driver)
        self.maintenancepage = MaintenancePage(driver)

    def login_and_navigate_to_maintenance(self, username="admin", password="admin123"):
        """
        Helper method to log in and navigate to the maintenance page.
        """
        self.loginpage.load()
        self.loginpage.login(username, password)
        self.maintenancepage.click_maintainennec_option()
        time.sleep(1)

    def clear_input(self, element, input_text):
        """
        Helper method to clear input fields by sending backspace for each character.
        """
        for _ in range(len(input_text)):
            element.send_keys(Keys.BACKSPACE)
        time.sleep(1)

    def verify_error_message(self, field, expected_visible=True):
        """
        Helper method to verify if error message is displayed or not based on the input field.
        """
        if field == "password":
            if expected_visible:
                assert self.maintenancepage.is_error_message_displayed(), "'Required' error message should be displayed."
            else:
                assert not self.maintenancepage.is_error_message_displayed(), "'Required' error message should be gone."
