from gameObject import *

class Coin(GameObject):
    value = 0

    def __init__(self, value):
        self.value = value
        super().__init__(self)
