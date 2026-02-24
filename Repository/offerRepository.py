from sqlalchemy.orm import Session
from Models.offer import Offer

class OfferRepository:
    def __init__(self, session: Session):
        self._session = session

    def create_offer(self, offer: Offer):
        self._session.add(offer)
        self._session.commit()

    