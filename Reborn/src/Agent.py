from abc import ABC, abstractmethod
from Action import Action
from Enviroment import Enviroment

class Agent(ABC):
    
    enviroment = None
    actions = None

    def __init__(self, enviroment: Enviroment):
        self.enviroment = enviroment
        self.actions = []

    @abstractmethod
    def makeDecision(self) -> Action:
        return
