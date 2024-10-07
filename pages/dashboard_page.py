from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dropdown_icon = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span')
        self.logout_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a')
        self.about_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[1]/a')
        self.about_close_button = (By.XPATH, '//*[@id="app"]/div[2]/div/div/div/button')
        self.support_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[2]/a')
        self.changePassword_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[3]/a')
        self.upgrade_button = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/a/button')
        self.help_button = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/div/button')
        self.sidebar_toggle = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/button')
        self.logo = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[1]/a/div[2]/img')
        self.footer_link = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[3]/p[2]/a')

        self.admin_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
        self.pim_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')
        self.leave_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a')
        self.time_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a')
        self.recruitment_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a')
        self.myinfo_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a')
        self.performance_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a')
        self.dashboard_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a')
        self.directory_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a')
        self.maintainennec_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a')
        self.claim_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a')
        self.buzz_option = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a')
        self.searchbar = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')


    def click_dropdown_icon(self):
        # Wait until the dropdown icon is clickable and then click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.dropdown_icon)
        ).click()

    def click_logout_option(self):
        # Wait until the logout option is visible and then click it
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_option)
        ).click()

    def click_about_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.about_option)
        ).click()

    def click_about_close_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.about_close_button)
        ).click()

    def click_support_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.support_option)
        ).click()

    def click_changePassword_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.changePassword_option)
        ).click()

    def click_upgrade_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.upgrade_button)
        ).click()

    def click_help_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.help_button)
        ).click()

    def click_sidebar_toggle(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sidebar_toggle)
        ).click()

    def click_logo(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logo)
        ).click()

    def click_admin_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.admin_option)
        ).click()

    def click_pim_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.pim_option)
        ).click()

    def click_leave_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.leave_option)
        ).click()

    def click_time_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.time_option)
        ).click()

    def click_recruitment_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.recruitment_option)
        ).click()

    def click_myinfo_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.myinfo_option)
        ).click()

    def click_performance_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.performance_option)
        ).click()

    def click_dashboard_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.dashboard_option)
        ).click()

    def click_directory_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.directory_option)
        ).click()

    def click_maintainennec_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.maintainennec_option)
        ).click()

    def click_claim_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.claim_option)
        ).click()

    def click_buzz_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.buzz_option)
        ).click()


    def enter_search(self, query):
        search_element = self.driver.find_element(*self.searchbar)
        search_element.send_keys(query)

    def click_footer_link(self):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.footer_link)
        ).click()
