from State import *
from GameObject import *
from Enviroment import *

class Stage(Enviroment):

    # stage stores the folloing unchanging data:
    #   walls: 2d array of boolean values ( true => wall exists)
    #   players: a list of player objects ( object's state may change but references don't)
    rowCount = 0
    colCount = 0
    walls = None

    def __init__(self, rowCount, colCount):
        super(Stage, self).__init__(self, GameState())

        self.rowCount = rowCount
        self.colCount = colCount
        self.walls = [[None for x in range(colCount)] for y in range(rowCount)]
            

    def executeAction(self, action: Action):
        newState = action.execute(self.state)
        if not self.checkStateValidity(newState):
            raise SimulationError("Player " + player.name + " tried to execute an illigal move")
        self.state = newState

    def checkActionValidity(self, state):
        #TODO
        return True

    def placeObject(self, object, position):
        if not self.positionIsEmpty(position):
            raise StageException('Position is not empty')
        if type(object) is Wall:
            self.walls[position.row][position.col] = True
        if type(object) is Coin:
            self.state.coinPositions.append(position)
        if issubclass(type(object), Player):
            self.players.append(object)
            self.state.playerPositions.append(position)

    def positionIsEmpty(self, position):
        for pos in self.state.playerPositions:
            if pos.isTheSamePositionAs(position):
                return False
        for pos in self.state.coinPositions:
            if pos.isTheSamePositionAs(position):
                return False
        if self.walls[position.row][position.col]:
            return False
        return True

    def positionIsEmptyOfSolids(self, position):
        if self.walls[position.row][position.col]:
            return False
        for playerPos in self.state.playerPositions:
            if playerPos.isTheSamePositionAs(position):
                return False
        return True
        
    def positionIsEmptyOfWalls(self, position):
        if self.walls[position.row][position.col]:
            return False
        return True
        
    def positionIsOutOfBounds(self, position):
        if position.row < 0 or position.row > self.rowCount -1 or
            position.col < 0 or position.col > self.colCount -1:
            return True
        return False

    def gameIsOver(self):
        if len(self.state.coinPositions) == 0:
            return True
        return False

    def getIndexOfPlayer(self, player):
        for i in range(0, len(self.players)):
            if self.players[i] is player:
                return i
            
    @staticmethod
    def getPlayerColors():
        return ['lightblue', 'pink', 'lightgreen', 'orange', 'yellow']


class StageException(Exception):
    pass
