from AbstractResources import AbstractResources
from Building import Building
from CultProgress import CultProgress
from Resources import Resources
from RoundToken import RoundToken


ROUND_TOKENS = [
    RoundToken(
        bonus_condition=AbstractResources(spades=1),
        bonus_points=2,
        cult_condition=CultProgress(earth=1),
        cult_reward=Resources(coins=1),
    ),
    RoundToken(
        bonus_condition=Building.DWELLING,
        bonus_points=2,
        cult_condition=CultProgress(fire=4),
        cult_reward=Resources(power=4),
    ),
    RoundToken(
        bonus_condition=Building.DWELLING,
        bonus_points=2,
        cult_condition=CultProgress(water=4),
        cult_reward=Resources(priests=1),
    ),
    RoundToken(
        bonus_condition=Building.TRADING_HOUSE,
        bonus_points=3,
        cult_condition=CultProgress(air=4),
        cult_reward=AbstractResources(spades=1),
    ),
    RoundToken(
        bonus_condition=Building.TRADING_HOUSE,
        bonus_points=3,
        cult_condition=CultProgress(water=4),
        cult_reward=AbstractResources(spades=1),
    ),
    RoundToken(
        bonus_condition=(Building.STRONGHOLD, Building.SANCTUARY),
        bonus_points=5,
        cult_condition=CultProgress(fire=2),
        cult_reward=Resources(workers=1),
    ),
    RoundToken(
        bonus_condition=(Building.STRONGHOLD, Building.SANCTUARY),
        bonus_points=5,
        cult_condition=CultProgress(air=2),
        cult_reward=Resources(workers=1),
    ),
    RoundToken(
        bonus_condition=AbstractResources(towns=1),
        bonus_points=5,
        cult_condition=CultProgress(earth=4),
        cult_reward=AbstractResources(spades=1),
    ),
]
