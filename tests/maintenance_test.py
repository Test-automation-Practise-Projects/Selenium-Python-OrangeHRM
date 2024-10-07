import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.maintenance_page import MaintenancePage
from pages.login_page import LoginPage
from tests.successfulLogin_test import TestSuccesfulLogin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMaintenancePage(TestSuccesfulLogin):

    def test_maintenance_popup(self):
        # Step 1: Login
        self.loginpage = LoginPage(self.driver)
        self.test_successful_login()

        maintenancepopup = MaintenancePage(self.driver)
        maintenancepopup.click_maintainennec_option()

        # Step 2: Click on cancel button and verify URL
        maintenancepopup.click_cancel_button()
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index", "URL did not match after clicking cancel button."
        maintenancepopup.click_maintainennec_option()

        # Step 3: Verify username is autofilled and disabled
        assert maintenancepopup.is_username_disabled(), "Username field should be disabled."
        assert maintenancepopup.driver.find_element(*maintenancepopup.username_field).get_attribute("value") != "", "Username field should be autofilled."

        # Step 4: Verify 'Required' error message when clicking confirm button with empty password
        maintenancepopup.click_confirm_button()
        assert maintenancepopup.is_error_message_displayed(), "'Required' error message should be displayed."

        # Step 5: Enter password and check if error disappears
        maintenancepopup.enter_password("testPassword")
        assert not maintenancepopup.is_error_message_displayed(), "'Required' error message should be gone."

        # Step 6: Enter a password and clear it to trigger the error again
        maintenancepopup.loadpage()
        maintenancepopup.enter_password("Ad")
        time.sleep(1)
        password_element = self.driver.find_element(*self.loginpage.password_field)
        password_length = len("Ad")
        for _ in range(password_length):
            password_element.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        assert maintenancepopup.is_error_message_displayed(), "'Required' error message should be displayed again."

        maintenancepopup.loadpage()
        maintenancepopup.enter_password("admidddddd")
        maintenancepopup.click_confirm_button()
        time.sleep(1)
        assert maintenancepopup.is_invalid_credentials_error_displayed(), "Invalid credentials message not displayed."

        # Step 7: Enter password again and click save button
        maintenancepopup.loadpage()
        maintenancepopup.enter_password("admin123")
        maintenancepopup.click_confirm_button()
        assert maintenancepopup.is_on_purge_employee_page(), "Should be on Purge Employee Records page."
        self.test_click_employeerecords_search_button()

    def test_click_employeerecords_search_button(self):
        maintenancepopup = MaintenancePage(self.driver)

        failed_steps = []

        try:
            # Step 2: Click search button without entering anything
            maintenancepopup.click_employeerecords_search_button()

            # Step 3: Verify 'Required' error message is displayed
            assert maintenancepopup.is_hints_field_error_message_displayed(), "Expected 'Required' error message is not displayed."
            print("Error message is displayed correctly when the field is empty.")
        except AssertionError as e:
            print(f"Assertion failed: {str(e)}")
            failed_steps.append(f"Step 3 failed: {str(e)}")

        try:
            # Step 4: Enter text into the field and verify the error disappears
            maintenancepopup.enter_text_in_hints_field("Test")
            time.sleep(1)
            assert not maintenancepopup.is_hints_field_error_message_displayed(), "Error message should disappear after entering text."
            print("Error message disappears after entering text.")
        except AssertionError as e:
            print(f"Assertion failed: {str(e)}")
            failed_steps.append(f"Step 4 failed: {str(e)}")

        try:
            # Step 5: Backspace all the typed text and verify the error reappears
            hints_field_element = self.driver.find_element(*maintenancepopup.hints_field)
            for _ in range(len("Test")):
                hints_field_element.send_keys(Keys.BACKSPACE)

            time.sleep(1)
            assert maintenancepopup.is_hints_field_error_message_displayed(), "Expected 'Required' error message should appear again after backspacing."
            print("Error message appears again after clearing the text.")
        except AssertionError as e:
            print(f"Assertion failed: {str(e)}")
            failed_steps.append(f"Step 5 failed: {str(e)}")

        # Print out any failed steps at the end of the test
        if failed_steps:
            print("\nTest completed with the following failed steps:")
            for failed_step in failed_steps:
                print(failed_step)
        else:
            print("\nTest completed successfully without any failed steps.")
