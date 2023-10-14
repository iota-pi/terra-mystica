from CultProgress import CultProgress
from Faction import Faction
from Resources import Resources


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
