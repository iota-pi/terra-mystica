from typing import Type
from Building import Building
from Faction import Faction
from Terrain import Terrain

from errors import InvalidActionError


class Tile:
    _terrain: Terrain
    _building: Building | None
    _faction: Type[Faction] | None

    def __init__(self, terrain: Terrain) -> None:
        self._terrain = terrain
        self._building = None
        self._faction = None

    @property
    def terrain(self) -> Terrain:
        return self._terrain

    @property
    def building(self) -> Building | None:
        return self._building

    def terraform(self, terrain_goal: Terrain) -> None:
        if self._building or self._faction:
            raise InvalidActionError("Cannot terraform a tile with a building on it")
        self._terrain = terrain_goal

    def build(self, new_building: Building, faction: Type[Faction]) -> None:
        if not self.can_build(new_building=new_building, faction=faction):
            raise InvalidActionError()
        self._building = new_building
        self._faction = faction

    def can_build(self, new_building: Building, faction: Type[Faction]) -> bool:
        if self._faction is not None and self._faction != faction:
            return False
        if self._terrain != faction.terrain:
            return False
        if self._building is None:
            return new_building == Building.DWELLING
        if self._building == Building.DWELLING:
            return new_building == Building.TRADING_HOUSE
        if self._building == Building.TRADING_HOUSE:
            return new_building in (Building.STRONGHOLD, Building.TEMPLE)
        if self._building == Building.TEMPLE:
            return new_building == Building.SANCTUARY
        return False
