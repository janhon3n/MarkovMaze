from GameObject import *

class State:

    players = None
    coins = None
    walls = None

    rowCount = 0
    colCount = 0
    objects = None

    def __init__(self, rowCount, colCount):
        self.objects = [[None for j in colCount] for i in rowCount]
        self.players = []
        self.coins = []
        self.walls = []

    def placeObject(self, object, position):
        if issubclass(type(object), Player):
            self.players.append(object)
        if issubclass(type(object), Coin):
            self.coins.append(object)
        if issubclass(type(object), Wall):
            self.walls.append(object)

    def getObjectAt(self, position):
        return self.objects[position['row']][position['col']]

    def getPositionOf(self, object):
        for row in range(0, self.rowCount):
            for col in range(0, self.colCount):
                if self.objects[row][col] is object:
                    return {'row':row, 'col':col}
        raise StateException('Given object does not exist in the state')


    # Moves an object to a position
    # returns the previous object in the position that was overwriten
    def moveObjectToPosition(self, object, position):
        overwritenObject = None
        if issubclass(type(self.getObjectAt(position)), SolidObject):
            raise StateException('An solid object already exists at the position')
        originalPosition = self.getPositionOf(object)
        overwritenObject = self.getObjectAt(position)
        if type(self.getObjectAt(position)) is Coin:
            self.coins.remove(self.getObjectAt(position))

        self.objects[position['row']][position['col']] = object
        self.objects[originalPosition['row']][originalPosition['col']] = None
        return overwritenObject

    def isTheSameStateAs(self, state):
        if self.rowCount is not state.rowCount or self.colCount is not state.colCount:
            return False
        for row in range(0, self.rowCount):
            for col in range(0, self.colCount):
                if type(self.getObjectAt({'row': row, 'col':col})) is not type(state.getObjectAt({'row': row, 'col':col})):
                    return False
        return True


class StateException(Exception):
    pass