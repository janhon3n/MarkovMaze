from abc import ABC, abstractmethod
from State import State

class SimulationListener(ABC):

    @abstractmethod
    def update(self, state: State):
        pass

    @abstractmethod
    def simulationOver(self, state: State):
        pass