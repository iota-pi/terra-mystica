# import random
# import math
from typing import Dict, List, Tuple

from Cult import Cult
from errors import InvalidActionError
from Player import Player
from Terrain import Terrain
from Tile import Tile
from board_layouts import DEFAULT_BOARD, LARGER_BOARD


BOARD_WIDTH = 13
BOARD_HEIGHT = 9
Coords = Tuple[int, int]


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

    def get(self, coords: Coords):
        return self.data[coords[1]][coords[0]]

    def get_directly_adj(
        self,
        start: Coords = (0, 0),
        terrain_filter: Terrain | None = None,
    ) -> List[Coords]:
        adjacent_tile_list = []
        row_start_offset = -(start[1] % 2)
        if terrain_filter is None:
            if start[1] > 0:
                adjacent_tile_list.append(
                    (start[0] + row_start_offset, start[1] - 1)
                )  # top left
                adjacent_tile_list.append(
                    (start[0] + row_start_offset + 1, start[1] - 1)
                )  # top right
            if start[0] < BOARD_WIDTH - 2 or (
                start[1] % 2 == 1 and start[0] < BOARD_WIDTH - 1
            ):
                adjacent_tile_list.append((start[0] + 1, start[1]))  # right
            if start[1] < BOARD_HEIGHT - 1:
                adjacent_tile_list.append(
                    (start[0] + row_start_offset, start[1] + 1)
                )  # bottom left
                adjacent_tile_list.append(
                    (start[0] + row_start_offset + 1, start[1] + 1)
                )  # bottom right
            if start[0] > 0:
                adjacent_tile_list.append((start[0] - 1, start[1]))  # left
        else:
            unfiltered_list = self.get_directly_adj(start, None)
            for tile in unfiltered_list:
                if self.get(tile)._terrain == terrain_filter:
                    adjacent_tile_list.append(tile)
        return adjacent_tile_list  # = [TL,TR,R,BR,BL,L]

    def get_indirectly_adj(
        self, start=(0, 0), terrain_filter=None, shipping_limit=0
    ) -> list:
        adjacent_tile_list = []
        if self.get_directly_adj(start, Terrain.RIVER) == []:
            return self.get_directly_adj(start, None)
        if shipping_limit == 0:
            direct_list = self.get_directly_adj(start, terrain_filter)
            for tile in direct_list:
                if tile not in adjacent_tile_list:
                    adjacent_tile_list.append(tile)
        else:
            direct_list = self.get_directly_adj(start, None)
            for tile in direct_list:
                if self.get(tile).terrain == Terrain.RIVER:
                    indirect_list = self.get_indirectly_adj(
                        tile, terrain_filter, shipping_limit - 1
                    )
                    for t in indirect_list:
                        if t not in adjacent_tile_list:
                            adjacent_tile_list.append(t)
                else:
                    adjacent_tile_list.append(tile)
        return adjacent_tile_list

    def check_adjacency(self, start, end, shipping_limit) -> str:
        for tile in self.get_directly_adj(start, self.get(end)._terrain):
            if tile == end:
                return "Direct"
        for tile in self.get_indirectly_adj(
            start, self.get(end)._terrain, shipping_limit=shipping_limit
        ):
            if tile == end:
                return "Indirect"
        return "Not"

    def play_priest(self, player: Player, cult: Cult):
        if self.priest_slots[cult] <= 0:
            raise InvalidActionError("Cult track has no more slots for priests")

        priest_points = 3 if self.priest_slots[cult] == 4 else 2
        self.priest_slots[cult] -= 1
        player.advance_in_cult(cult, priest_points)
