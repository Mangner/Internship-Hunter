from Models.offer import Offer
from DTOs.rawOffer import RawOffer
from Parsers.offerParser import OfferParser
from Repository.offerRepository import OfferRepository


class OfferService:
    def __init__(self, repository: OfferRepository, parser: OfferParser):
        self._repository = repository
        self._parser = parser

    def save_new_offers(self, raw_offers: list[RawOffer]) -> list[Offer]:
        """Parsuje surowe oferty i zapisuje nowe (pomija duplikaty po href)."""
        parsed_offers = self._parser.parse_all(raw_offers)
        saved = []
        for offer in parsed_offers:
            if not self._repository.exists_by_href(offer.href):
                self._repository.create_offer(offer)
                saved.append(offer)
        return saved
