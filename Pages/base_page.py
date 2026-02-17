from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._wait = WebDriverWait(driver, 10)

    def find(self, locator: tuple):
        return self._wait.until(EC.visibility_of_element_located(locator))
    
    def get_text(self, locator: tuple) -> str:
        element = self.find(locator)
        return element.text
    