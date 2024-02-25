from dataclasses import dataclass
from typing import Type, Callable

from AbstractResources import AbstractResources
from Action import Action
from Building import Building
from Resources import Resources
from Cult import Cult


@dataclass
class FavourToken:
    cult_bonus: Cult
    cult_value: int = 0
    available: int = 3
    pass_bonus_condition: Building | None = None
    pass_bonus_points: int | Callable[[int], int] = 0
    build_bonus_condition: Building | None = None
    build_bonus_points: int = 0
    income: tuple[Resources, Resources] | Resources = Resources()
    abstract_resources: AbstractResources = AbstractResources()
    action: Type[Action] | None = None
