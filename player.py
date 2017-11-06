from solidObject import *
from msvcrt import getch

class Player(SolidObject):
    points = None

    def move(self):
        return


class HumanPlayer(Player):

    gameWindow = None

    def __init__(self, stage, gameWindow):
        super().__init__(stage)
        self.gameWindow = gameWindow

    def move(self):
        key = ""
        while not (key == 'Up' or key == 'Left' or key == 'Down' or key == 'Right'):
            key = self.gameWindow.checkKey()
        self.stage.moveObjectTowardsDirection(self, key)