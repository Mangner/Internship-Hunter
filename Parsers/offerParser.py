from datetime import date
from Models.offer import Offer
from DTOs.rawOffer import RawOffer


class OfferParser:

    def parse_all(self, offers: list[RawOffer]) -> list[Offer]:
        return [self._to_model(offer) for offer in offers]

    def _to_model(self, raw: RawOffer) -> Offer:
        return Offer(
            offer_name=raw.name,
            add_date=date.fromisoformat(raw.add_date),
            exp_date=date.fromisoformat(raw.exp_date),
            href=raw.href,
        )
        