from errors import InsufficientResourcesError


class Power(int):
    _bowl_1: int
    _bowl_2: int
    _bowl_3: int

    def __init__(self, initial: 'int | Power' = 0) -> None:
        self._bowl_1 = initial.max_power if type(initial) == Power else 12
        self._bowl_2 = 0
        self._bowl_3 = 0
        self._gain(initial)

    def _gain(self, power: 'int | Power'):
        if type(power) != int:
            power = int(power)

        from_bowl_1 = min(self._bowl_1, power)
        self._bowl_2 += from_bowl_1
        self._bowl_1 -= from_bowl_1
        power -= from_bowl_1

        from_bowl_2 = min(self._bowl_2, power)
        self._bowl_3 += from_bowl_2
        self._bowl_2 -= from_bowl_2
        power -= from_bowl_2

    def _spend(self, power: int):
        if self._bowl_3 < power:
            raise InsufficientResourcesError("Not enough power in bowl 3")
        self._bowl_3 -= power
        self._bowl_1 += power

    def sacrifice(self, amount: int = 1) -> None:
        if self._bowl_2 < amount * 2:
            raise InsufficientResourcesError("Not enough power in bowl 2 to sacrifice")
        self._bowl_2 -= amount * 2
        self._bowl_3 += amount

    def get_max_gain(self) -> int:
        return self._bowl_1 * 2 + self._bowl_2

    @property
    def available(self) -> int:
        return self._bowl_3

    @property
    def max_power(self) -> int:
        return self._bowl_1 + self._bowl_2 + self._bowl_3

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        bowls = [self._bowl_1, self._bowl_2, self._bowl_3]
        bowls_str = ', '.join(str(b) for b in bowls)
        return f"Power({bowls_str})"

    def __int__(self) -> int:
        return self._bowl_2 + self._bowl_3 * 2

    def __lt__(self, __value: 'int | Power') -> bool:
        return self.available < int(__value)

    def __add__(self, __value: int) -> 'Power':
        p = Power(self)
        p._gain(__value)
        return p

    def __sub__(self, __value: int) -> 'Power':
        p = Power(self)
        p._spend(__value)
        return p
