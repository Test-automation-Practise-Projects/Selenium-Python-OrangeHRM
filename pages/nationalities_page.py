from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NationalitiesPage:
    def __init__(self, driver):
        self.driver = driver
        self.admin_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
        self.nationalities_tab = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]')
        self.add_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]')
        self.delete_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        self.individual_checkboxes = (By.XPATH, '//input[@type="checkbox" and @class="checkbox-selector"]')
        self.overall_checkbox = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div[1]/div/label/span')
        self.record_count_label = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/button')
        self.delete_selected_button = (By.XPATH, '//button[@class="btn-delete-selected"]')
        self.pagination_buttons = (By.XPATH, '//*[@class="pagination-button"]')


    def click_admin_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.admin_option)
        ).click()

    def click_nationalities_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.nationalities_tab)
        ).click()

    def select_all_records(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.overall_checkbox)
        ).click()

    def select_individual_checkbox(self, index):
        individual_checkboxes = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.individual_checkboxes)
        )
        individual_checkboxes[index].click()

    def click_delete_selected(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delete_selected_button)
        ).click()

    def is_delete_popup_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'deleteModal'))
        ).is_displayed()

    def navigate_pagination(self, page_number):
        pagination_buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.pagination_buttons)
        )
        pagination_buttons[page_number - 1].click()

    def get_table_data(self):
        rows = self.driver.find_elements(By.XPATH, '//table/tbody/tr')
        table_data = []
        for row in rows:
            columns = row.find_elements(By.XPATH, './td')
            row_data = [col.text for col in columns]
            table_data.append(row_data)
        return table_data
