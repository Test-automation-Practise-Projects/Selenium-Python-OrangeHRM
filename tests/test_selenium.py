import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BaseTest:
    def setup_method(self, method):
        """Setup method to initialize the browser before each test."""
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

class TestGoogleSearch(BaseTest):
    def test_title(self):
        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title

    def test_search(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("pytest")
        search_box.send_keys(Keys.RETURN)
        assert "pytest" in self.driver.title

    def test_search_results(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("selenium")
        search_box.send_keys(Keys.RETURN)
        results = self.driver.find_elements(By.XPATH, '//h3')
        assert len(results) > 0  # Check that there are search results
