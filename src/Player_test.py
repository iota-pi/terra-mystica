import pytest
from Faction import ChaosMagicians
from Player import Player
from errors import InsufficientResourcesError


class TestPlayer:
    def test_resource_management(self):
        # Setup
        p = Player(faction=ChaosMagicians)
        p.gain(workers=1, priests=2)

        # Spend all resources
        p.spend(workers=5, coins=10, priests=1)
        p.spend(coins=5, priests=1)

        # Check we can't spend any more
        with pytest.raises(InsufficientResourcesError):
            p.spend(workers=1)
        with pytest.raises(InsufficientResourcesError):
            p.spend(coins=1)
        with pytest.raises(InsufficientResourcesError):
            p.spend(priests=1)
