from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ForgetPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.cancel_button = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[1]')
        self.reset_button = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')
        self.error_message = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[1]/div/span')  # Adjust based on actual locator

    def load(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # def enter_username(self, query):
    #     username_element = self.driver.find_element(*self.username_field)
    #     username_element.send_keys(query)

    def enter_username(self, query):
        username_element = self.driver.find_element(*self.username_field)
        username_element.clear()  # Clear any existing text
        username_element.send_keys(query)

    def click_cancel_button(self):
        cancel_button_element = self.driver.find_element(*self.cancel_button)
        cancel_button_element.click()

    def click_reset_button(self):
        reset_button_element = self.driver.find_element(*self.reset_button)
        reset_button_element.click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def is_error_message_visible(self):
        return self.driver.find_element(*self.error_message).is_displayed()

    def is_error_message_not_visible(self):
        try:
            # Check if the error message is not displayed
            return not self.driver.find_element(*self.error_message).is_displayed()
        except:
            # If the element isn't found at all, it definitely isn't visible!
            return True
