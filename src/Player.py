from Cult import Cult
from CultProgress import CultProgress
from Faction import Faction
from Resources import Resources


POWER_BONUSES = [
    (2, 1),
    (4, 2),
    (6, 2),
    (10, 3),
]


class Player:
    resources: Resources
    faction: Faction
    cult_progress: CultProgress
    shipping_level: int
    spades_level: int

    def __init__(self, faction: Faction) -> None:
        self.faction = faction

        self.cult_progress = faction.starting_cult
        self.resources = faction.starting_resources
        self.shipping_level = (
            0 if faction.disable_shipping else faction.starting_shipping
        )
        self.spades_level = 0

    def gain(self, resources: Resources) -> None:
        self.resources = self.resources + resources

    def advance_in_cult(self, cult: Cult, points: int) -> None:
        # Calculate power bonus
        cult_name = cult.name.lower()
        initial_cult_score = self.cult_progress.__getattribute__(cult_name)
        new_cult_score = initial_cult_score + points
        total_power_bonus = 0
        for cult_level, power_bonus in POWER_BONUSES:
            if initial_cult_score <= cult_level and new_cult_score > cult_level:
                total_power_bonus += power_bonus
        self.gain(Resources(power=total_power_bonus))

        # Add to cult progress
        progress = CultProgress()
        progress.__setattr__(cult_name, points)
        self.cult_progress = self.cult_progress + progress
