from stage import *

class SolidObject:
    stage = None

    def __init__(self, stage):
        self.stage = stage

    def moveTo(self, row, col):
        self.stage.moveObject(self.stage.getPositionOf(self), GridPosition(row,col))
