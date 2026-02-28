from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import BigInteger
from Models.base import Base


class Subscription(Base):
    __tablename__ = "ChannelSubscriptions"

    subscription_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    guild_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    channel_id: Mapped[int] = mapped_column(BigInteger, unique=True)
