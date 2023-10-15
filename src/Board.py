import random
import math

from Terrain import Terrain
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

    def getDirectlyAdj(self, start = (0, 0), TerainFilter = None) -> list:
        adjacentTileList = []
        if start[1] % 2 == 0: # for even rows
            if TerainFilter is None or TerainFilter == self.data[start[0]][start[1] - 1].terrain:
                adjacentTileList.append((start[0], start[1] - 1)) # top left
            if TerainFilter is None or TerainFilter == self.data[start[0] + 1][start[1] - 1].terrain:
                adjacentTileList.append((start[0] + 1, start[1] - 1)) # top right
        else: # for odd rows
            if TerainFilter is None or TerainFilter == self.data[start[0] - 1][start[1] - 1].terrain:
                adjacentTileList.append((start[0] - 1, start[1] - 1)) # top left
            if TerainFilter is None or TerainFilter == self.data[start[0]][start[1] - 1].terrain:
                adjacentTileList.append((start[0], start[1] - 1)) # top right
        if TerainFilter is None or TerainFilter == self.data[start[0] + 1][start[1]].terrain:
            adjacentTileList.append((start[0] + 1, start[1])) # right
        if start[1] % 2 == 0: # for even rows
            if TerainFilter is None or TerainFilter == self.data[start[0] + 1][start[1] + 1].terrain:
                adjacentTileList.append((start[0] + 1, start[1] + 1)) # bottom right
            if TerainFilter is None or TerainFilter == self.data[start[0]][start[1] + 1].terrain:
                adjacentTileList.append((start[0], start[1] + 1)) # bottom left
        else: # for odd rows
            if TerainFilter is None or TerainFilter == self.data[start[0]][start[1] + 1].terrain:
                adjacentTileList.append((start[0], start[1] + 1)) # bottom right
            if TerainFilter is None or TerainFilter == self.data[start[0] - 1][start[1] + 1].terrain:
                adjacentTileList.append((start[0] - 1, start[1] + 1)) # bottom left
        if TerainFilter is None or TerainFilter == self.data[start[0] - 1][start[1]].terrain:
            adjacentTileList.append((start[0] - 1, start[1])) # left
        return adjacentTileList # = [TL,TR,R,BR,BL,L]

    def getIndirectlyAdj(self, start = (0, 0), TerainFilter = None, shippingLimit = 0) -> list:
        if self.getDirectlyAdj(start, Terrain.RIVER) == []:
            return []
        if shippingLimit == 0:
            return self.getDirectlyAdj(start, TerainFilter)
        adjacentTileList = []
        if start[1] % 2 == 0: # for even rows
            if TerainFilter is None or TerainFilter == self.data[start[0]][start[1] - 1].terrain:
                if self.data[start[0]][start[1] - 1].terrain == Terrain.RIVER:
                    for tile in self.getIndirectlyAdj((start[0], start[1] - 1), TerainFilter, shippingLimit - 1):
                        adjacentTileList.append(tile)
                else:
                    adjacentTileList.append((start[0], start[1] - 1)) # top left
            if TerainFilter is None or TerainFilter == self.data[start[0] + 1][start[1] - 1].terrain:
                if self.data[start[0] + 1][start[1] - 1].terrain == Terrain.RIVER:
                    for tile in self.getIndirectlyAdj((start[0] + 1, start[1] - 1), TerainFilter, shippingLimit - 1):
                        adjacentTileList.append(tile)
                else:
                    adjacentTileList.append((start[0] + 1, start[1] - 1)) # top right
        else: # for odd rows
            if TerainFilter is None or TerainFilter == self.data[start[0] - 1][start[1] - 1].terrain:
                if self.data[start[0] - 1][start[1] - 1].terrain == Terrain.RIVER:
                    for tile in self.getIndirectlyAdj((start[0] - 1, start[1] - 1), TerainFilter, shippingLimit - 1):
                        adjacentTileList.append(tile)
                else:
                    adjacentTileList.append((start[0] - 1, start[1] - 1)) # top left
            if TerainFilter is None or TerainFilter == self.data[start[0]][start[1] - 1].terrain:
                if self.data[start[0]][start[1] - 1].terrain == Terrain.RIVER:
                    for tile in self.getIndirectlyAdj((start[0], start[1] - 1), TerainFilter, shippingLimit - 1):
                        adjacentTileList.append(tile)
                else:
                    adjacentTileList.append((start[0], start[1] - 1)) # top right
        if TerainFilter is None or TerainFilter == self.data[start[0] + 1][start[1]].terrain:
            if self.data[start[0] + 1][start[1]].terrain == Terrain.RIVER:
                for tile in self.getIndirectlyAdj((start[0] + 1, start[1]), TerainFilter, shippingLimit - 1):
                    adjacentTileList.append(tile)
            else:
                adjacentTileList.append((start[0] + 1, start[1])) # right
        if start[1] % 2 == 0: # for even rows
            if TerainFilter is None or TerainFilter == self.data[start[0] + 1][start[1] + 1].terrain:
                if self.data[start[0] + 1][start[1] + 1].terrain == Terrain.RIVER:
                    for tile in self.getIndirectlyAdj((start[0] + 1, start[1] + 1), TerainFilter, shippingLimit - 1):
                        adjacentTileList.append(tile)
                else:
                    adjacentTileList.append((start[0] + 1, start[1] + 1)) # bottom right
            if TerainFilter is None or TerainFilter == self.data[start[0]][start[1] + 1].terrain:
                if self.data[start[0]][start[1] + 1].terrain == Terrain.RIVER:
                    for tile in self.getIndirectlyAdj((start[0], start[1] + 1), TerainFilter, shippingLimit - 1):
                        adjacentTileList.append(tile)
                else:
                    adjacentTileList.append((start[0], start[1] + 1)) # bottom left
        else: # for odd rows
            if TerainFilter is None or TerainFilter == self.data[start[0]][start[1] + 1].terrain:
                if self.data[start[0]][start[1] + 1].terrain == Terrain.RIVER:
                    for tile in self.getIndirectlyAdj((start[0], start[1] + 1), TerainFilter, shippingLimit - 1):
                        adjacentTileList.append(tile)
                else:
                    adjacentTileList.append((start[0], start[1] + 1)) # bottom right
            if TerainFilter is None or TerainFilter == self.data[start[0] - 1][start[1] + 1].terrain:
                if self.data[start[0] - 1][start[1] + 1].terrain == Terrain.RIVER:
                    for tile in self.getIndirectlyAdj((start[0] - 1, start[1] + 1), TerainFilter, shippingLimit - 1):
                        adjacentTileList.append(tile)
                else:
                    adjacentTileList.append((start[0] - 1, start[1] + 1)) # bottom left
        if TerainFilter is None or TerainFilter == self.data[start[0] - 1][start[1]].terrain:
            if self.data[start[0] - 1][start[1]].terrain == Terrain.RIVER:
                for tile in self.getIndirectlyAdj((start[0] - 1, start[1]), TerainFilter, shippingLimit - 1):
                    adjacentTileList.append(tile)
            else:
                adjacentTileList.append((start[0] - 1, start[1])) # left
        adjacentTileList = self.removeSubsequentDuplicates(adjacentTileList)
        return adjacentTileList
        
    def checkAdjacency(self, start = (0, 0), end = (0, 0)) -> str:
        for tile in self.getDirectlyAdj(start, self.data[end[0]][end[1]]):
            if tile == end:
                return "Direct"
        for tile in self.getIndirectlyAdj(start, self.data[end[0]][end[1]]):
            if tile == end:
                return "Indirect"
        return "Not"
             
    def removeSubsequentDuplicates(list = []) -> list:
        newList = []
        for tile1 in list:
            found = False
            for tile2 in newList:
                if tile1 == tile2:
                    found = True
            if not found:
                newList.append(tile1)
        return newList