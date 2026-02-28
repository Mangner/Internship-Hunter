from sqlalchemy.orm import Session
from Models.subscription import Subscription


class SubscriptionRepository:
    def __init__(self, session: Session):
        self._session = session

    def create_if_missing(self, channel_id: int, guild_id: int | None):
        exists = (
            self._session.query(Subscription)
            .filter(Subscription.channel_id == channel_id)
            .first()
        )
        if exists is None:
            self._session.add(Subscription(channel_id=channel_id, guild_id=guild_id))
            self._session.commit()

    def get_all(self) -> list[Subscription]:
        return self._session.query(Subscription).all()

    def delete_by_channel_id(self, channel_id: int) -> bool:
        subscription = (
            self._session.query(Subscription)
            .filter(Subscription.channel_id == channel_id)
            .first()
        )
        if subscription is None:
            return False
        self._session.delete(subscription)
        self._session.commit()
        return True
