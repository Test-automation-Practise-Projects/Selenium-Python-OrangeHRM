import driver
import pytest
from pages.directory_page import DirectoryPage
from tests.Login.test_login_valid_credentials import TestLoginValidCredentials


@pytest.mark.usefixtures("successful_login")
class TestResetFields((TestLoginValidCredentials)):

    def test_reset_fields(self):
        directory_page = DirectoryPage(driver)

        # Navigate to the directory page
        directory_page.click_directory_option()

        # Enter some data in the fields
        directory_page.enter_employee_name("John Doe")
        directory_page.select_job_title()
        directory_page.select_location()

        # Click the reset button
        directory_page.click_reset_button()
        directory_page.select_job_title()
        # Validate that fields are cleared after reset
        # employee_name_value = driver.find_element(*directory_page.employee_name_field).get_attribute("value")
        # assert employee_name_value == "", "Employee name field is not cleared"

        # Additional checks for job title and location fields depending on how the reset works
        # job_title_value = driver.find_element(*directory_page.jobtitle_field).text
        # location_value = driver.find_element(*directory_page.location_field).text
        # assert job_title_value == "", "Job title field is not cleared"
        # assert location_value == "", "Location field is not cleared"
