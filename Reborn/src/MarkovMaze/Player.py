from Agent import Agent
from State import Position
from GameObject import SolidObject

class Player(Agent, SolidObject):
    name = "Dumb player"
    points = 0

      def __init__(self, enviroment: Enviroment):
            super().__init__(enviroment)

        # Override this to create player logic
      def makeDecision(self, state: State) -> Action:
            return MoveAction('RIGHT')

                    
class HumanPlayer(Player):
    gameWindow = None

    def __init__(self, stage, gameWindow):
        super().__init__(stage)
        self.gameWindow = gameWindow

    def makeDecision(self):
        #TODO
        key = ''
        while not (key == 'Up' or key == 'Left' or key == 'Down' or key == 'Right'):
            key = self.gameWindow.checkKey()
