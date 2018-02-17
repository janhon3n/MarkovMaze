from abc import ABC, abstractmethod
from State import State
from Action import Action

class Enviroment(ABC):

    agents = None
    state = None

    def __init__(self, initialState: State):
        self.agents = []
        self.state = initialState

    @abstractmethod
    def executeAction(self, action: Action):
        pass