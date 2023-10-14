import random
import math

from Tile import Tile
from board_layouts import DEFAULT_BOARD, LARGER_BOARD


BOARD_WIDTH = 13
BOARD_HEIGHT = 9


class Board:
    def __init__(self, style="default", size=5) -> None:
        extention = 0  # provision for games with more players
        if size > 5:
            extention = math.floor((math.ceil((size - 5) / 3) * 3) * 2.8)
        if style == "random":
            self.data = [
                [
                    Tile(terrain=random.randint(1, 9))
                    for _ in range(BOARD_WIDTH + extention)
                ]
                for _ in range(BOARD_HEIGHT)
            ]
            self.data[2][-1] = 0
            self.data[4][-1] = 0
            self.data[6][-1] = 0
            self.data[8][-1] = 0
        elif style == "default":
            if size <= 5:
                self.data = DEFAULT_BOARD
            elif size <= 7:
                self.data = LARGER_BOARD
            else:
                raise ValueError("There is no default board for that number of players")
        else:
            raise ValueError("Un-recognised map style")
