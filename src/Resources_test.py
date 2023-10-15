from Resources import Resources


class TestResources:
    def test_add(self):
        a = Resources(workers=1, coins=1)
        b = Resources(workers=2, power=3)
        result = a + b

        assert result.workers == 3
        assert result.power == 3
        assert result.coins == 1
        assert result.priests == 0

    def test_sub(self):
        a = Resources(workers=3, coins=15)
        b = Resources(workers=2, coins=3)
        result = a - b

        assert result.workers == 1
        assert result.coins == 12
        assert result.power == 0
        assert result.priests == 0
