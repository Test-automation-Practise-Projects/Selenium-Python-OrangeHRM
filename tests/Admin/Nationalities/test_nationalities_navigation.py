import time

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.dashboard_page import DashboardPage
from pages.nationalities_page import NationalitiesPage
from tests.Login.test_login_valid_credentials import TestLoginValidCredentials

class TestNationalities(TestLoginValidCredentials):
    @pytest.mark.usefixtures("successful_login")

    def test_nationalities_navigation(self):

        nationalitiespage = NationalitiesPage(self.driver)

        dashboardpage=DashboardPage(self.driver)

        dashboardpage.click_admin_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/admin/viewSystemUsers"),
            "URL did not change to admin page after clicking admin option"
        )

        time.sleep(2)
        nationalitiespage.click_nationalities_option()
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/admin/nationality"),
            "URL did not change to Nationalities page after clicking nationality option"
        )


        time.sleep(2)
