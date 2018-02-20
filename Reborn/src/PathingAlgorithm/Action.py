from abc import ABC, abstractmethod
from State import State
from Agent import Agent

class Action(ABC):

    initiator = None

    def __init__(self, initiator: Agent):
        self.initiator = initiator

    @abstractmethod
    def execute(self, state: State) -> State:
        pass