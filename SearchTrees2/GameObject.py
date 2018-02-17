from Stage import *

class GameObject:
    stage = None
    rotation = 'Up'

    def __init__(self, stage):
        self.stage = stage

class SolidObject(GameObject):
    pass

class Coin(GameObject):
    pass

class Wall(SolidObject):
    pass

class Player(SolidObject):

    points = 0

    def move(self):
        self.stage.movePlayer(self, 'Up')        

    def initialize(self):
        pass
        
        
class HumanPlayer(Player):
    gameWindow = None

    def __init__(self, stage, gameWindow):
        super().__init__(stage)
        self.gameWindow = gameWindow

    def move(self):
        moveSuccessful = False
        while not moveSuccessful:
            try:
                key = ""
                while not (key == 'Up' or key == 'Left' or key == 'Down' or key == 'Right'):
                    key = self.gameWindow.checkKey()
                self.stage.executePlayerMove(self, key)
                moveSuccessful = True
            except Exception as ex:
                pass