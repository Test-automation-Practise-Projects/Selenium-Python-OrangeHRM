import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from tests.Login.test_login_valid_credentials import TestLoginValidCredentials

class TestDashboardSidebarActions(TestLoginValidCredentials):
    @pytest.mark.usefixtures("successful_login")

    def test_sidebar_actions(self):

        dashboard_page = DashboardPage(self.driver)

        # Sidebar actions
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
            "URL did not change to My Info page after clicking my info option"
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

        dashboard_page.click_sidebar_toggle()
        time.sleep(2)
        dashboard_page.click_sidebar_toggle()


        dashboard_page.enter_search("Cla")
        dashboard_page.enter_search(Keys.BACKSPACE)