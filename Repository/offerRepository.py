from sqlalchemy.orm import Session
from Models.offer import Offer


class OfferRepository:
    def __init__(self, session: Session):
        self._session = session

    def create_offer(self, offer: Offer):
        self._session.add(offer)
        self._session.commit()

    def exists_by_href(self, href: str) -> bool:
        return (
            self._session.query(Offer)
            .filter(Offer.href == href)
            .first()
            is not None
        )

    def get_all(self) -> list[Offer]:
        return self._session.query(Offer).all()