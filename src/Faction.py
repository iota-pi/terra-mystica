from collections import Enum

from Resources import Resources
from CultProgress import CultProgress


class FactionColour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    BROWN = 5
    GREY = 6
    BLACK = 7


class Faction:
    starting_resources = Resources(
        workers=3,
        coins=15,
        power=7,
    )
    starting_cult: CultProgress
    starting_dwellings = 2
    starting_shipping = 0
    colour: FactionColour

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

    # TODO for non-neighbouring trading houses, coins cost is doubled
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


class ChaosMagicians(Faction):
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

    temple_favour_tokens = 2

    stronghold_cost = Resources(workers=4, coins=4)
    stronghold_income = Resources(workers=2)

    sanctuary_cost = Resources(workers=4, coins=8)
    sanctuary_favour_tokens = 2



class Giants(Faction):
    starting_cult = CultProgress(
        fire=1,
        air=1,
    )
    colour = FactionColour.RED

    stronghold_income = Resources(power=4)


class Auren(Faction):
    starting_cult = CultProgress(
        water=1,
        air=1,
    )
    colour = FactionColour.GREEN

    stronghold_favour_tokens = 1

    sanctuary_cost = Resources(workers=4, coins=8)


class Witches(Faction):
    starting_cult = CultProgress(
        air=2,
    )
    colour = FactionColour.GREEN


class Swarmlings(Faction):
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

    stronghold_income = Resources(power=4)

    sanctuary_cost = Resources(workers=4, coins=8)


class Fakirs(Faction):
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

    stronghold_cost = Resources(workers=4, coins=10)
    stronghold_income = Resources(priests=1)

    disable_shipping = True
    spade_max_upgrades = 1


class Nomads(Faction):
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

    trading_house_incomes = (
        Resources(power=1, coins=2),
        Resources(power=1, coins=2),
        Resources(power=1, coins=3),
        Resources(power=1, coins=4),
    )

    stronghold_cost = Resources(workers=4, coins=8)


class Halflings(Faction):
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

    stronghold_cost = Resources(workers=4, coins=8)

    spade_upgrade_cost = Resources(workers=2, coins=1, priests=1)


class Cultists(Faction):
    starting_cult = CultProgress(
        fire=1,
        earth=1,
    )
    colour = FactionColour.BROWN

    stronghold_cost = Resources(workers=4, coins=8)

    sanctuary_cost = Resources(workers=4, coins=8)


class Engineers(Faction):
    starting_resources = Resources(
        workers=2,
        coins=10,
        power=9,
    )
    starting_cult = CultProgress()
    colour = FactionColour.GREY

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
    starting_cult = CultProgress(
        earth=2,
    )
    colour = FactionColour.GREY

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

    sanctuary_cost = Resources(workers=4, coins=10)
    sanctuary_income = Resources(priests=2)

    spade_max_upgrades = 0


class Alchemists(Faction):
    starting_cult = CultProgress(
        fire=1,
        water=1,
    )
    colour = FactionColour.BLACK

    trading_house_incomes = (
        Resources(power=1, coins=2),
        Resources(power=1, coins=2),
        Resources(power=1, coins=3),
        Resources(power=1, coins=4),
    )

    stronghold_income = Resources(coins=6)
