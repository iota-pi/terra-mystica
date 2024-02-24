from abc import ABC
from typing import TYPE_CHECKING

from AbstractResources import AbstractResources
from Building import Building
from Cult import Cult
from Resources import Resources
from Terrain import Terrain
from errors import GameplayError, InvalidActionError

if TYPE_CHECKING:
    from Board import Board
    from Player import Player
    from Tile import Tile


class Action(ABC):
    _time: int = 1
    _cost: Resources = Resources()
    _reward: Resources | AbstractResources = Resources()

    def activate(self, board: "Board", player: "Player"):
        if player.turns_credit <= 0:
            raise GameplayError("Player is out of actions")
        player.turns_credit -= self._time
        if isinstance(self._reward, Resources):
            player.gain(self._reward - self._cost)
        # TODO: handle abstract resources


class BonusAction(Action):
    _time = 0


class LocationSpecificAction(Action):
    _location: "Tile | None" = None

    @property
    def location(self) -> "Tile":
        if self._location is None:
            raise InvalidActionError(
                f"Location must be set for type {self.__class__.__name__}"
            )
        return self._location

    @location.setter
    def location(self, tile: "Tile") -> None:
        self._location = tile


class FlyingAction(LocationSpecificAction):
    _distance = 1

    def activate(self, board: "Board", player: "Player"):
        adjacent = board.get_indirectly_adj(
            self.location,
            self._distance,
            flying=True,
        )
        dwelling_in_range = any(
            tile.building is not None and tile.faction == player.faction
            for tile in adjacent
        )
        if not dwelling_in_range:
            raise InvalidActionError(
                "Cannot build on selected tile; "
                "too far from the nearest building of the same player"
            )

        player.build(self.location, Building.DWELLING)
        return super().activate(board, player)


class CultAction(Action):
    _value: int = 1
    _cult: Cult | None = None

    @property
    def cult(self) -> Cult:
        if self._cult is None:
            raise InvalidActionError(
                f"Cult must be set for type {self.__class__.__name__}"
            )
        return self._cult

    @cult.setter
    def cult(self, cult: Cult) -> None:
        self._cult = cult

    def activate(self, board: "Board", player: "Player") -> None:
        player.advance_in_cult(self.cult, self._value)
        return super().activate(board, player)


class SharedAction(Action):
    _available = True

    @property
    def available(self):
        return self._available

    def activate(self, board: "Board", player: "Player") -> None:
        self._available = False
        return super().activate(board, player)

    def reset(self) -> None:
        self._available = True


class AnyTimeAction(Action):
    _time = 0


# Standard any-time actions
class AnyTimeCoinAction(AnyTimeAction):
    _cost = Resources(power=1)
    _reward = Resources(coins=1)


class AnyTimeWorkerAction(AnyTimeAction):
    _cost = Resources(power=3)
    _reward = Resources(workers=1)


class AnyTimePriestAction(AnyTimeAction):
    _cost = Resources(power=5)
    _reward = Resources(priests=1)


class AnyTimeDowngradePriest(AnyTimeAction):
    _cost = Resources(priests=1)
    _reward = Resources(workers=1)


class AnyTimeDowngradeWorker(AnyTimeAction):
    _cost = Resources(workers=1)
    _reward = Resources(coins=1)


# Standard turn actions
class PlayPriestAction(Action):
    _cost = Resources(priests=1)


class FirePriestAction(PlayPriestAction):
    def activate(self, board: "Board", player: "Player") -> None:
        board.play_priest(player=player, cult=Cult.FIRE)
        return super().activate(board, player)


class EarthPriestAction(PlayPriestAction):
    def activate(self, board: "Board", player: "Player") -> None:
        board.play_priest(player=player, cult=Cult.EARTH)
        return super().activate(board, player)


class WaterPriestAction(PlayPriestAction):
    def activate(self, board: "Board", player: "Player") -> None:
        board.play_priest(player=player, cult=Cult.WATER)
        return super().activate(board, player)


class AirPriestAction(PlayPriestAction):
    def activate(self, board: "Board", player: "Player") -> None:
        board.play_priest(player=player, cult=Cult.AIR)
        return super().activate(board, player)


class TerraformAndBuildAction(LocationSpecificAction):
    _terrain_goal: Terrain | None = None
    _building_goal: Building | None = None

    @property
    def terrain_goal(self) -> Terrain:
        if self._terrain_goal is None:
            raise InvalidActionError(
                f"Terrain goal must be set for type {self.__class__.__name__}"
            )
        return self._terrain_goal

    @terrain_goal.setter
    def terrain_goal(self, terrain_goal: Terrain) -> None:
        self._terrain_goal = terrain_goal

    @property
    def building_goal(self) -> Building:
        if self._building_goal is None:
            raise InvalidActionError(
                f"Building goal must be set for type {self.__class__.__name__}"
            )
        return self._building_goal

    @building_goal.setter
    def building_goal(self, building_goal: Building) -> None:
        self._building_goal = building_goal

    def activate(self, board: "Board", player: "Player") -> None:
        player.terraform(self.location, self.terrain_goal)
        player.build(location=self.location, building=self.building_goal)
        return super().activate(board, player)


# Action token actions
class SingleSpadeAction(Action):
    _reward = AbstractResources(spades_credit=1)


# Shared board actions
class BridgeAction(SharedAction):
    _cost = Resources(power=3)
    _reward = AbstractResources(bridge_credit=1)


class PriestAction(SharedAction):
    _cost = Resources(power=3)
    _reward = Resources(priests=1)


class WorkersAction(SharedAction):
    _cost = Resources(power=4)
    _reward = Resources(workers=2)


class CoinsAction(SharedAction):
    _cost = Resources(power=4)
    _reward = Resources(coins=7)


class SpadeAction(SharedAction):
    _cost = Resources(power=4)
    _reward = AbstractResources(spades_credit=1)


class DoubleSpadeAction(SharedAction):
    _cost = Resources(power=6)
    _reward = AbstractResources(spades_credit=2)


# Cult-specific actions
class ChaosMagicianStrongholdAction(Action):
    _time = -1


class GiantsStrongholdAction(LocationSpecificAction):
    _reward = AbstractResources(spades_credit=2)


class WitchesStrongholdAction(LocationSpecificAction):
    def activate(self, board: "Board", player: "Player") -> None:
        player.build(location=self.location, building=Building.DWELLING)

        return super().activate(board, player)


class AurenStrongholdAction(CultAction):
    _value = 2


class SwarmlingsStrongholdAction(LocationSpecificAction):
    def activate(self, board: "Board", player: "Player") -> None:
        player.build(location=self.location, building=Building.TRADING_HOUSE)

        return super().activate(board, player)


class MermaidStrongholdBonusAction(BonusAction):
    def activate(self, board: "Board", player: "Player"):
        player.upgrade_shipping_level()
        return super().activate(board, player)


class FakirsBasicAction(FlyingAction):
    _cost = Resources(priests=1)
    _reward = Resources(points=4)


class FakirsStrongholdAction(FlyingAction):
    _cost = Resources(priests=1)
    _reward = Resources(points=4)
    _distance = 2


class NomadsStrongholdAction(LocationSpecificAction):
    def activate(self, board: "Board", player: "Player"):
        self.location.terraform(player.faction.terrain)
        return super().activate(board, player)


class HalflingsStrongholdBonusAction(BonusAction):
    _reward = AbstractResources(spades_credit=3)


class CultistsStrongholdBonusAction(BonusAction):
    _reward = Resources(points=7)


class CultistsNeighbourBonusAction(CultAction, BonusAction):
    pass


class EngineersBasicAction(Action):
    _cost = Resources(workers=2)
    _reward = AbstractResources(bridge_credit=1)


class DwarvesBasicAction(FlyingAction):
    _cost = Resources(workers=2)
    _reward = Resources(points=4)


class DwarvesStrongholdAction(FlyingAction):
    _cost = Resources(workers=1)
    _reward = Resources(points=4)


class AlchemistsCoinBasicAction(BonusAction):
    _cost = Resources(points=1)
    _reward = Resources(coins=1)


class AlchemistsPointBasicAction(BonusAction):
    _cost = Resources(coins=2)
    _reward = Resources(points=1)


class DarklingsStrongholdBonusAction(BonusAction):
    def activate(self, board: "Board", player: "Player"):
        workers_to_swap = min(player.resources.workers, 3)
        player.gain(workers=-workers_to_swap, priests=workers_to_swap)
        return super().activate(board, player)
