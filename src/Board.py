import random

# import math
from typing import Dict, List, Tuple, Set

from Cult import Cult
from errors import InvalidActionError
from Player import Player
from Terrain import Terrain
from Tile import Tile
from RoundToken import RoundToken
from round_tokens import ROUND_TOKENS
from PassToken import PassToken

# from pass_tokens import PASS_TOKENS
from AbstractResources import AbstractResources
from enum import Enum
from board_layouts import DEFAULT_BOARD, LARGER_BOARD


BOARD_WIDTH = 13
BOARD_HEIGHT = 9
NUMBER_OF_ROUNDS = 6
Coords = Tuple[int, int]


class AdjacencyType(Enum):
    DIRECT = 0
    INDIRECT = 1


class Board:
    priest_slots: Dict[Cult, int] = {
        Cult.FIRE: 4,
        Cult.EARTH: 4,
        Cult.WATER: 4,
        Cult.AIR: 4,
    }
    data: List[List[Tile]]
    rounds: List[RoundToken] = [ROUND_TOKENS[1]] * NUMBER_OF_ROUNDS
    pass_token_selection: Set[PassToken] = set()

    def __init__(self, style: str = "default", NumberOfPlayers: int = 5) -> None:
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
            if NumberOfPlayers <= 5:
                self.data = DEFAULT_BOARD
            elif NumberOfPlayers <= 7:
                self.data = LARGER_BOARD
            else:
                raise ValueError("There is no default board for that number of players")
        else:
            raise ValueError("Unrecognised map style")
        self.calculate_adjacency_for_tiles()
        self.choose_round_tokens()
        self.randomise_pass_tokens(NumberOfPlayers)

    def calculate_adjacency_for_tiles(self):
        for row in range(len(self.data)):
            for col in range(len(self.data[row])):
                coords = (col, row)
                tile = self.get(coords)
                if tile.terrain != Terrain.EMPTY:
                    tile.adjacency = set(self.get_directly_adj(coords))

    def get_tiles_of_type(self, terrain_filter: Terrain | None) -> Set[Tile]:
        return_list: Set[Tile] = set()
        for row in range(0, len(self.data)):
            for col in range(0, len(self.data[row])):
                tile = (col, row)
                tile_object = self.get(tile)
                if tile_object.terrain == terrain_filter or (
                    terrain_filter is None and tile_object.terrain != Terrain.EMPTY
                ):
                    return_list.add(tile_object)
        return return_list

    def get(self, coords: Coords):
        return self.data[coords[1]][coords[0]]

    def get_directly_adj(
        self,
        start: Coords = (0, 0),
    ) -> Set[Tile]:
        adjacent_tile_set: Set[Tile] = set()
        row_start_offset = -((start[1] + 1) % 2)
        if start[1] > 0:
            adjacent_tile_set.add(
                self.get((start[0] + row_start_offset, start[1] - 1))
            )  # top left
            adjacent_tile_set.add(
                self.get((start[0] + row_start_offset + 1, start[1] - 1))
            )  # top right
        if start[0] < BOARD_WIDTH - 2 or (
            start[1] % 2 == 1 and start[0] < BOARD_WIDTH - 1
        ):
            adjacent_tile_set.add(self.get((start[0] + 1, start[1])))  # right
        if start[1] < BOARD_HEIGHT - 1:
            adjacent_tile_set.add(
                self.get((start[0] + row_start_offset + 1, start[1] + 1))
            )  # bottom left
            adjacent_tile_set.add(
                self.get((start[0] + row_start_offset, start[1] + 1))
            )  # bottom right
        if start[0] > 0:
            adjacent_tile_set.add(self.get((start[0] - 1, start[1])))  # left
        return adjacent_tile_set

    def get_indirectly_adj(
        self,
        tile: Tile,
        shipping_limit: int = 0,
        flying: bool = False,
    ) -> Set[Tile]:
        tiles = tile.adjacency
        if shipping_limit <= 0:
            return tiles
        all_tiles = set(tiles)
        for t in tiles:
            if flying or t.terrain == Terrain.RIVER:
                all_tiles |= self.get_indirectly_adj(
                    t, shipping_limit=shipping_limit - 1
                )
        all_tiles.remove(tile)
        return all_tiles

    def filter_terrain(self, tiles: Set[Tile], terrain_filter: Terrain) -> Set[Tile]:
        filtered_tiles: Set[Tile] = set()
        for tile in tiles:
            if tile.terrain == terrain_filter:
                filtered_tiles.add(tile)
        return filtered_tiles

    def check_adjacency(
        self, start: Coords, end: Coords, shipping_limit: int
    ) -> AdjacencyType | None:
        end_tile = self.get(end)
        if end_tile in self.get_directly_adj(start):
            return AdjacencyType.DIRECT
        if end_tile in self.get_indirectly_adj(self.get(start), shipping_limit):
            return AdjacencyType.INDIRECT
        return None

    def play_priest(self, player: Player, cult: Cult):
        if self.priest_slots[cult] <= 0:
            raise InvalidActionError("Cult track has no more slots for priests")

        priest_points = 3 if self.priest_slots[cult] == 4 else 2
        self.priest_slots[cult] -= 1
        player.advance_in_cult(cult, priest_points)

    def choose_round_tokens(self):
        RoundTokensWithoutSpades: List[RoundToken] = []
        for token in ROUND_TOKENS:
            if not (
                type(token.build_bonus_condition) == AbstractResources
                and token.build_bonus_condition.spades_credit > 1
            ):
                RoundTokensWithoutSpades.append(token)
        self.rounds.append(ROUND_TOKENS[random.randint(0, len(ROUND_TOKENS) - 1)])
        self.rounds.append(ROUND_TOKENS[random.randint(0, len(ROUND_TOKENS) - 1)])
        self.rounds.append(ROUND_TOKENS[random.randint(0, len(ROUND_TOKENS) - 1)])
        self.rounds.append(ROUND_TOKENS[random.randint(0, len(ROUND_TOKENS) - 1)])
        self.rounds.append(
            RoundTokensWithoutSpades[
                random.randint(0, len(RoundTokensWithoutSpades) - 1)
            ]
        )
        self.rounds.append(
            RoundTokensWithoutSpades[
                random.randint(0, len(RoundTokensWithoutSpades) - 1)
            ]
        )
        #               This was supposed to allow for a non-standard number of rounds:
        # round = 0
        # while round < int(NUMBER_OF_ROUNDS / 3) * 2:
        #     newToken = ROUND_TOKENS[random.randint(0, len(ROUND_TOKENS) - 1)]
        #     if newToken not in self.rounds:
        #         self.rounds.append(newToken)
        #         round += 1
        #     else:
        #         round -= 1
        # while round < NUMBER_OF_ROUNDS:
        #     newToken = RoundTokensWithoutSpades[
        #         random.randint(0, len(RoundTokensWithoutSpades) - 1)
        #     ]
        #     if newToken not in self.rounds:
        #         self.rounds.append(newToken)
        #         round += 1
        #     else:
        #         round -= 1

    def randomise_pass_tokens(self, NumberOfPlayers: int):
        #               This got an "unhashable type: PassToken" error:
        #               This adds random items to the set:
        # iterator = 0
        # while iterator < NumberOfPlayers + 3:
        #     token = PASS_TOKENS[random.randint(0, len(PASS_TOKENS))]
        #     if token not in self.pass_token_selection:
        #         self.pass_token_selection.add(token)
        #         iterator += 1
        #     else:
        #         iterator -= 1
        #
        #               So I tried this way instead, but it got the same error:
        #               This removes random items from a copy of the list:
        # number_of_pass_tokens = NumberOfPlayers + 3
        # remove_pass_tokens = len(PASS_TOKENS) - number_of_pass_tokens
        # pass_token_list = PASS_TOKENS
        # counter = 0
        # while counter < remove_pass_tokens:
        #     token = PASS_TOKENS[random.randint(0, len(PASS_TOKENS))]
        #     pass_token_list.remove(token)
        #     counter += 1
        # for token in pass_token_list:
        #     self.pass_token_selection.add(token)
        #
        #               But neither of them worked.
        return
