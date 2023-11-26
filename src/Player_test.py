import pytest
from Faction import ChaosMagicians
from Player import Player
from Resources import Resources
from errors import InsufficientResourcesError


class TestPlayer:
    def test_resource_management(self):
        # Setup
        p = Player(faction=ChaosMagicians)
        p.gain(Resources(workers=1, priests=2))

        # Spend all resources
        p.spend(Resources(workers=5, coins=10, priests=1))
        p.spend(Resources(coins=5, priests=1))

        # Check we can't spend any more
        with pytest.raises(InsufficientResourcesError):
            p.spend(Resources(workers=1))
        with pytest.raises(InsufficientResourcesError):
            p.spend(Resources(coins=1))
        with pytest.raises(InsufficientResourcesError):
            p.spend(Resources(priests=1))
