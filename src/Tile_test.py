from Tile import Tile
from Terrain import Terrain
from Building import Building
from Faction import (
    Dwarves,
    Engineers,
    Auren,
    Witches,
    Swarmlings,
    Mermaids,
    Alchemists,
    Darklings,
    Halflings,
    Cultists,
    Fakirs,
    Nomads,
    ChaosMagicians,
    Giants,
)


class TestTile:
    def test_building(self):
        spot = Tile(Terrain.MOUNTAIN)
        assert spot.can_build(Building.DWELLING, Dwarves)
        assert not spot.can_build(Building.TRADING_HOUSE, Dwarves)
        assert not spot.can_build(Building.TEMPLE, Dwarves)
        assert not spot.can_build(Building.STRONGHOLD, Dwarves)
        assert not spot.can_build(Building.SANCTUARY, Dwarves)
        spot.build(Building.DWELLING, Dwarves)
        assert not spot.can_build(Building.DWELLING, Dwarves)
        assert spot.can_build(Building.TRADING_HOUSE, Dwarves)
        assert not spot.can_build(Building.TEMPLE, Dwarves)
        assert not spot.can_build(Building.STRONGHOLD, Dwarves)
        assert not spot.can_build(Building.SANCTUARY, Dwarves)
        spot.build(Building.TRADING_HOUSE, Dwarves)
        assert not spot.can_build(Building.DWELLING, Dwarves)
        assert not spot.can_build(Building.TRADING_HOUSE, Dwarves)
        assert spot.can_build(Building.TEMPLE, Dwarves)
        assert spot.can_build(Building.STRONGHOLD, Dwarves)
        assert not spot.can_build(Building.SANCTUARY, Dwarves)
        spot.build(Building.TEMPLE, Dwarves)
        assert not spot.can_build(Building.DWELLING, Dwarves)
        assert not spot.can_build(Building.TRADING_HOUSE, Dwarves)
        assert not spot.can_build(Building.TEMPLE, Dwarves)
        assert not spot.can_build(Building.STRONGHOLD, Dwarves)
        assert spot.can_build(Building.SANCTUARY, Dwarves)
        spot.build(Building.SANCTUARY, Dwarves)
        assert not spot.can_build(Building.DWELLING, Dwarves)
        assert not spot.can_build(Building.TRADING_HOUSE, Dwarves)
        assert not spot.can_build(Building.TEMPLE, Dwarves)
        assert not spot.can_build(Building.STRONGHOLD, Dwarves)
        assert not spot.can_build(Building.SANCTUARY, Dwarves)
        spot = Tile(Terrain.MOUNTAIN)
        spot.build(Building.DWELLING, Dwarves)
        spot.build(Building.TRADING_HOUSE, Dwarves)
        spot.build(Building.STRONGHOLD, Dwarves)
        assert not spot.can_build(Building.DWELLING, Dwarves)
        assert not spot.can_build(Building.TRADING_HOUSE, Dwarves)
        assert not spot.can_build(Building.TEMPLE, Dwarves)
        assert not spot.can_build(Building.STRONGHOLD, Dwarves)
        assert not spot.can_build(Building.SANCTUARY, Dwarves)
        # cross colour building tests
        spot = Tile(Terrain.MOUNTAIN)
        assert spot.can_build(Building.DWELLING, Engineers)
        assert spot.can_build(Building.DWELLING, Dwarves)
        assert not spot.can_build(Building.DWELLING, Auren)
        assert not spot.can_build(Building.DWELLING, Witches)
        assert not spot.can_build(Building.DWELLING, Swarmlings)
        assert not spot.can_build(Building.DWELLING, Mermaids)
        assert not spot.can_build(Building.DWELLING, Alchemists)
        assert not spot.can_build(Building.DWELLING, Darklings)
        assert not spot.can_build(Building.DWELLING, Halflings)
        assert not spot.can_build(Building.DWELLING, Cultists)
        assert not spot.can_build(Building.DWELLING, Fakirs)
        assert not spot.can_build(Building.DWELLING, Nomads)
        assert not spot.can_build(Building.DWELLING, ChaosMagicians)
        assert not spot.can_build(Building.DWELLING, Giants)
        spot.build(Building.DWELLING, Dwarves)
        assert not spot.can_build(Building.DWELLING, Engineers)
        assert not spot.can_build(Building.TRADING_HOUSE, Engineers)
