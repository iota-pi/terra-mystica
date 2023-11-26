from enum import Enum
from Building import Building

from Resources import Resources
from CultProgress import CultProgress
from Terrain import Terrain


class FactionColour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    BROWN = 5
    GREY = 6
    BLACK = 7


class Faction:
    name: str
    starting_resources = Resources(
        workers=3,
        coins=15,
        power=7,
    )
    starting_cult: CultProgress
    starting_dwellings = 2
    starting_shipping = 0
    colour: FactionColour
    terrain: Terrain

    base_income = Resources(workers=1)

    dwelling_cost = Resources(workers=1, coins=2)
    dwelling_incomes = (
        Resources(workers=1),
        Resources(workers=1),
        Resources(workers=1),
        Resources(workers=1),
        Resources(workers=1),
        Resources(workers=1),
        Resources(workers=1),
        Resources(),
    )

    trading_house_cost = Resources(workers=2, coins=3)
    trading_house_incomes = (
        Resources(power=1, coins=2),
        Resources(power=1, coins=2),
        Resources(power=2, coins=2),
        Resources(power=2, coins=2),
    )

    temple_cost = Resources(workers=2, coins=5)
    temple_incomes = (
        Resources(priests=1),
        Resources(priests=1),
        Resources(priests=1),
    )
    temple_favour_tokens = 1

    stronghold_cost = Resources(workers=4, coins=6)
    stronghold_income = Resources(power=2)
    stronghold_favour_tokens = 0
    # TODO
    # stronghold_action: PlayerAction

    sanctuary_cost = Resources(workers=4, coins=6)
    sanctuary_income = Resources(priests=1)
    sanctuary_favour_tokens = 1

    disable_shipping = False
    spade_upgrade_cost = Resources(workers=2, coins=5, priests=1)
    spade_max_upgrades = 2

    # TODO
    # extra cult abilities

    @classmethod
    def get_building_cost(cls, building: Building):
        if building == Building.DWELLING:
            return cls.dwelling_cost
        # TODO for non-neighbouring trading houses, coins cost is doubled
        if building == Building.TRADING_HOUSE:
            return cls.trading_house_cost
        if building == Building.TEMPLE:
            return cls.temple_cost
        if building == Building.STRONGHOLD:
            return cls.stronghold_cost
        if building == Building.SANCTUARY:
            return cls.sanctuary_cost
        raise ValueError(f"Unknown building type: {building}")


class ChaosMagicians(Faction):
    name = "Chaos Magicians"
    starting_resources = Resources(
        workers=4,
        coins=15,
        power=7,
    )
    starting_cult = CultProgress(
        fire=2,
    )
    starting_dwellings = 1
    colour = FactionColour.RED
    terrain = Terrain.WASTELAND

    temple_favour_tokens = 2

    stronghold_cost = Resources(workers=4, coins=4)
    stronghold_income = Resources(workers=2)

    sanctuary_cost = Resources(workers=4, coins=8)
    sanctuary_favour_tokens = 2


class Giants(Faction):
    name = "Giants"
    starting_cult = CultProgress(
        fire=1,
        air=1,
    )
    colour = FactionColour.RED
    terrain = Terrain.WASTELAND

    stronghold_income = Resources(power=4)


class Auren(Faction):
    name = "Auren"
    starting_cult = CultProgress(
        water=1,
        air=1,
    )
    colour = FactionColour.GREEN
    terrain = Terrain.FOREST

    stronghold_favour_tokens = 1

    sanctuary_cost = Resources(workers=4, coins=8)


class Witches(Faction):
    name = "Witches"
    starting_cult = CultProgress(
        air=2,
    )
    colour = FactionColour.GREEN
    terrain = Terrain.FOREST


class Swarmlings(Faction):
    name = "Swarmlings"
    starting_resources = Resources(
        workers=8,
        coins=20,
        power=9,
    )
    starting_cult = CultProgress(
        fire=1,
        earth=1,
        water=1,
        air=1,
    )
    colour = FactionColour.BLUE
    terrain = Terrain.LAKE

    base_income = Resources(workers=2)

    dwelling_cost = Resources(workers=2, coins=3)

    trading_house_cost = Resources(workers=3, coins=4)
    trading_house_incomes = (
        Resources(power=2, coins=2),
        Resources(power=2, coins=2),
        Resources(power=2, coins=2),
        Resources(power=2, coins=3),
    )

    temple_cost = Resources(workers=3, coins=6)

    stronghold_cost = Resources(workers=5, coins=8)
    stronghold_income = Resources(power=4)

    sanctuary_cost = Resources(workers=5, coins=8)
    sanctuary_income = Resources(priests=2)


class Mermaids(Faction):
    name = "Mermaids"
    starting_resources = Resources(
        workers=3,
        coins=15,
        power=9,
    )
    starting_cult = CultProgress(
        water=2,
    )
    starting_shipping = 1
    colour = FactionColour.BLUE
    terrain = Terrain.LAKE

    stronghold_income = Resources(power=4)

    sanctuary_cost = Resources(workers=4, coins=8)


class Fakirs(Faction):
    name = "Fakirs"
    starting_resources = Resources(
        workers=3,
        coins=15,
        power=5,
    )
    starting_cult = CultProgress(
        fire=1,
        air=1,
    )
    colour = FactionColour.YELLOW
    terrain = Terrain.DESERT

    stronghold_cost = Resources(workers=4, coins=10)
    stronghold_income = Resources(priests=1)

    disable_shipping = True
    spade_max_upgrades = 1


class Nomads(Faction):
    name = "Nomads"
    starting_resources = Resources(
        workers=2,
        coins=15,
        power=7,
    )
    starting_cult = CultProgress(
        fire=1,
        earth=1,
    )
    starting_dwellings = 3
    colour = FactionColour.YELLOW
    terrain = Terrain.DESERT

    trading_house_incomes = (
        Resources(power=1, coins=2),
        Resources(power=1, coins=2),
        Resources(power=1, coins=3),
        Resources(power=1, coins=4),
    )

    stronghold_cost = Resources(workers=4, coins=8)


class Halflings(Faction):
    name = "Halflings"
    starting_resources = Resources(
        workers=3,
        coins=15,
        power=9,
    )
    starting_cult = CultProgress(
        earth=1,
        air=1,
    )
    colour = FactionColour.BROWN
    terrain = Terrain.FIELD

    stronghold_cost = Resources(workers=4, coins=8)

    spade_upgrade_cost = Resources(workers=2, coins=1, priests=1)


class Cultists(Faction):
    name = "Cultists"
    starting_cult = CultProgress(
        fire=1,
        earth=1,
    )
    colour = FactionColour.BROWN
    terrain = Terrain.FIELD

    stronghold_cost = Resources(workers=4, coins=8)

    sanctuary_cost = Resources(workers=4, coins=8)


class Engineers(Faction):
    name = "Engineers"
    starting_resources = Resources(
        workers=2,
        coins=10,
        power=9,
    )
    starting_cult = CultProgress()
    colour = FactionColour.GREY
    terrain = Terrain.MOUNTAIN

    base_income = Resources()

    dwelling_cost = Resources(workers=1, coins=1)
    dwelling_incomes = (
        Resources(workers=1),
        Resources(workers=1),
        Resources(),
        Resources(workers=1),
        Resources(workers=1),
        Resources(),
        Resources(workers=1),
        Resources(workers=1),
    )

    trading_house_cost = Resources(workers=1, coins=2)

    temple_cost = Resources(workers=1, coins=4)
    temple_incomes = (
        Resources(priests=1),
        Resources(power=5),
        Resources(priests=1),
    )

    stronghold_cost = Resources(workers=3, coins=6)

    sanctuary_cost = Resources(workers=3, coins=6)


class Dwarves(Faction):
    name = "Dwarves"
    starting_cult = CultProgress(
        earth=2,
    )
    colour = FactionColour.GREY
    terrain = Terrain.MOUNTAIN

    trading_house_incomes = (
        Resources(power=1, coins=3),
        Resources(power=1, coins=2),
        Resources(power=2, coins=2),
        Resources(power=2, coins=3),
    )

    stronghold_cost = Resources(workers=4, coins=8)

    sanctuary_cost = Resources(workers=4, coins=8)

    disable_shipping = True


class Darklings(Faction):
    name = "Darklings"
    starting_resources = Resources(
        workers=1,
        coins=15,
        power=7,
        priests=1,
    )
    starting_cult = CultProgress(
        water=1,
        earth=1,
    )
    colour = FactionColour.BLACK
    terrain = Terrain.SWAMP

    sanctuary_cost = Resources(workers=4, coins=10)
    sanctuary_income = Resources(priests=2)

    spade_max_upgrades = 0


class Alchemists(Faction):
    name = "Alchemists"
    starting_cult = CultProgress(
        fire=1,
        water=1,
    )
    colour = FactionColour.BLACK
    terrain = Terrain.SWAMP

    trading_house_incomes = (
        Resources(power=1, coins=2),
        Resources(power=1, coins=2),
        Resources(power=1, coins=3),
        Resources(power=1, coins=4),
    )

    stronghold_income = Resources(coins=6)
