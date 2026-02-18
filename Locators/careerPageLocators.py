from selenium.webdriver.common.by import By

class CareerPageLocators:
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "//*[@id=\"app\"]/div/div[4]/button")
    INDUSTRIES_BUTTON = (By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/div/div/div[1]/button[2]")
    IT_LABEL = (By.XPATH, "//label[.//span[text()='IT']]")
    IT_CODING_LABEL = (By.XPATH, "//label[.//span[text()='IT- Programowanie']]")
    OFFERS = (By.XPATH, "//li//h5//a")
    LOADER = (By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div[2]/div/div/div/div[1]/div")
    NEXT_PAGE = (By.XPATH, "//ul[contains(@class, 'pagination')]/li[last()-1]")