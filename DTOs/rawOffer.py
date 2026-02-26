from dataclasses import dataclass


@dataclass
class RawOffer:
    name: str
    add_date: str
    exp_date: str
    href: str
