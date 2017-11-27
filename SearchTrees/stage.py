from solidObject import *
from stageException import *
from coin import *
from stateAnalyser import *


class Stage:
    rowCount = 0
    colCount = 0

    state = None  # an 2d array of states
    players = None
    
    def __init__(self, rowCount = 3, colCount = 3):
        self.rowCount = rowCount
        self.colCount = colCount
        self.state = [[None for x in range(colCount)] for y in range(rowCount)]
        self.players = []

    def moveObjectTowardsDirection(self, object, direction):
        object.rotation = direction
        StateAnalyser.moveObjectTowardsDirection(self.state, object, direction)

    def placeObject(self, object, destinationPosition):
        if issubclass(type(self.state[destinationPosition['row']][destinationPosition['col']]), SolidObject):
            raise StageException('There already is an object at position ' + str(destinationPosition['row']) + ',' + str(destinationPosition['col']))
        self.state[destinationPosition['row']][destinationPosition['col']] = object

    def placePlayer(self, playerObject, destinationPosition):
        self.placeObject(playerObject, destinationPosition)
        self.players.append(playerObject)

    def getPositionOf(self, object):
        for i in range(0, self.rowCount):
            for j in range(0, self.colCount):
                if self.state[i][j] is object:
                    return { 'row':i, 'col':j }
        return None


    def gameIsOver(self):
        return StateAnalyser.goalIsReached(self.state)

    def getObjects(self):
        objects = []
        for i in range(0, self.rowCount):
            for j in range(0, self.colCount):
                if issubclass(type(self.state[i][j]), GameObject):
                    dictionary = {'position': self.getPositionOf(self.state[i][j]), 'object': self.state[i][j]}
                    objects.append(dictionary)
        return objects
    
    def getCoins(self):
        coins = []
        for object in self.getObjects():
            if issubclass(type(object), Coin):
                coins.append(object)
        return coins