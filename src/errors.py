class GameplayError(RuntimeError):
    pass


class InvalidActionError(GameplayError):
    pass


class InsufficientResourcesError(GameplayError):
    pass
