from dataclasses import dataclass


@dataclass
class Resources:
    workers: int = 0
    power: int = 0
    coins: int = 0
    priests: int = 0
