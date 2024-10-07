# tests/nationalities/test_select_all_records.py
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.nationalities_page import NationalitiesPage
from tests.Login.test_login_valid_credentials import TestLoginValidCredentials

class TestSelectAllRecords(TestLoginValidCredentials):
    @pytest.mark.usefixtures("successful_login")
    def test_select_all_records(self):
        nationalities_page = NationalitiesPage(self.driver)
        nationalities_page.click_admin_option()
        nationalities_page.click_nationalities_option()

        # Select all records using the checkbox
        nationalities_page.select_all_records()

        # Verify that all individual checkboxes are selected
        individual_checkboxes = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(nationalities_page.individual_checkboxes)
        )
        for checkbox in individual_checkboxes:
            assert checkbox.is_selected(), "Some checkboxes were not selected when 'Select All' was clicked"
