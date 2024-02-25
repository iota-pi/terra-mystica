from dataclasses import dataclass

from CultProgress import CultProgress
from Resources import Resources


@dataclass
class TownToken:
    available_tokens: int = 2
    points: int = 0
    cult_reward: CultProgress | None = None
    resource_bonus: Resources = Resources()
