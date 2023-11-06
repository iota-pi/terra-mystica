from Building import Building
from Cult import Cult
from CultProgress import CultProgress
from Faction import Faction
from Resources import Resources
from Terrain import Terrain, calculate_spade_cost
from Tile import Tile

from errors import InsufficientResourcesError, InvalidActionError
from typing import Set


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
    building_locations: Set[Tile]

    def __init__(self, faction: Faction) -> None:
        self.faction = faction

        self.cult_progress = faction.starting_cult
        self.resources = faction.starting_resources
        self.shipping_level = (
            0 if faction.disable_shipping else faction.starting_shipping
        )
        self.spades_level = 3

    def gain(self, resources: Resources) -> None:
        self.resources = self.resources + resources

        if (
            self.resources.coins < 0
            or self.resources.power < 0
            or self.resources.priests < 0
            or self.resources.workers < 0
        ):
            raise InsufficientResourcesError()

    def spend(self, resources: Resources) -> None:
        self.gain(-resources)

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

    def upgrade_spade_track(self) -> None:
        if self.spades_level <= 1:
            raise InvalidActionError("Spades track is already at max")
        self.spend(self.faction.spade_upgrade_cost)
        self.spades_level -= 1

    def terraform(self, location: Tile, terrain_goal: Terrain) -> None:
        spade_cost = calculate_spade_cost(
            location.terrain,
            terrain_goal,
        )
        worker_cost = spade_cost * self.spades_level
        self.spend(Resources(workers=worker_cost))
        location.terraform(terrain_goal)

    def build(self, location: Tile, building: Building) -> None:
        building_cost = self.faction.get_building_cost(building)
        self.spend(building_cost)
        location.build(building=building, faction=self.faction)
        self.building_locations.add(location)
