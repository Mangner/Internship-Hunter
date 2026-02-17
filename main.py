from CareerConfig import careerPageConfig
from Pages.career_page import CareerPage
from selenium import webdriver

page = CareerPage(webdriver.Chrome(), careerPageConfig)
page.get_offers()