from dataclasses import dataclass
from Power import Power
from util import ArithmeticEnabledDataclass


@dataclass(frozen=True, slots=True, init=False)
class Resources(ArithmeticEnabledDataclass):
    workers: int = 0
    power: Power = Power()
    coins: int = 0
    priests: int = 0

    def __init__(
        self,
        workers: int = 0,
        power: int | Power = 0,
        coins: int = 0,
        priests: int = 0,
    ):
        # Work around limitations of frozen dataclasses
        object.__setattr__(self, 'workers', workers)
        object.__setattr__(self, 'power', Power(power))
        object.__setattr__(self, 'coins', coins)
        object.__setattr__(self, 'priests', priests)
