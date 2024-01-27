import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_weather_chrome(self):
        driver_chrome = self.driver
        driver_chrome.get('http://www.google.com')
        wait = WebDriverWait(driver_chrome, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)  # simulate test

        search = driver_chrome.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver_chrome.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver_chrome.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver_chrome.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver_chrome.find_element(By.ID, "wob_temp").click()

    def test_search_weather_chrome_1120x850(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1120, 850)
        driver_chrome.get('http://www.google.com')
        wait = WebDriverWait(driver_chrome, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)

        search = driver_chrome.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver_chrome.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver_chrome.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver_chrome.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver_chrome.find_element(By.ID, "wob_temp").click()

    def test_search_weather_chrome_1120x950(self):
        driver_chrome = self.driver
        driver_chrome.set_window_size(1120, 950)
        driver_chrome.get('http://www.google.com')
        wait = WebDriverWait(driver_chrome, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)

        search = driver_chrome.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver_chrome.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver_chrome.title
        print("Page title in Chrome is:", driver_chrome.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver_chrome.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver_chrome.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver_chrome.find_element(By.ID, "wob_temp").click()

    # Anything declared in tearDown will be executed for all test cases
    # Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_weather_firefox(self):
        driver_firefox = self.driver
        driver_firefox.get('http://www.google.com')
        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)

        search = driver_firefox.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver_firefox.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver_firefox.title
        print("Page title in Chrome 1120x850 is:", driver_firefox.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver_firefox.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver_firefox.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver_firefox.find_element(By.ID, "wob_temp").click()

    def test_search_weather_firefox_1120x850(self):
        driver_firefox = self.driver
        driver_firefox.set_window_size(1120, 850)
        driver_firefox.get('http://www.google.com')
        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)

        search = driver_firefox.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver_firefox.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver_firefox.title
        print("Page title in Chrome 1120x850 is:", driver_firefox.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver_firefox.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver_firefox.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver_firefox.find_element(By.ID, "wob_temp").click()

    def test_search_weather_firefox_1120x950(self):
        driver_firefox = self.driver
        driver_firefox.set_window_size(1120, 950)
        driver_firefox.get('http://www.google.com')
        wait = WebDriverWait(driver_firefox, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='q']")))
        time.sleep(1)

        search = driver_firefox.find_element(By.NAME, "q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        time.sleep(1)

        # Check if the search returns any result
        assert "No results found." not in driver_firefox.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver_firefox.title
        print("Page title in Chrome 1120x850 is:", driver_firefox.title)

        # Check Weather frame functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver_firefox.find_element(By.ID, "wob_rain").click()
        time.sleep(1)
        driver_firefox.find_element(By.ID, "wob_wind").click()
        time.sleep(1.5)
        driver_firefox.find_element(By.ID, "wob_temp").click()

    # Anything declared in tearDown will be executed for all test cases
    # Closing browser. You need to use "tearDown" method only one time for every Class
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()