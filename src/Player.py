from dataclasses import dataclass
from Building import Building
from Cult import Cult
from CultProgress import CultProgress
from Faction import Alchemists, Faction
from Resources import Resources, ResourcesType
from Terrain import Terrain, calculate_spade_cost
from Tile import Tile
from PassToken import PassToken
from FavourToken import FavourToken
from TownToken import TownToken
from RoundToken import RoundToken

from errors import GameplayError, InsufficientResourcesError, InvalidActionError
from typing import Set, Type, Unpack


POWER_BONUSES = [
    (2, 1),
    (4, 2),
    (6, 2),
    (10, 3),
]


@dataclass
class Token:
    Pass: PassToken | None = None
    Favour: Set[FavourToken] | None = None
    Town: Set[TownToken] | None = None
    Round: RoundToken | None = None


class Player:
    tokens: Set[Token] = set()
    resources: Resources
    faction: Type[Faction]
    cult_progress: CultProgress
    shipping_level: int
    spades_level: int
    building_locations: Set[Tile]
    turns_credit: int = 0

    def __init__(self, faction: Type[Faction]) -> None:
        self.faction = faction

        self.cult_progress = faction.starting_cult
        self.resources = faction.starting_resources
        self.shipping_level = (
            0 if faction.shipping_disabled else faction.shipping_start_level
        )
        self.spades_level = 3

    @property
    def score(self):
        return self.resources.points

    def gain(
        self,
        resources: Resources = Resources(),
        **kwargs: Unpack[ResourcesType],
    ) -> None:
        new_resources = self.resources
        if resources:
            new_resources += resources
        if kwargs:
            new_resources += Resources(**kwargs)

        if (
            new_resources.coins < 0
            or new_resources.power < 0
            or new_resources.priests < 0
            or new_resources.workers < 0
        ):
            raise InsufficientResourcesError()

        self.resources = new_resources

    def spend(
        self,
        resources: Resources = Resources(),
        **kwargs: Unpack[ResourcesType],
    ) -> None:
        to_spend = -resources
        if kwargs:
            to_spend -= Resources(**kwargs)
        self.gain(to_spend)

    def advance_in_cult(self, cult: Cult, points: int) -> None:
        # Calculate power bonus
        cult_name = cult.name.lower()
        initial_cult_score = self.cult_progress.__getattribute__(cult_name)
        new_cult_score = initial_cult_score + points
        total_power_bonus = 0
        for cult_level, power_bonus in POWER_BONUSES:
            if initial_cult_score <= cult_level and new_cult_score > cult_level:
                total_power_bonus += power_bonus
        self.gain(power=total_power_bonus)

        # Add to cult progress
        progress = CultProgress()
        progress.__setattr__(cult_name, points)
        self.cult_progress = self.cult_progress + progress

    def upgrade_spade_level(self) -> None:
        if self.spades_level <= 1:
            raise InvalidActionError("Spades track is already at max")
        self.spend(self.faction.spade_upgrade_cost)
        self.spades_level -= 1

    def upgrade_shipping_level(self) -> None:
        if self.shipping_level >= self.faction.shipping_max_level:
            raise GameplayError(
                f"Shipping level cannot exceed maximum of {self.shipping_level} "
                f"for {self.faction.__name__}"
            )
        self.spend(self.faction.shipping_upgrade_cost)
        self.shipping_level += 1

    def terraform(self, location: Tile, terrain_goal: Terrain) -> None:
        spades_required = calculate_spade_cost(
            location.terrain,
            terrain_goal,
        )
        worker_cost = spades_required * self.spades_level
        self.spend(Resources(workers=worker_cost))
        location.terraform(terrain_goal)

    def build(self, location: Tile, building: Building) -> None:
        # TODO: check player hasn't exceeded maximum building numbers
        building_cost = self.faction.get_building_cost(building)
        self.spend(building_cost)
        location.build(new_building=building, faction=self.faction)
        self.building_locations.add(location)
        if building is Building.TEMPLE or building is Building.SANCTUARY:
            self.gain_token(self.choose_favour_token())

    def has_building(self, building: Building) -> bool:
        for tile in self.building_locations:
            if tile.building == building:
                return True

        return False

    def trigger_spades(self, spade_count: int):
        if self.faction == Alchemists and self.has_building(Building.STRONGHOLD):
            self.gain(power=2 * spade_count)
        self.gain(points=self.faction.spade_bonus_points)
        
    def gain_token(self, newToken: Token):
        if newToken == Token():
            return
        self.tokens.add(newToken)
        
    def loose_token(self, remove: Token):
        if remove is Token():
            return
        if remove not in self.tokens:
            raise(InvalidActionError("You cannot remove a token you do not have."))
        else:
            self.tokens.remove(remove)

    def choose_favour_token(self):
        # TODO: Select a favour token that is available and I don't own
        return Token()