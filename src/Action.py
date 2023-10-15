from abc import ABC

from AbstractResources import AbstractResources
from Board import Board
from Cult import Cult
from Resources import Resources
from Player import Player


class Action(ABC):
    time: int = 1
    cost: Resources = Resources()
    reward: Resources = Resources()

    def activate(self, board: Board, player: Player) -> None:
        player.gain(self.reward - self.cost)


class SharedAction(Action):
    available = True

    def activate(self, board: Board, player: Player) -> None:
        self.available = False
        return super().activate(board, player)

    def reset(self) -> None:
        self.available = True


# Standard any-time actions
class AnyTimeAction(Action):
    time = 0


class AnyTimeCoinAction(Action):
    cost = Resources(power=1)
    result = Resources(coins=1)


class AnyTimeWorkerAction(Action):
    cost = Resources(power=3)
    result = Resources(workers=1)


class AnyTimePriestAction(Action):
    cost = Resources(power=5)
    result = Resources(priests=1)


# Standard turn actions
class PlayPriestAction(Action):
    cost = Resources(priests=1)


class FirePriestAction(PlayPriestAction):
    def activate(self, board: Board, player: Player) -> None:
        board.play_priest(player=player, cult=Cult.FIRE)
        return super().activate(board, player)


class EarthPriestAction(PlayPriestAction):
    def activate(self, board: Board, player: Player) -> None:
        board.play_priest(player=player, cult=Cult.EARTH)
        return super().activate(board, player)


class WaterPriestAction(PlayPriestAction):
    def activate(self, board: Board, player: Player) -> None:
        board.play_priest(player=player, cult=Cult.WATER)
        return super().activate(board, player)


class AirPriestAction(PlayPriestAction):
    def activate(self, board: Board, player: Player) -> None:
        board.play_priest(player=player, cult=Cult.AIR)
        return super().activate(board, player)


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
