from dataclasses import dataclass
from util import ArithmeticEnabledDataclass


@dataclass(frozen=True, slots=True)
class Resources(ArithmeticEnabledDataclass):
    workers: int = 0
    power: int = 0
    coins: int = 0
    priests: int = 0
