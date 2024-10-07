# tests/nationalities/test_select_individual_records.py
import pytest
from pages.nationalities_page import NationalitiesPage

class TestSelectIndividualRecords:
    @pytest.mark.usefixtures("successful_login")
    def test_select_individual_records(self):
        nationalities_page = NationalitiesPage(self.driver)
        nationalities_page.click_nationalities_option()

        # Select individual records
        nationalities_page.select_individual_checkbox(0)
        nationalities_page.select_individual_checkbox(1)

        # Verify the checkboxes were selected
        individual_checkboxes = nationalities_page.driver.find_elements(*nationalities_page.individual_checkboxes)
        assert individual_checkboxes[0].is_selected(), "First checkbox was not selected"
        assert individual_checkboxes[1].is_selected(), "Second checkbox was not selected"
