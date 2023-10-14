import random
import math as maths
# from Terrain import Terrain
from Tile import Tile as T


BOARD_WIDTH = 13
BOARD_HEIGHT = 9


class Board:
    def __init__(self, style = "default", size = 5) -> None:
        extention = 0 # provision for games with more players
        if size > 5:
            extention = maths.floor((maths.ceil((size-5)/3)*3)*2.8)
        if style == "random":
            self.data = [
                [T(terrain=random.randint(1,9)) for _ in range(BOARD_WIDTH+extention)]
                for _ in range(BOARD_HEIGHT)
            ]
            self.data[2][-1] = 0
            self.data[4][-1] = 0
            self.data[6][-1] = 0
            self.data[8][-1] = 0
        elif style == "default":
            if size <= 5:
                self.data = [
                    [T(5),T(1),T(2),T(3),T(6),T(7),T(5),T(4),T(7),T(2),T(3),T(7),T(4)],
                    [T(6),T(8),T(8),T(5),T(4),T(8),T(8),T(6),T(4),T(8),T(8),T(6),T(0)],
                    [T(8),T(8),T(4),T(8),T(1),T(8),T(2),T(8),T(2),T(8),T(1),T(8),T(8)],
                    [T(2),T(3),T(6),T(8),T(8),T(7),T(3),T(8),T(7),T(8),T(7),T(5),T(0)],
                    [T(4),T(5),T(7),T(3),T(4),T(5),T(1),T(6),T(8),T(8),T(2),T(4),T(3)],
                    [T(1),T(2),T(8),T(8),T(6),T(2),T(8),T(8),T(8),T(5),T(1),T(5),T(0)],
                    [T(8),T(8),T(8),T(1),T(8),T(7),T(8),T(2),T(8),T(6),T(4),T(3),T(6)],
                    [T(6),T(3),T(5),T(8),T(8),T(8),T(3),T(4),T(8),T(1),T(5),T(1),T(0)],
                    [T(7),T(4),T(1),T(3),T(7),T(2),T(6),T(5),T(1),T(8),T(3),T(2),T(7)]
                ]
            elif size <= 8:
                self.data = [
                    [T(5),T(1),T(2),T(3),T(6),T(7),T(5),T(4),T(7),T(2),T(3),T(7),T(4),T(2),T(8),T(4),T(2),T(1),T(3),T(6),T(5)],
                    [T(6),T(8),T(8),T(5),T(4),T(8),T(8),T(6),T(4),T(8),T(8),T(6),T(1),T(5),T(8),T(3),T(5),T(7),T(2),T(3),T(0)],
                    [T(8),T(8),T(4),T(8),T(1),T(8),T(2),T(8),T(2),T(8),T(1),T(8),T(8),T(8),T(8),T(8),T(8),T(6),T(4),T(5),T(4)],
                    [T(2),T(3),T(6),T(8),T(8),T(7),T(3),T(8),T(7),T(8),T(7),T(5),T(6),T(4),T(8),T(4),T(8),T(1),T(6),T(1),T(0)],
                    [T(4),T(5),T(7),T(3),T(4),T(5),T(1),T(6),T(8),T(8),T(2),T(4),T(3),T(1),T(8),T(1),T(5),T(8),T(3),T(7),T(4)],
                    [T(1),T(2),T(8),T(8),T(6),T(2),T(8),T(8),T(8),T(5),T(1),T(5),T(2),T(7),T(8),T(3),T(7),T(8),T(2),T(8),T(0)],
                    [T(8),T(8),T(8),T(1),T(8),T(7),T(8),T(2),T(8),T(6),T(4),T(3),T(6),T(3),T(5),T(8),T(8),T(8),T(8),T(8),T(8)],
                    [T(6),T(3),T(5),T(8),T(8),T(8),T(3),T(4),T(8),T(1),T(5),T(1),T(4),T(8),T(8),T(6),T(3),T(1),T(8),T(8),T(0)],
                    [T(7),T(4),T(1),T(3),T(7),T(2),T(6),T(5),T(1),T(8),T(3),T(2),T(7),T(8),T(7),T(2),T(4),T(5),T(7),T(6),T(2)]
                ]
            else:
                raise ValueError("There is no default board for that number of players")
        else:
            raise ValueError("Un-recognised map style")
