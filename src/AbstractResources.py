from dataclasses import dataclass

from util import ArithmeticEnabledDataclass


@dataclass(frozen=True, slots=True)
class AbstractResources(ArithmeticEnabledDataclass):
    towns: int = 0
    spades_credit: int = 0
    bridge_credit: int = 0
    dwelling_credit: int = 0
    terraform_credit: int = 0
    shipping_bonus: int = 0
    town_discount: bool = False
