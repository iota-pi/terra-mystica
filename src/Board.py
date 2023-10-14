from Terrain import Terrain
from Tile import Tile


BOARD_WIDTH = 20
BOARD_HEIGHT = 10


class Board:
    def __init__(self) -> None:
        self.data = [
            [Tile(terrain=Terrain.MOUNTAIN) for _ in range(BOARD_WIDTH)]
            for _ in range(BOARD_HEIGHT)
        ]
