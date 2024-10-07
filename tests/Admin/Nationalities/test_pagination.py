# tests/nationalities/test_pagination.py
import pytest
from pages.nationalities_page import NationalitiesPage
from tests.Login.test_login_valid_credentials import TestLoginValidCredentials

class TestPagination(TestLoginValidCredentials):
    @pytest.mark.usefixtures("successful_login")
    def test_pagination(self):
        nationalities_page = NationalitiesPage(self.driver)
        nationalities_page.click_admin_option()

        nationalities_page.click_nationalities_option()

        # Navigate to page 2 and check data
        nationalities_page.navigate_pagination(2)
        page_2_data = nationalities_page.get_table_data()

        # Navigate back to page 1 and check data
        nationalities_page.navigate_pagination(1)
        page_1_data = nationalities_page.get_table_data()

        # Verify that data between pages is different
        assert page_1_data != page_2_data, "Data between pages did not change"
