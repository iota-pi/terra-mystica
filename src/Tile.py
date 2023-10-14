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
        # TODO
        pass
