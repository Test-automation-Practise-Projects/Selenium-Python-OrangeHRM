from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTest:
    def setup_method(self, method):
        """Setup method to initialize the browser before each test."""
        # Set Chrome options to load Google as the homepage
        chrome_options = Options()
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("homepage=https://www.google.com")
        chrome_options.add_argument("--no-first-run")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):
        """Teardown method to clean up after each test."""
        self.driver.quit()
        pass
