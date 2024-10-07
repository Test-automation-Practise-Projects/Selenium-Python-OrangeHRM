# tests/nationalities/test_record_count.py
import pytest
from pages.nationalities_page import NationalitiesPage
from tests.Login.test_login_valid_credentials import TestLoginValidCredentials

class TestRecordCount(TestLoginValidCredentials):
    @pytest.mark.usefixtures("successful_login")
    def test_record_count(self):
        nationalities_page = NationalitiesPage(self.driver)
        nationalities_page.click_nationalities_option()

        record_count = nationalities_page.get_record_count()
        assert record_count == "Expected Record Count", f"Record count mismatch: {record_count}"
