from Resources import Resources
from CultProgress import CultProgress
from TownToken import TownToken


TOWN_TOKENS = [
    TownToken(
        points=5,
        resource_bonus=Resources(coins=6),
    ),
    TownToken(
        points=6,
        resource_bonus=Resources(power=6),
    ),
    TownToken(
        points=7,
        resource_bonus=Resources(workers=2),
    ),
    TownToken(
        points=8,
        cult_reward=CultProgress(fire=1,water=1,earth=1,air=1),
    ),
    TownToken(
        points=9,
        resource_bonus=Resources(priests=1),
    ),
]
