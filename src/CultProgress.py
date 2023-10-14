from dataclasses import dataclass


@dataclass
class CultProgress:
    fire: int = 0
    water: int = 0
    earth: int = 0
    air: int = 0
