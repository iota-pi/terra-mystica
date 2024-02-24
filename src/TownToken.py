from dataclasses import dataclass

from Cult import Cult
from Resources import Resources


@dataclass
class TownToken:
    available_tokens: int = 2
    points: int = 0
    cult_reward: tuple[Cult,Cult,Cult,Cult] | None = None
    cult_reward_value: int = 0
    resource_bonus: Resources = Resources()
