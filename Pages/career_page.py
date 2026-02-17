from Pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException


class CareerPage(BasePage):
    def __init__(self, driver: webdriver, config: dict):
        super().__init__(driver)
        self._config = config

    def get_offers(self):
        self._driver.maximize_window()
        self._driver.get(self._config["URL"])

        all_offers = []

        accept_cookies_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self._config["ACCEPT_COOKIES_BUTTON_XPATH"]))
        )
        accept_cookies_button.click()

        industries_button = self.find((By.XPATH, self._config["INDUSTRIES_BUTTON_XPATH"]))
        industries_button.click()

        it_label = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self._config["IT_LABEL_XPATH"]))
        )
        it_label.click()

        it_coding_label = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self._config["IT_CODING_LABEL_XPATH"]))
        )
        it_coding_label.click()


        try:
            loader = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self._config["LOADER_XPATH"]))
            )
        except TimeoutException:
            pass

        self.wait.until(EC.staleness_of(loader))
        all_offers = self._driver.find_elements(By.XPATH, self._config["OFFERS_XPATH"])

        for offer in all_offers:
            print(f"Offer: {offer.text}. Link: {offer.get_property("href")}")
