from solidObject import *
from stageException import *

class Stage:
    rowCount = 0
    colCount = 0

    state = [[]]  # an 2d array of states
    
    def __init__(self, rowCount = 3, colCount = 3):
        self.rowCount = rowCount
        self.colCount = colCount
        self.state = [[None for x in range(colCount)] for y in range(rowCount)]


    def moveObject(self, object, destinationPosition):
        sourcePosition = self.getPositionOf(object)
        if not issubclass(type(self.state[sourcePosition['row']][sourcePosition['col']]), SolidObject):
            raise StageException('There is no object to be moved at position ' + str(sourcePosition['row']) + ',' + str(sourcePosition['col']))
        if issubclass(type(self.state[destinationPosition['row']][destinationPosition['col']]), SolidObject):
            raise StageException('There already is an object at position ' + str(destinationPosition['row']) + ',' + str(destinationPosition['col']))
        
        self.state[destinationPosition['row']][destinationPosition['col']] = self.state[sourcePosition['row']][sourcePosition['col']];
        self.state[sourcePosition['row']][sourcePosition['col']] = None

    def placeObject(self, object, destinationPosition):
        if issubclass(type(self.state[destinationPosition['row']][destinationPosition['col']]), SolidObject):
            raise StageException('There already is an object at position ' + str(destinationPosition['row']) + ',' + str(destinationPosition['col']))
        self.state[destinationPosition['row']][destinationPosition['col']] = object

    def getPositionOf(self, object):
        for i in range(0, self.rowCount):
            for j in range(0, self.colCount):
                if self.state[i][j] is object:
                    return { 'row':i, 'col':j }
        return None


    def getObjects(self):
        objects = []
        for i in range(0, self.rowCount):
            for j in range(0, self.colCount):
                if issubclass(type(self.state[i][j]), SolidObject):
                    dictionary = {'position': self.getPositionOf(self.state[i][j]), 'object': self.state[i][j]}
                    objects.append(dictionary)
        return objects