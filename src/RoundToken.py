from dataclasses import dataclass

from AbstractResources import AbstractResources
from Building import Building
from CultProgress import CultProgress
from Resources import Resources


@dataclass
class RoundToken:
    build_bonus_condition: Building | tuple[Building, Building] | AbstractResources
    build_bonus_points: int
    cult_condition: CultProgress
    cult_reward: Resources | AbstractResources
