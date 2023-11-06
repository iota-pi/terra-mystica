from abc import ABC

from AbstractResources import AbstractResources
from Board import Board
from Building import Building
from Cult import Cult
from Player import Player
from Resources import Resources
from Terrain import Terrain
from Tile import Tile

from errors import InvalidActionError


class Action(ABC):
    time: int = 1
    cost: Resources = Resources()
    reward: Resources = Resources()

    def _validate_action(self) -> None:
        pass

    def _actuate(self, board: Board, player: Player) -> None:
        player.gain(self.reward - self.cost)

    def activate(self, board: Board, player: Player):
        self._validate_action()
        self._actuate(board, player)


class LocationSpecificAction(Action):
    _location: Tile | None = None

    @property
    def location(self) -> Tile:
        if self._location is None:
            raise InvalidActionError()
        return self._location

    @location.setter
    def location(self, tile: Tile) -> None:
        self._location = tile


class SharedAction(Action):
    available = True

    def _actuate(self, board: Board, player: Player) -> None:
        self.available = False
        return super()._actuate(board, player)

    def reset(self) -> None:
        self.available = True


# Standard any-time actions
class AnyTimeAction(Action):
    time = 0


class AnyTimeCoinAction(AnyTimeAction):
    cost = Resources(power=1)
    result = Resources(coins=1)


class AnyTimeWorkerAction(AnyTimeAction):
    cost = Resources(power=3)
    result = Resources(workers=1)


class AnyTimePriestAction(AnyTimeAction):
    cost = Resources(power=5)
    result = Resources(priests=1)


# Standard turn actions
class PlayPriestAction(Action):
    cost = Resources(priests=1)


class FirePriestAction(PlayPriestAction):
    def _actuate(self, board: Board, player: Player) -> None:
        board.play_priest(player=player, cult=Cult.FIRE)
        return super()._actuate(board, player)


class EarthPriestAction(PlayPriestAction):
    def _actuate(self, board: Board, player: Player) -> None:
        board.play_priest(player=player, cult=Cult.EARTH)
        return super()._actuate(board, player)


class WaterPriestAction(PlayPriestAction):
    def _actuate(self, board: Board, player: Player) -> None:
        board.play_priest(player=player, cult=Cult.WATER)
        return super()._actuate(board, player)


class AirPriestAction(PlayPriestAction):
    def _actuate(self, board: Board, player: Player) -> None:
        board.play_priest(player=player, cult=Cult.AIR)
        return super()._actuate(board, player)


class TerraformAndBuildAction(LocationSpecificAction):
    terrain_goal: Terrain | None = None
    building_goal: Building | None = None

    def set_terrain_goal(self, terrain: Terrain) -> None:
        self.terrain_goal = terrain

    def set_building_goal(self, building: Building) -> None:
        self.building_goal = building

    def _validate_action(self):
        if self.terrain_goal is None and self.building_goal is None:
            raise InvalidActionError()

        return super()._validate_action()

    def _actuate(self, board: Board, player: Player) -> None:
        if self.terrain_goal is not None:
            player.terraform(self.location, self.terrain_goal)

        if self.building_goal is not None:
            player.build(location=self.location, building=self.building_goal)

        return super()._actuate(board, player)


# Shared board actions
class BridgeAction(SharedAction):
    cost = Resources(power=3)
    result = AbstractResources(bridge_credit=1)


class PriestAction(SharedAction):
    cost = Resources(power=3)
    result = Resources(priests=1)


class WorkersAction(SharedAction):
    cost = Resources(power=4)
    result = Resources(workers=2)


class CoinsAction(SharedAction):
    cost = Resources(power=4)
    result = Resources(coins=7)


class SpadeAction(SharedAction):
    cost = Resources(power=4)
    result = AbstractResources(spades_credit=1)


class DoubleSpadeAction(SharedAction):
    cost = Resources(power=6)
    result = AbstractResources(spades_credit=2)


# Cult-specific actions
class WitchesAction(Action):
    result = AbstractResources(dwelling_credit=1)


# TODO
