from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver: webdriver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 2)

    def _find_element(self, locator: tuple):
        return self._driver.find_element(*locator)
    
    def _find_all_elements(self, locator: tuple):
        return self._driver.find_elements(*locator)