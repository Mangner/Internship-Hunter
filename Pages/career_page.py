from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Pages.base_page import BasePage
from Locators.careerPageLocators import CareerPageLocators
from DTOs.rawOffer import RawOffer

class CareerPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.URL = "https://kariery.pk.edu.pl/#/offers"
        self._preprocessed_offers = []

    def open(self):
        self._driver.maximize_window()
        self._driver.get(self.URL)
        accept_cookies_button = self._wait.until(EC.visibility_of_element_located(CareerPageLocators.ACCEPT_COOKIES_BUTTON))
        accept_cookies_button.click()
    
    def get_offers(self) -> list[RawOffer]:
        self._preprocessed_offers = []
        self._apply_filters()
        while True:
            self._scrape_current_page_offers()
            next_page = self._wait.until(EC.presence_of_element_located(CareerPageLocators.NEXT_PAGE))
            if next_page.get_attribute("class") == "page-item disabled":
                break
            self._change_to_next_page(next_page)

        final_offers = []
        for offer in self._preprocessed_offers:
            final_offers.append(self._get_offer_details(offer))
        return final_offers

    def get_new_offers(self, exists_by_href) -> list[RawOffer]:
        self._preprocessed_offers = []
        self._apply_filters()

        while True:
            scraped_offers = self._find_all_elements(CareerPageLocators.OFFERS)
            for offer in scraped_offers:
                href = offer.get_property("href")
                if exists_by_href(href):
                    continue
                self._preprocessed_offers.append(href)

            next_page = self._wait.until(EC.presence_of_element_located(CareerPageLocators.NEXT_PAGE))
            if next_page.get_attribute("class") == "page-item disabled":
                break
            self._change_to_next_page(next_page)

        final_offers = []
        for offer in self._preprocessed_offers:
            final_offers.append(self._get_offer_details(offer))
        return final_offers

    def _apply_filters(self):
        industries_button = self._find_element(CareerPageLocators.INDUSTRIES_BUTTON)   
        industries_button.click() 
        it_label = self._wait.until(EC.visibility_of_element_located(CareerPageLocators.IT_LABEL))     
        it_label.click()
        self._wait_for_reload()
        it_coding_label = self._wait.until(EC.visibility_of_element_located(CareerPageLocators.IT_CODING_LABEL))
        it_coding_label.click()
        self._wait_for_reload()

    def _wait_for_reload(self):
        try: 
            loader = self._wait.until(EC.visibility_of_element_located(CareerPageLocators.LOADER)) 
            self._wait.until(EC.staleness_of(loader))       
        except TimeoutException:
            pass

    def _scrape_current_page_offers(self):
        scraped_offers = self._find_all_elements(CareerPageLocators.OFFERS)
        for offer in scraped_offers:
            self._preprocessed_offers.append(offer.get_property("href"))

    def _change_to_next_page(self, element):
        next_page_a = element.find_element(By.XPATH, "./a")
        self._driver.execute_script("arguments[0].click();", next_page_a)
        self._wait_for_reload()
        
    def _get_offer_details(self, url):
        self._driver.get(url)
        offer_name = self._wait.until(
            lambda d: d.find_element(*CareerPageLocators.OFFER_NAME).text.strip() or False
        )
        add_date = self._wait.until(
            EC.visibility_of_element_located(CareerPageLocators.ADD_DATE)
        ).text
        expiration_date = self._wait.until(
            EC.visibility_of_element_located(CareerPageLocators.EXPIRATION_DATE)
        ).text
        self._driver.get("https://kariery.pk.edu.pl/#/offers")
        self._wait_for_reload()
        return RawOffer(name=offer_name, add_date=add_date, exp_date=expiration_date, href=url)