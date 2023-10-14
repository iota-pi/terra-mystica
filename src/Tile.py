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

    def can_build(self, building: Building) -> None:
        if self.building >= building:
            return False
        if self.building == None and building == 1:
            return True
        if self.building == 2 and building == 4:
            return True
        if self.building + 1 == building:
            return True
