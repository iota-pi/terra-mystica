from enum import Enum


class Terrain(Enum):
    EMPTY = 0
    MOUNTAIN = 1
    FOREST = 2
    LAKE = 3
    SWAMP = 4
    FIELD = 5
    DESERT = 6
    WASTELAND = 7
    RIVER = 8


TERRAIN_ORDER = (
    Terrain.MOUNTAIN,
    Terrain.FOREST,
    Terrain.LAKE,
    Terrain.SWAMP,
    Terrain.FIELD,
    Terrain.DESERT,
    Terrain.WASTELAND,
)


def calculate_spade_cost(current: Terrain, target: Terrain) -> int:
    try:
        current_position = TERRAIN_ORDER.index(current)
    except ValueError:
        raise ValueError(f"Invalid terrain type for terraforming: {current}")
    try:
        target_position = TERRAIN_ORDER.index(target)
    except ValueError:
        raise ValueError(f"Invalid terrain type for terraforming: {target}")

    cost = abs(current_position - target_position)
    return cost
