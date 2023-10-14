from Terrain import Terrain
from Building import Building


class Tile:
    terrain: Terrain
    building: Building | None

    def __init__(self, terrain: Terrain) -> None:
        self.terrain = terrain

    def build(self, building: Building) -> None:
        if self.can_build(building):
            self.building = building

    def can_build(self, building: Building) -> bool:
        if self.building is None and building == Building.DWELLING:
            return True
        if self.building is None:
            return False
        if self.building == Building.DWELLING and building == Building.TRADING_HOUSE:
            return True
        if self.building == Building.TRADING_HOUSE:
            if building == Building.STRONGHOLD:
                return True
            if building == Building.TEMPLE:
                return True
        if self.building == Building.TEMPLE and building == Building.SANCTUARY:
            return True
        return False
