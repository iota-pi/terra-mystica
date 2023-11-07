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
        if self.building is None:
            if new_building == Building.DWELLING:
                return True
            return False
        if self.building == Building.DWELLING:
            if new_building == Building.TRADING_HOUSE:
                return True
            return False
        if self.building == Building.TRADING_HOUSE:
            if new_building == Building.STRONGHOLD:
                return True
            if new_building == Building.TEMPLE:
                return True
            return False
        if self.building == Building.TEMPLE:
            if new_building == Building.SANCTUARY:
                return True
        return False
