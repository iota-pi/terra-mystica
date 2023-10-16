# import random
# import math
from typing import Dict, List

from Cult import Cult
from errors import InvalidActionError
from Player import Player
from Terrain import Terrain
from Tile import Tile
from board_layouts import DEFAULT_BOARD, LARGER_BOARD


BOARD_WIDTH = 13
BOARD_HEIGHT = 9


class Board:
    priest_slots: Dict[Cult, int] = {
        Cult.FIRE: 4,
        Cult.EARTH: 4,
        Cult.WATER: 4,
        Cult.AIR: 4,
    }
    data: List[List[Tile]]

    def __init__(self, style: str = "default", size: int = 5) -> None:
        # Commented out the following because it doesn't work with strict typechecking
        # extension = 0  # provision for games with more players
        # if size > 5:
        #     extension = math.floor((math.ceil((size - 5) / 3) * 3) * 2.8)
        # if style == "random":
        #     self.data = [
        #         [
        #             Tile(terrain=random.randint(1, 9))
        #             for _ in range(BOARD_WIDTH + extension)
        #         ]
        #         for _ in range(BOARD_HEIGHT)
        #     ]
        #     self.data[2][-1] = 0
        #     self.data[4][-1] = 0
        #     self.data[6][-1] = 0
        #     self.data[8][-1] = 0
        # elif style == "default":
        if style == "default":
            if size <= 5:
                self.data = DEFAULT_BOARD
            elif size <= 7:
                self.data = LARGER_BOARD
            else:
                raise ValueError("There is no default board for that number of players")
        else:
            raise ValueError("Unrecognised map style")

    def get(self, x, y):
        return self.data[y][x]

    def getDirectlyAdj(self, start=(0, 0), TerainFilter=None) -> list:
        adjacentTileList = []
        if start[1] > 0:
            if start[1] % 2 == 0:  # for even rows
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0], start[1] - 1).terrain
                ):
                    adjacentTileList.append((start[0], start[1] - 1))  # top left
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0] + 1, start[1] - 1).terrain
                ):
                    adjacentTileList.append((start[0] + 1, start[1] - 1))  # top right
            else:  # for odd rows
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0] - 1, start[1] - 1).terrain
                ):
                    adjacentTileList.append((start[0] - 1, start[1] - 1))  # top left
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0], start[1] - 1).terrain
                ):
                    adjacentTileList.append((start[0], start[1] - 1))  # top right
        if start[0] < BOARD_WIDTH - 2 or (
            start[1] % 2 == 1 and start[0] < BOARD_WIDTH - 1
        ):
            if (
                TerainFilter is None
                or TerainFilter == self.get(start[0] + 1, start[1]).terrain
            ):
                adjacentTileList.append((start[0] + 1, start[1]))  # right
        if start[1] < BOARD_HEIGHT - 1:
            if start[1] % 2 == 0:  # for even rows
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0] + 1, start[1] + 1).terrain
                ):
                    adjacentTileList.append(
                        (start[0] + 1, start[1] + 1)
                    )  # bottom right
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0], start[1] + 1).terrain
                ):
                    adjacentTileList.append((start[0], start[1] + 1))  # bottom left
            else:  # for odd rows
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0], start[1] + 1).terrain
                ):
                    adjacentTileList.append((start[0], start[1] + 1))  # bottom right
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0] - 1, start[1] + 1).terrain
                ):
                    adjacentTileList.append((start[0] - 1, start[1] + 1))  # bottom left
        if start[0] > 0:
            if (
                TerainFilter is None
                or TerainFilter == self.get(start[0] - 1, start[1]).terrain
            ):
                adjacentTileList.append((start[0] - 1, start[1]))  # left
        return adjacentTileList  # = [TL,TR,R,BR,BL,L]

    def getIndirectlyAdj(
        self, start=(0, 0), TerainFilter=None, shippingLimit=0
    ) -> list:
        if self.getDirectlyAdj(start, Terrain.RIVER) == []:
            return []
        if shippingLimit == 0:
            return self.getDirectlyAdj(start, TerainFilter)
        adjacentTileList = []
        if start[1] > 0:
            if start[1] % 2 == 0:  # for even rows
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0], start[1] - 1).terrain
                ):
                    if self.get(start[0], start[1] - 1).terrain == Terrain.RIVER:
                        for tile in self.getIndirectlyAdj(
                            (start[0], start[1] - 1), TerainFilter, shippingLimit - 1
                        ):
                            adjacentTileList.append(tile)
                    else:
                        adjacentTileList.append((start[0], start[1] - 1))  # top left
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0] + 1, start[1] - 1).terrain
                ):
                    if self.get(start[0] + 1, start[1] - 1).terrain == Terrain.RIVER:
                        for tile in self.getIndirectlyAdj(
                            (start[0] + 1, start[1] - 1),
                            TerainFilter,
                            shippingLimit - 1,
                        ):
                            adjacentTileList.append(tile)
                    else:
                        adjacentTileList.append(
                            (start[0] + 1, start[1] - 1)
                        )  # top right
            else:  # for odd rows
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0] - 1, start[1] - 1).terrain
                ):
                    if self.get(start[0] - 1, start[1] - 1).terrain == Terrain.RIVER:
                        for tile in self.getIndirectlyAdj(
                            (start[0] - 1, start[1] - 1),
                            TerainFilter,
                            shippingLimit - 1,
                        ):
                            adjacentTileList.append(tile)
                    else:
                        adjacentTileList.append(
                            (start[0] - 1, start[1] - 1)
                        )  # top left
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0], start[1] - 1).terrain
                ):
                    if self.get(start[0], start[1] - 1).terrain == Terrain.RIVER:
                        for tile in self.getIndirectlyAdj(
                            (start[0], start[1] - 1), TerainFilter, shippingLimit - 1
                        ):
                            adjacentTileList.append(tile)
                    else:
                        adjacentTileList.append((start[0], start[1] - 1))  # top right
        if start[0] < BOARD_WIDTH - 2 or (
            start[1] % 2 == 1 and start[0] < BOARD_WIDTH - 1
        ):
            if (
                TerainFilter is None
                or TerainFilter == self.get(start[0] + 1, start[1]).terrain
            ):
                if self.get(start[0] + 1, start[1]).terrain == Terrain.RIVER:
                    for tile in self.getIndirectlyAdj(
                        (start[0] + 1, start[1]), TerainFilter, shippingLimit - 1
                    ):
                        adjacentTileList.append(tile)
                else:
                    adjacentTileList.append((start[0] + 1, start[1]))  # right
        if start[1] < BOARD_HEIGHT - 1:
            if start[1] % 2 == 0:  # for even rows
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0] + 1, start[1] + 1).terrain
                ):
                    if self.get(start[0] + 1, start[1] + 1).terrain == Terrain.RIVER:
                        for tile in self.getIndirectlyAdj(
                            (start[0] + 1, start[1] + 1),
                            TerainFilter,
                            shippingLimit - 1,
                        ):
                            adjacentTileList.append(tile)
                    else:
                        adjacentTileList.append(
                            (start[0] + 1, start[1] + 1)
                        )  # bottom right
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0], start[1] + 1).terrain
                ):
                    if self.get(start[0], start[1] + 1).terrain == Terrain.RIVER:
                        for tile in self.getIndirectlyAdj(
                            (start[0], start[1] + 1), TerainFilter, shippingLimit - 1
                        ):
                            adjacentTileList.append(tile)
                    else:
                        adjacentTileList.append((start[0], start[1] + 1))  # bottom left
            else:  # for odd rows
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0], start[1] + 1).terrain
                ):
                    if self.get(start[0], start[1] + 1).terrain == Terrain.RIVER:
                        for tile in self.getIndirectlyAdj(
                            (start[0], start[1] + 1), TerainFilter, shippingLimit - 1
                        ):
                            adjacentTileList.append(tile)
                    else:
                        adjacentTileList.append(
                            (start[0], start[1] + 1)
                        )  # bottom right
                if (
                    TerainFilter is None
                    or TerainFilter == self.get(start[0] - 1, start[1] + 1).terrain
                ):
                    if self.get(start[0] - 1, start[1] + 1).terrain == Terrain.RIVER:
                        for tile in self.getIndirectlyAdj(
                            (start[0] - 1, start[1] + 1),
                            TerainFilter,
                            shippingLimit - 1,
                        ):
                            adjacentTileList.append(tile)
                    else:
                        adjacentTileList.append(
                            (start[0] - 1, start[1] + 1)
                        )  # bottom left
        if start[0] > 0:
            if (
                TerainFilter is None
                or TerainFilter == self.get(start[0] - 1, start[1]).terrain
            ):
                if self.get(start[0] - 1, start[1]).terrain == Terrain.RIVER:
                    for tile in self.getIndirectlyAdj(
                        (start[0] - 1, start[1]), TerainFilter, shippingLimit - 1
                    ):
                        adjacentTileList.append(tile)
                else:
                    adjacentTileList.append((start[0] - 1, start[1]))  # left
        adjacentTileList = self.removeSubsequentDuplicates(adjacentTileList)
        return adjacentTileList

    def checkAdjacency(self, start, end, shippingLimit) -> str:
        for tile in self.getDirectlyAdj(start, self.get(end[0], end[1]).terrain):
            if tile == end:
                return "Direct"
        for tile in self.getIndirectlyAdj(
            start, self.get(end[0], end[1]).terrain, shippingLimit=shippingLimit
        ):
            if tile == end:
                return "Indirect"
        return "Not"

    def removeSubsequentDuplicates(list=[]) -> list:
        newList = []
        for tile1 in list:
            found = False
            for tile2 in newList:
                if tile1 == tile2:
                    found = True
            if not found:
                newList.append(tile1)
        return newList

    def play_priest(self, player: Player, cult: Cult):
        if self.priest_slots[cult] <= 0:
            raise InvalidActionError("Cult track has no more slots for priests")

        priest_points = 3 if self.priest_slots[cult] == 4 else 2
        self.priest_slots[cult] -= 1
        player.advance_in_cult(cult, priest_points)
