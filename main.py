from Pages.career_page import CareerPage
from selenium import webdriver
from Parsers.offerParser import OfferParser
from Repository.offerRepository import OfferRepository

page = CareerPage(webdriver.Chrome())
page.open()
offers = page.get_offers()

parser = OfferParser()
parsed_offers = parser.parse_all(offers)

repository = OfferRepository()
