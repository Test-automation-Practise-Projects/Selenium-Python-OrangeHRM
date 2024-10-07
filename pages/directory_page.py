from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DirectoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.directory_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a')
        self.reset_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]')
        self.search_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
        self.employee_name_field = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        self.jobtitle_field = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]')
        self.location_field = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div')
        self.jobtitle_dropdown_icon = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i')
        self.location_dropdown_icon = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i')
        self.collapse_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/button')


    def click_directory_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.directory_option)
        ).click()

    def click_reset_button(self):
        self.driver.find_element(*self.reset_button).click()

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    def enter_employee_name(self, query):
        self.driver.find_element(*self.employee_name_field).send_keys(query)

    def click_jobtitle_field(self):
        self.driver.find_element(*self.jobtitle_field).click()

    def click_location_field(self):
        self.driver.find_element(*self.location_field).click()

    def click_jobtitle_dropdown_icon(self):
        self.driver.find_element(*self.jobtitle_dropdown_icon).click()

    def click_location_dropdown_icon(self):
        self.driver.find_element(*self.location_dropdown_icon).click()

    def select_job_title(self):
        """Method to select the 4th job title from the dropdown."""
        self.click_jobtitle_field()
        self.click_jobtitle_dropdown_icon()

        # Wait for the dropdown and select the 4th option
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]]'))
        )
        fourth_option = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span]')
        fourth_option.click()

    def select_location(self):
        """Method to select the 4th location from the dropdown."""
        self.click_location_field()
        self.click_location_dropdown_icon()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//ul[contains(@class, "dropdown-menu")]'))
        )
        fourth_option = self.driver.find_element(By.XPATH, '(//ul[contains(@class, "dropdown-menu")]/li)[4]')
        fourth_option.click()

    def click_collapse_button(self):
        self.driver.find_element(*self.collapse_button).click()
