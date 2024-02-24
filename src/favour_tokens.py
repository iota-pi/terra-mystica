from AbstractResources import AbstractResources
from Action import CultAction
from Building import Building
from Resources import Resources
from FavourToken import FavourToken
from Cult import Cult


FAVOUR_TOKENS = [
    FavourToken(
        cult_bonus=Cult.FIRE,
        cult_value=1,
        income=Resources(coins=3),
    ),
    FavourToken(
        cult_bonus=Cult.WATER,
        cult_value=1,
        build_bonus_condition=Building.TRADING_HOUSE,
        build_bonus_points=3,
    ),
    FavourToken(
        cult_bonus=Cult.EARTH,
        cult_value=1,
        build_bonus_condition=Building.DWELLING,
        build_bonus_points=2,
    ),
    FavourToken(  # needs the non-linear point reward looked at
        cult_bonus=Cult.AIR,
        cult_value=1,
        pass_bonus_condition=Building.TRADING_HOUSE,
        pass_bonus_points=1,  # 1 point per trading house +1 if you only have 1 or 2 trading houses
    ),
    FavourToken(
        cult_bonus=Cult.FIRE,
        cult_value=2,
        abstract_resources=AbstractResources(town_discount=True),
    ),
    FavourToken(
        cult_bonus=Cult.WATER,
        cult_value=2,
        action=CultAction,
    ),
    FavourToken(
        cult_bonus=Cult.EARTH,
        cult_value=2,
        income=(Resources(power=1), Resources(workers=1)),
    ),
    FavourToken(
        cult_bonus=Cult.AIR,
        cult_value=2,
        income=Resources(power=4),
    ),
    FavourToken(
        cult_bonus=Cult.FIRE,
        cult_value=3,
        available=1,
    ),
    FavourToken(
        cult_bonus=Cult.WATER,
        cult_value=3,
        available=1,
    ),
    FavourToken(
        cult_bonus=Cult.EARTH,
        cult_value=3,
        available=1,
    ),
    FavourToken(
        cult_bonus=Cult.AIR,
        cult_value=3,
        available=1,
    ),
]
