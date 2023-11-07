from Terrain import Terrain
from Building import Building


class Tile:
    terrain: Terrain
    building: Building | None

    def __init__(self, terrain: Terrain) -> None:
        self.terrain = terrain
        self.building = None

    def build(self, new_building: Building) -> None:
        if self.can_build(new_building):
            self.building = new_building

    def can_build(self, new_building: Building) -> bool:
        if self.building is None and new_building == Building.DWELLING:
            return True
        if self.building is None:
            return False
        if (
            self.building == Building.DWELLING
            and new_building == Building.TRADING_HOUSE
        ):
            return True
        if self.building == Building.TRADING_HOUSE:
            if new_building == Building.STRONGHOLD:
                return True
            if new_building == Building.TEMPLE:
                return True
        if self.building == Building.TEMPLE and new_building == Building.SANCTUARY:
            return True
        return False
