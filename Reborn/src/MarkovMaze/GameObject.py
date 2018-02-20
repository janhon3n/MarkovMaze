from Stage import *

class GameObject:
    super(GameObject, self).__init__(self)
    stage = None
    rotation = 'Up'

    def __init__(self, stage):
        self.stage = stage

class SolidObject(GameObject):
    super(SolidObject, self).__init__(self)
    pass

class Coin(GameObject):
    pass

class Wall(SolidObject):
    pass