from abc import ABC
from enum import Enum
from typing import List, Type
from Action import (
    Action,
    AurenStrongholdAction,
    BonusAction,
    ChaosMagicianStrongholdAction,
    CultistsNeighbourBonusAction,
    CultistsStrongholdBonusAction,
    DarklingsStrongholdBonusAction,
    DwarvesBasicAction,
    DwarvesStrongholdAction,
    FakirsBasicAction,
    FakirsStrongholdAction,
    GiantsStrongholdAction,
    HalflingsStrongholdBonusAction,
    MermaidStrongholdBonusAction,
    NomadsStrongholdAction,
    SwarmlingsStrongholdAction,
    WitchesStrongholdAction,
)
from Building import Building
from Player import Player

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


class Faction(ABC):
    name: str
    starting_resources = Resources(
        workers=3,
        coins=15,
        power=7,
    )
    starting_cult: CultProgress
    starting_dwellings = 2
    colour: FactionColour
    terrain: Terrain
    basic_actions: List[Type[Action]] = []

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
    stronghold_action: Type[Action] | None = None
    stronghold_once_off_action: Type[BonusAction] | None = None

    sanctuary_cost = Resources(workers=4, coins=6)
    sanctuary_income = Resources(priests=1)
    sanctuary_favour_tokens = 1

    spade_upgrade_cost = Resources(workers=2, coins=5, priests=1)
    spade_max_upgrades = 2
    spade_terraform_cost = 1
    spade_track_disabled = False
    spade_bonus_points = 0

    shipping_upgrade_cost = Resources(priests=1, coins=4)
    shipping_disabled = False
    shipping_start_level = 0
    shipping_max_level = 3

    town_bonus = Resources()

    neighbouring_dwelling_action: Type[BonusAction] | None = None

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

    @classmethod
    def handle_spade(cls, player: Player):
        pass

    @classmethod
    def handle_town(cls, player: Player):
        player.gain(cls.town_bonus)

    @classmethod
    def handle_end_of_round(cls, player: Player):
        pass


# Factions
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
    stronghold_action = ChaosMagicianStrongholdAction

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
    stronghold_action = GiantsStrongholdAction

    spade_terraform_cost = 2
    spade_track_disabled = True


class Auren(Faction):
    name = "Auren"
    starting_cult = CultProgress(
        water=1,
        air=1,
    )
    colour = FactionColour.GREEN
    terrain = Terrain.FOREST

    stronghold_favour_tokens = 1
    stronghold_action = AurenStrongholdAction

    sanctuary_cost = Resources(workers=4, coins=8)


class Witches(Faction):
    name = "Witches"
    starting_cult = CultProgress(
        air=2,
    )
    colour = FactionColour.GREEN
    terrain = Terrain.FOREST

    stronghold_action = WitchesStrongholdAction

    town_bonus = Resources(points=5)


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
    stronghold_action = SwarmlingsStrongholdAction

    sanctuary_cost = Resources(workers=5, coins=8)
    sanctuary_income = Resources(priests=2)

    town_bonus = Resources(workers=3)


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
    colour = FactionColour.BLUE
    terrain = Terrain.LAKE

    stronghold_income = Resources(power=4)
    stronghold_once_off_action = MermaidStrongholdBonusAction

    sanctuary_cost = Resources(workers=4, coins=8)

    shipping_start_level = 1
    shipping_max_level = 5


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
    basic_actions = [FakirsBasicAction]

    stronghold_cost = Resources(workers=4, coins=10)
    stronghold_income = Resources(priests=1)
    stronghold_action = FakirsStrongholdAction

    shipping_disabled = True
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
    stronghold_action = NomadsStrongholdAction


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
    stronghold_once_off_action = HalflingsStrongholdBonusAction

    spade_upgrade_cost = Resources(workers=2, coins=1, priests=1)

    @classmethod
    def handle_spade(cls, player: Player):
        player.gain(points=1)
        return super().handle_spade(player)


class Cultists(Faction):
    name = "Cultists"
    starting_cult = CultProgress(
        fire=1,
        earth=1,
    )
    colour = FactionColour.BROWN
    terrain = Terrain.FIELD

    stronghold_cost = Resources(workers=4, coins=8)
    stronghold_once_off_action = CultistsStrongholdBonusAction

    sanctuary_cost = Resources(workers=4, coins=8)

    neighbouring_dwelling_action = CultistsNeighbourBonusAction


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

    @classmethod
    def handle_end_of_round(cls, player: Player):
        # TODO: check for bridges
        return super().handle_end_of_round(player)


class Dwarves(Faction):
    name = "Dwarves"
    starting_cult = CultProgress(
        earth=2,
    )
    colour = FactionColour.GREY
    terrain = Terrain.MOUNTAIN

    basic_actions = [DwarvesBasicAction]

    trading_house_incomes = (
        Resources(power=1, coins=3),
        Resources(power=1, coins=2),
        Resources(power=2, coins=2),
        Resources(power=2, coins=3),
    )

    stronghold_cost = Resources(workers=4, coins=8)
    stronghold_action = DwarvesStrongholdAction

    sanctuary_cost = Resources(workers=4, coins=8)

    shipping_disabled = True


class Alchemists(Faction):
    name = "Alchemists"
    starting_cult = CultProgress(
        fire=1,
        water=1,
    )
    colour = FactionColour.BLACK
    terrain = Terrain.SWAMP

    basic_actions = []

    trading_house_incomes = (
        Resources(power=1, coins=2),
        Resources(power=1, coins=2),
        Resources(power=1, coins=3),
        Resources(power=1, coins=4),
    )

    stronghold_income = Resources(coins=6)

    @classmethod
    def handle_spade(cls, player: Player):
        if player.has_building(Building.STRONGHOLD):
            player.gain(power=2)
        return super().handle_spade(player)


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

    stronghold_once_off_action = DarklingsStrongholdBonusAction

    sanctuary_cost = Resources(workers=4, coins=10)
    sanctuary_income = Resources(priests=2)

    spade_max_upgrades = 0
