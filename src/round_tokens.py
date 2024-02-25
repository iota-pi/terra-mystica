from AbstractResources import AbstractResources
from Building import Building
from CultProgress import CultProgress
from Resources import Resources
from RoundToken import RoundToken


ROUND_TOKENS = [
    RoundToken(
        build_bonus_condition=AbstractResources(spades_credit=1),
        build_bonus_points=2,
        cult_condition=CultProgress(earth=1),
        cult_reward=Resources(coins=1),
    ),
    RoundToken(
        build_bonus_condition=Building.DWELLING,
        build_bonus_points=2,
        cult_condition=CultProgress(fire=4),
        cult_reward=Resources(power=4),
    ),
    RoundToken(
        build_bonus_condition=Building.DWELLING,
        build_bonus_points=2,
        cult_condition=CultProgress(water=4),
        cult_reward=Resources(priests=1),
    ),
    RoundToken(
        build_bonus_condition=Building.TRADING_HOUSE,
        build_bonus_points=3,
        cult_condition=CultProgress(air=4),
        cult_reward=AbstractResources(spades_credit=1),
    ),
    RoundToken(
        build_bonus_condition=Building.TRADING_HOUSE,
        build_bonus_points=3,
        cult_condition=CultProgress(water=4),
        cult_reward=AbstractResources(spades_credit=1),
    ),
    RoundToken(
        build_bonus_condition=(Building.STRONGHOLD, Building.SANCTUARY),
        build_bonus_points=5,
        cult_condition=CultProgress(fire=2),
        cult_reward=Resources(workers=1),
    ),
    RoundToken(
        build_bonus_condition=(Building.STRONGHOLD, Building.SANCTUARY),
        build_bonus_points=5,
        cult_condition=CultProgress(air=2),
        cult_reward=Resources(workers=1),
    ),
    RoundToken(
        build_bonus_condition=AbstractResources(towns=1),
        build_bonus_points=5,
        cult_condition=CultProgress(earth=4),
        cult_reward=AbstractResources(spades_credit=1),
    ),
]
