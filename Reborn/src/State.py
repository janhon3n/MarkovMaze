from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def equals(self, state: State) -> bool:
        pass

    @abstractmethod
    def copy(self) -> State:
        pass


class StateException(Exception):
    pass