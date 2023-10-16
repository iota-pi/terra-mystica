from dataclasses import dataclass

from AbstractResources import AbstractResources
from Building import Building
from Resources import Resources


@dataclass
class PassToken:
    bonus_condition: Building | tuple[Building, Building] | None = None
    bonus_points: int = 0
    income: Resources = Resources()
    abstract_resources: AbstractResources = AbstractResources()
    # TODO add actions
    # action: PlayerAction
