from dataclasses import dataclass
from typing import Type

from AbstractResources import AbstractResources
from Action import Action
from Building import Building
from Resources import Resources


@dataclass
class PassToken:
    pass_bonus_condition: Building | tuple[Building, Building] | None = None
    pass_bonus_points: int = 0
    income: Resources = Resources()
    abstract_resources: AbstractResources = AbstractResources()
    action: Type[Action] | None = None
