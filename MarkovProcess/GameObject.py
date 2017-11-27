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

    def move(self):
        self.stage.movePlayer(self, 'Up')

        
        
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