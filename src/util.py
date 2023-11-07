from dataclasses import dataclass


def _add_resources[T](a: T, b: T) -> T:
    if type(a) != type(b) or not isinstance(a, ArithmeticEnabledDataclass):
        raise NotImplementedError()
    result = {}
    for slot in a.__slots__:
        result[slot] = a.__getattribute__(slot) + b.__getattribute__(slot)
    return type(a)(**result)


def _sub_resources[T](a: T, b: T) -> T:
    if type(a) != type(b) or not isinstance(a, ArithmeticEnabledDataclass):
        raise NotImplementedError()
    result = {}
    for slot in a.__slots__:
        result[slot] = a.__getattribute__(slot) - b.__getattribute__(slot)
    return type(a)(**result)


@dataclass(frozen=True, slots=True)
class ArithmeticEnabledDataclass:
    __add__ = __radd__ = _add_resources
    __sub__ = __rsub__ = _sub_resources

    def __neg__(self):
        return _sub_resources(type(self)(), self)
