from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

        self.forget_password_link = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
        self.linkedin_icon = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[1]')
        self.facebook_icon = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[2]')
        self.twitter_icon = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[3]')
        self.youtube_icon = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[4]')
        self.web_link = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a')

        # Error message elements
        self.username_required_error = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span')
        self.password_required_error = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span')
        self.invalid_credentials_error = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]')

    def load(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/auth/login")

    def enter_username(self, query):
        username_element = self.driver.find_element(*self.username_field)
        username_element.send_keys(query)

    def enter_password(self, pquery):
        password_element = self.driver.find_element(*self.password_field)
        password_element.send_keys(pquery)

    def click_login_button(self):
        login_button_element = self.driver.find_element(*self.login_button)
        login_button_element.click()

    def click_forgot_password(self):
        forgot_password_element = self.driver.find_element(*self.forget_password_link)
        forgot_password_element.click()

    def get_username_required_error(self):
        return self.driver.find_element(*self.username_required_error).text

    def get_password_required_error(self):
        return self.driver.find_element(*self.password_required_error).text

    def get_invalid_credentials_error(self):
        return self.driver.find_element(*self.invalid_credentials_error).text

    def is_username_required_error_displayed(self):
        return self.driver.find_element(*self.username_required_error).is_displayed()

    def is_password_required_error_displayed(self):
        return self.driver.find_element(*self.password_required_error).is_displayed()

    def is_invalid_credentials_error_displayed(self):
        return self.driver.find_element(*self.invalid_credentials_error).is_displayed()

    def click_linkedin_icon(self):
        linkedin_element = self.driver.find_element(*self.linkedin_icon)
        linkedin_element.click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def click_facebook_icon(self):
        facebook_element = self.driver.find_element(*self.facebook_icon)
        facebook_element.click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def click_twitter_icon(self):
        twitter_element = self.driver.find_element(*self.twitter_icon)
        twitter_element.click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def click_youtube_icon(self):
        youtube_element = self.driver.find_element(*self.youtube_icon)
        youtube_element.click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def click_web_link(self):
        web_link_element = self.driver.find_element(*self.web_link)
        web_link_element.click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])


    def is_username_error_message_not_visible(self):
        try:
            # Check if the error message is not displayed
            return not self.driver.find_element(*self.username_required_error).is_displayed()
        except:
            # If the element isn't found at all, it definitely isn't visible!
            return True

    def is_password_error_message_not_visible(self):
        try:
            # Check if the error message is not displayed
            return not self.driver.find_element(*self.password_required_error).is_displayed()
        except:
            # If the element isn't found at all, it definitely isn't visible!
            return True
