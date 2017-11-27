class GameObject:
    stage = None
    rotation = "Up"

    def __init__(self, stage):
        self.stage = stage

    def moveTo(self, row, col):
        self.stage.moveObject(self.stage.getPositionOf(self), {"row":row, "col":col})