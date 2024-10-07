import time

from selenium.webdriver.common.by import By

from pages.changePassword_page import ChangePasswordPage
from pages.login_page import LoginPage
from tests.successfulLogin_test import TestSuccesfulLogin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestChangePassword(TestSuccesfulLogin):

    def test_change_password(self):
        # Step 1: Login
        self.loginpage = LoginPage(self.driver)
        self.test_successful_login()

        # Step 2: Navigate to Change Password Page
        changepswpage = ChangePasswordPage(self.driver)

        # Open the dropdown and select 'Change Password'
        changepswpage.click_dropdown_icon()
        changepswpage.click_changePassword_option()
        time.sleep(2)

        changepswpage.click_cancel_button()
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index", \
        f"Expected URL: https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index, but got {self.driver.current_url}"

        changepswpage.click_dropdown_icon()
        changepswpage.click_changePassword_option()

        # Step 3: Enter current, new, and confirm password
        changepswpage.enter_currentPassword("admin123")
        changepswpage.enter_newPassword("newPassword123")
        changepswpage.enter_confirmPassword("newPassword123")
        time.sleep(2)

        changepswpage.click_save_button()
        time.sleep(10)
        #TODO - Task 1: Verify that success notification is displayed

        # success_notification = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, '//*[@id="oxd-toaster_1"]'))
        # )
        # assert success_notification.is_displayed(), "Success notification not displayed."

        # Step 5: Verify that fields are cleared
        assert changepswpage.get_currentPassword_value() == "", "Current password field is not cleared."
        assert changepswpage.get_newPassword_value() == "", "New password field is not cleared."
        assert changepswpage.get_confirmPassword_value() == "", "Confirm password field is not cleared."

        #TODO - Task 2: Do error validations
