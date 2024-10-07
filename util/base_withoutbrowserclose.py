from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTestBrowser:
    driver = None  # Class-level attribute to persist the browser session

    @classmethod
    def setup_class(cls):
        """Setup method to initialize the browser before all tests in the class."""
        if cls.driver is None:  # Only initialize if not already done
            chrome_options = Options()
            chrome_options.add_argument("start-maximized")  # Start Chrome maximized
            chrome_options.add_argument("--disable-notifications")  # Disable notifications
            chrome_options.add_argument("--disable-infobars")  # Disable Chrome's infobar
            chrome_options.add_argument("homepage=https://www.google.com")  # Set Google as homepage
            chrome_options.add_argument("--no-first-run")  # Disable first-run experience

            cls.driver = webdriver.Chrome(options=chrome_options)
            cls.driver.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        """Teardown method to clean up after all tests in the class."""
        # You can comment this out or control when the browser should be closed.
        # For example, only close the browser at the end of all tests.
        pass

    @classmethod
    def close_browser(cls):
        """Manually close the browser if needed."""
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
