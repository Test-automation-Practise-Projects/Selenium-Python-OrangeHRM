from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MaintenancePage:
    def __init__(self, driver):
        self.driver = driver
        self.maintainennec_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a')
        self.username_field = (By.NAME, 'username')
        self.newPassword_field = (By.NAME, 'password')
        self.cancel_button = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/form/div[4]/button[1]')
        self.confirm_button = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/form/div[4]/button[2]')
        self.error_message = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/form/div[3]/div/span')  # Adjust the XPath if needed
        self.page_heading = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/h6')  # Adjust as necessary
        self.invalid_credentials_error = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/form/div[2]/div[1]')
        self.employeerecords_search_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[2]/button')


        self.hints_field = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/div[2]/div/div/input')  # Replace with the correct XPath for hints field
        self.hints_field_error_message = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div/div/div/span')  # Replace with the correct XPath for error

    def loadpage(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/purgeEmployee")

    def click_maintainennec_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.maintainennec_option)
        ).click()

    def click_cancel_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cancel_button)
        ).click()

    def is_username_disabled(self):
        return not self.driver.find_element(*self.username_field).is_enabled()

    def is_error_message_displayed(self):
        return len(self.driver.find_elements(*self.error_message)) > 0

    def enter_password(self, password):
        password_element = self.driver.find_element(*self.newPassword_field)
        password_element.clear()
        password_element.send_keys(password)

    def click_confirm_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_button)
        ).click()

    def is_on_purge_employee_page(self):
        current_url = self.driver.current_url
        return current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/purgeEmployee" and \
            self.driver.find_element(*self.page_heading).is_displayed()

    def get_invalid_credentials_error(self):
        return self.driver.find_element(*self.invalid_credentials_error).text

    def is_invalid_credentials_error_displayed(self):
        return self.driver.find_element(*self.invalid_credentials_error).is_displayed()

    def click_employeerecords_search_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.employeerecords_search_button)
        ).click()

    def is_hints_field_error_message_displayed(self):
        return len(self.driver.find_elements(*self.hints_field_error_message)) > 0

    def enter_text_in_hints_field(self, text):
        hints_field_element = self.driver.find_element(*self.hints_field)
        hints_field_element.clear()
        hints_field_element.send_keys(text)