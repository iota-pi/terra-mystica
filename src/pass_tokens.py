from AbstractResources import AbstractResources
from Action import CultAction, SingleSpadeAction
from Building import Building
from Resources import Resources
from PassToken import PassToken


PASS_TOKENS = [
    PassToken(
        bonus_condition=Building.DWELLING,
        bonus_points=1,
        income=Resources(coins=2),
    ),
    PassToken(
        bonus_condition=Building.TRADING_HOUSE,
        bonus_points=2,
        income=Resources(workers=1),
    ),
    PassToken(
        bonus_condition=(Building.STRONGHOLD, Building.SANCTUARY),
        bonus_points=4,
        income=Resources(workers=2),
    ),
    PassToken(
        income=Resources(workers=1, power=3),
    ),
    PassToken(
        income=Resources(power=3),
        abstract_resources=AbstractResources(shipping_bonus=1),
    ),
    PassToken(
        income=Resources(priests=1),
    ),
    PassToken(
        income=Resources(coins=6),
    ),
    PassToken(
        income=Resources(coins=4),
        action=CultAction,
    ),
    PassToken(
        income=Resources(coins=2),
        action=SingleSpadeAction,
    ),
]
