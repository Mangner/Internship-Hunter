from selenium import webdriver
from Pages.career_page import CareerPage
from Parsers.offerParser import OfferParser
from Repository.offerRepository import OfferRepository
from Services.offerService import OfferService
from database import Database

# 1. Baza danych
db = Database("sqlite:///offers.db")
db.create_tables()
session = db.get_session()

# 2. Scraping — CareerPage zwraca list[RawOffer] (DTO)
page = CareerPage(webdriver.Chrome())
page.open()
raw_offers = page.get_offers()

# 3. Service — parsuje DTO → ORM i zapisuje do bazy (przez Repository)
repository = OfferRepository(session)
parser = OfferParser()
service = OfferService(repository, parser)
saved = service.save_new_offers(raw_offers)

print(f"Zapisano {len(saved)} nowych ofert.")
session.close()
