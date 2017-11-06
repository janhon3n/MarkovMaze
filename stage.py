from solidObject import *
from stageException import *

class Stage:
    rowCount = 0
    colCount = 0

    state = [[]]  # an 2d array of states
    player = None
    bots = []
    
    def __init__(self, rowCount = 3, colCount = 3):
        self.rowCount = rowCount
        self.colCount = colCount
        self.state = [[None for x in range(colCount)] for y in range(rowCount)]


    def moveObject(self, object, destinationPosition):
        if destinationPosition['row'] >= self.rowCount or destinationPosition['row'] < 0:
            raise StageException('Given destination row is out of stage bounds')
        if destinationPosition['col'] >= self.colCount or destinationPosition['col'] < 0:
            raise StageException('Given destination column is out of stage bounds')

        sourcePosition = self.getPositionOf(object)
        if not issubclass(type(self.state[sourcePosition['row']][sourcePosition['col']]), SolidObject):
            raise StageException('There is no object to be moved at position ' + str(sourcePosition['row']) + ',' + str(sourcePosition['col']))
        if issubclass(type(self.state[destinationPosition['row']][destinationPosition['col']]), SolidObject):
            raise StageException('There already is an object at position ' + str(destinationPosition['row']) + ',' + str(destinationPosition['col']))
        
        self.state[destinationPosition['row']][destinationPosition['col']] = self.state[sourcePosition['row']][sourcePosition['col']];
        self.state[sourcePosition['row']][sourcePosition['col']] = None

    def moveObjectTowardsDirection(self, object, direction):
        position = self.getPositionOf(object)
        object.rotation = direction
        if direction == "Up":
            position['row'] = position['row'] - 1
        elif direction == "Down":
            position['row'] = position['row'] + 1
        elif direction == "Right":
            position['col'] = position['col'] + 1
        elif direction == "Left":
            position['col'] = position['col'] - 1
        try:
            self.moveObject(object, position)
        except StageException as ex:
            pass

    def placeObject(self, object, destinationPosition):
        if issubclass(type(self.state[destinationPosition['row']][destinationPosition['col']]), SolidObject):
            raise StageException('There already is an object at position ' + str(destinationPosition['row']) + ',' + str(destinationPosition['col']))
        self.state[destinationPosition['row']][destinationPosition['col']] = object

    def placePlayer(self, playerObject, destinationPosition):
        self.placeObject(playerObject, destinationPosition)
        self.player = playerObject

    def placeBot(self, botObject, destinationPosition):
        self.placeObject(botObject, destinationPosition)
        self.bots.append(botObject)
        
    def getPositionOf(self, object):
        for i in range(0, self.rowCount):
            for j in range(0, self.colCount):
                if self.state[i][j] is object:
                    return { 'row':i, 'col':j }
        return None


    def gameIsOver(self):
        return False

    def getObjects(self):
        objects = []
        for i in range(0, self.rowCount):
            for j in range(0, self.colCount):
                if issubclass(type(self.state[i][j]), GameObject):
                    dictionary = {'position': self.getPositionOf(self.state[i][j]), 'object': self.state[i][j]}
                    objects.append(dictionary)
        return objects