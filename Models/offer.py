from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import DATE
from Models.base import Base


class Offer(Base):
    __tablename__ = "Offers"

    offer_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    offer_name: Mapped[str] = mapped_column(String)
    add_date: Mapped[str] = mapped_column(DATE)
    exp_date: Mapped[str] = mapped_column(DATE)
    href: Mapped[str] = mapped_column(String)

    def __repr__(self) -> str:
        return f'''Oferta:
        offer_id: {self.offer_id!r}
        offer_name: {self.offer_name!r}
        add_date: {self.add_date!r}
        exp_date: {self.exp_date!r}
        href: {self.href!r}
        '''
    