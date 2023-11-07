from Building import Building
from Faction import Faction
from Terrain import Terrain

from errors import InvalidActionError


class Tile:
    _terrain: Terrain
    _building: Building | None
    _faction: Faction | None

    def __init__(self, terrain: Terrain) -> None:
        self._terrain = terrain
        self._building = None
        self._faction = None

    @property
    def terrain(self) -> Terrain:
        return self._terrain

    def terraform(self, terrain_goal: Terrain) -> None:
        if self._building or self._faction:
            raise InvalidActionError("Cannot terraform a tile with a building on it")
        self._terrain = terrain_goal

    def build(self, new_building: Building, faction: Faction) -> None:
        if not self.can_build(new_building=new_building, faction=faction):
            raise InvalidActionError()
        self._building = new_building
        self._faction = faction

    def can_build(self, new_building: Building, faction: Faction) -> bool:
        if self._faction is not None and self._faction != faction:
            raise InvalidActionError(
                "Cannot build on top of another faction's building"
            )
        if self._terrain != faction.terrain:
            raise InvalidActionError(
                f"Faction {faction.name} cannot build on {self._terrain.name}"
            )
        if self._building is None:
            if new_building == Building.DWELLING:
                return True
            return False
        if self._building == Building.DWELLING:
            if new_building == Building.TRADING_HOUSE:
                return True
            return False
        if self._building == Building.TRADING_HOUSE:
            if new_building == Building.STRONGHOLD:
                return True
            if new_building == Building.TEMPLE:
                return True
            return False
        if self._building == Building.TEMPLE:
            if new_building == Building.SANCTUARY:
                return True
        return False
