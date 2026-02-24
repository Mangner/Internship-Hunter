from Models.offer import Offer


class OfferParser:

    def parse_all(self, offers: list[list[str, str, str, str]]) -> list[Offer]:
        parsed_offers = []
        for offer in offers:
            new_offer = Offer(offer_name=offer[0], add_date=offer[1], exp_date=offer[2], href=offer[3])
            parsed_offers.append(new_offer)
        return parsed_offers
        