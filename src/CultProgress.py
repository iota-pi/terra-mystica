from dataclasses import dataclass
from util import ArithmeticEnabledDataclass


@dataclass(frozen=True, slots=True)
class CultProgress(ArithmeticEnabledDataclass):
    fire: int = 0
    water: int = 0
    earth: int = 0
    air: int = 0
