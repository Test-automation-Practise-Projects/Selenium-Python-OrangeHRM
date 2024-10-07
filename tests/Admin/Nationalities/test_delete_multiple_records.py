# tests/nationalities/test_delete_multiple_records.py
import pytest
from pages.nationalities_page import NationalitiesPage

class TestDeleteMultipleRecords:
    @pytest.mark.usefixtures("successful_login")
    def test_delete_multiple_records(self):
        nationalities_page = NationalitiesPage(self.driver)
        nationalities_page.click_nationalities_option()

        # Select multiple records
        nationalities_page.select_individual_checkbox(0)
        nationalities_page.select_individual_checkbox(1)

        # Click delete and verify the delete popup appears
        nationalities_page.click_delete_button()
        assert nationalities_page.is_delete_popup_displayed(), "Delete popup was not displayed"
