from dataclasses import dataclass


@dataclass
class AbstractResources:
    towns: int = 0
    spades: int = 0
    shipping_bonus: int = 0
