from solidObject import *

class Stage:
    rowCount = 0
    colCount = 0

    state = [[]]  # an 2d array of states
    
    def __init__(self, rowCount = 3, colCount = 3):
        self.rowCount = rowCount
        self.colCount = colCount
        self.state = [[None for x in range(colCount)] for y in range(rowCount)]


    def moveObject(self, sourcePosition, destinationPosition):
        if not issubclass(self.state[sourcePosition.row][sourcePosition.col], SolidObject):
            raise StageException('There is no object to be moved at position ' + str(sourcePosition.row) + ',' + str(sourcePosition.col))
        if issubclass(self.state[destinationPosition.row][destinationPosition.col], SolidObject):
            raise StageException('There already is an object at position ' + str(destinationPosition.row) + ',' + str(destinationPosition.col))
        
        self.state[destinationPosition.row][destinationPosition.col] = self.state[sourcePosition.row][sourcePosition.col];
        self.state[sourcePosition.row][sourcePosition.col] = None


    def getPositionOf(self, object):
        for i in range(0, self.rowCount):
            for j in range(0, self.colCount):
                if self.state[i][j] is object:
                    return GridPosition(i,j)
        raise StageException('Given object does not exist in the stage')

class GridPosition:
    row = None
    col = None

    def __init__(self, row, col):
        self.row = row
        self.col = col

class StageException(Exception):
    pass