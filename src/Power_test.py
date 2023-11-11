import pytest
from Power import Power
from errors import InsufficientResourcesError


class TestPower:
    def test_add(self):
        a = Power(5)
        b = Power(10)
        c = a + b
        assert c.available == 3

    def test_sub(self):
        a = Power(16)
        b = Power(4)
        c = a - b
        assert c.available == 0

    @pytest.mark.parametrize(
        'power,sacrifice',
        [
            (0, 1),
            (1, 1),
            (2, 2),
            (9, 5),
            (14, 6),
        ],
    )
    def test_invalid_sacrifice(self, power: int, sacrifice: int):
        a = Power(power)
        with pytest.raises(InsufficientResourcesError):
            a.sacrifice(sacrifice)

    @pytest.mark.parametrize(
        'power,sacrifice,available',
        [
            (0, 0, 0),
            (2, 1, 1),
            (11, 5, 5),
        ],
    )
    def test_valid_sacrifice(self, power: int, sacrifice: int, available: int):
        a = Power(power)
        a.sacrifice(sacrifice)
        assert a.available == available

    def test_arithmetic_with_sacrificed_power(self):
        a = Power(12)
        a.sacrifice(3)
        assert a.available == 3
        assert a.get_max_gain() == 6

        c = a + 12
        assert c.available == 9
        assert c.max_power == 9

        d = c - 4
        assert d.available == 5
        assert d.get_max_gain() == 8
        assert d.max_power == 9
