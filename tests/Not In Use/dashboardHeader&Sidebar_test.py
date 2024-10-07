import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from tests.Login.test_login_valid_credentials import TestLoginValidCredentials
from tests.successfulLogin_test import TestSuccesfulLogin

class TestDashboardActions(TestLoginValidCredentials):
    def test_dashboard_actions(self):
        self.keep_browser_open = True
        self.loginpage = LoginPage(self.driver)

        #Successful login
        self.test_successful_login()

        dashboard_page = DashboardPage(self.driver)

        #Header actions
        dashboard_page.click_dropdown_icon()
        dashboard_page.click_logout_option()
        self.test_successful_login()

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
            "URL did not change to Change password page after clicking change psw option"
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

        dashboard_page.click_sidebar_toggle()
        time.sleep(2)
        dashboard_page.click_sidebar_toggle()


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


        #Sidebar actions

        dashboard_page.click_admin_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"),
            "URL did not change to admin page after clicking admin option"
        )

        time.sleep(2)
        dashboard_page.click_dashboard_option()

        dashboard_page.click_pim_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"),
            "URL did not change to PIM page after clicking PIM option"
        )

        time.sleep(2)
        dashboard_page.click_dashboard_option()

        dashboard_page.click_leave_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList"),
            "URL did not change to Leave page after clicking Leave option"
        )

        time.sleep(2)
        dashboard_page.click_time_option()

        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet"),
            "URL did not change to Time page after clicking time option"
        )

        time.sleep(2)
        dashboard_page.click_dashboard_option()

        dashboard_page.click_recruitment_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates"),
            "URL did not change to Recruitment page after clicking recruitment option"
        )

        time.sleep(2)
        dashboard_page.click_dashboard_option()

        dashboard_page.click_myinfo_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"),
            "URL did not change to My Info page after clicking myinfo option"
        )

        time.sleep(2)
        dashboard_page.click_dashboard_option()

        dashboard_page.click_performance_option()
        WebDriverWait(self.driver, 20).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/performance/searchEvaluatePerformanceReview"),
            "URL did not change to Performance page after clicking Performance option"
        )

        time.sleep(2)
        dashboard_page.click_dashboard_option()

        dashboard_page.click_dashboard_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"),
            "URL did not change to dashboard page after clicking dashboard option"
        )

        dashboard_page.click_directory_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory"),
            "URL did not change to directory page after clicking directory option"
        )

        time.sleep(2)
        dashboard_page.click_dashboard_option()


        dashboard_page.click_maintainennec_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/purgeEmployee"),
            "URL did not change to Maintenance page after clicking maintenance option"
        )

        time.sleep(2)
        self.driver.back()


        dashboard_page.click_claim_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/claim/viewAssignClaim"),
            "URL did not change to Claim page after clicking claim option"
        )

        time.sleep(2)
        dashboard_page.click_dashboard_option()

        dashboard_page.click_buzz_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz"),
            "URL did not change to Buzz page after clicking buzz option"
        )

        time.sleep(2)
        dashboard_page.click_dashboard_option()


        dashboard_page.click_footer_link()
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        original_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://www.orangehrm.com/"),
            "URL did not change to the expected site page"
        )
        self.driver.close()
        self.driver.switch_to.window(original_window)


        dashboard_page.enter_search("Cla")
        dashboard_page.enter_search(Keys.BACKSPACE)

        dashboard_page.click_logo()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://www.orangehrm.com/"),
            "URL did not change to home page of OrangeHRM"
        )
        self.driver.back()

        time.sleep(5)








