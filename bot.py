from solidObject import *

class Bot(SolidObject):
    points = None
    stage = None

    def __init__(self, stage, gameWindow):
        self.stage = stage

    def move(self):
        return



class MinMaxBot(Bot):