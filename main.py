from Pages.career_page import CareerPage
from selenium import webdriver


page = CareerPage(webdriver.Chrome())
page.open()
page.get_offers()