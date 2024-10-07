from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChangePasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.dropdown_icon = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span')
        self.changePassword_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[3]/a')
        self.currentPassword_field = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/input')
        self.newPassword_field = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input')
        self.confirmPassword_field = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input')
        self.cancel_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[1]')
        self.save_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]')

    def load(self):
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/updatePassword")

    def click_dropdown_icon(self):
            # Wait until the dropdown icon is clickable and then click it
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.dropdown_icon)
            ).click()

    def click_changePassword_option(self):
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.changePassword_option)
            ).click()

    def enter_currentPassword(self, query):
            currentPassword_element = self.driver.find_element(*self.currentPassword_field)
            currentPassword_element.clear()
            currentPassword_element.send_keys(query)

    def enter_newPassword(self, query):
            newPassword_element = self.driver.find_element(*self.newPassword_field)
            newPassword_element.clear()
            newPassword_element.send_keys(query)

    def enter_confirmPassword(self, query):
            confirmPassword_element = self.driver.find_element(*self.confirmPassword_field)
            confirmPassword_element.clear()
            confirmPassword_element.send_keys(query)

    def click_cancel_button(self):
        # Wait until the dropdown icon is clickable and then click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cancel_button)
        ).click()

    def click_save_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()

    # Methods to get the values of the password fields
    def get_currentPassword_value(self):
        return self.driver.find_element(*self.currentPassword_field).get_attribute("value")

    def get_newPassword_value(self):
        return self.driver.find_element(*self.newPassword_field).get_attribute("value")

    def get_confirmPassword_value(self):
        return self.driver.find_element(*self.confirmPassword_field).get_attribute("value")