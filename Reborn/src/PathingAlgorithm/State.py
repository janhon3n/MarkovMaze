from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def equals(self, state) -> bool:
        pass

    @abstractmethod
    def copy(self):
        pass


class StateException(Exception):
    pass