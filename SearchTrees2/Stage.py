from State import *
from GameObject import *

class Stage:

    # stage stores the folloing unchanging data:
    #   walls: 2d array of boolean values ( true => wall exists)
    #   players: a list of player objects ( object's state may change but references don't)

    rowCount = 0
    colCount = 0
    walls = None
    players = None
    state = None

    def __init__(self, rowCount, colCount):
        self.rowCount = rowCount
        self.colCount = colCount
        self.walls = [[None for x in range(colCount)] for y in range(rowCount)]
        self.players = []
        self.state = State()

    def executePlayerMove(self, player, move):
        if move == 'Stay':
            return False
        for i in range(0, len(self.players)):
            if self.players[i] is player:
                oldPosition = self.state.playerPositions[i]
                position = oldPosition.copy()
                oldObjectWasCoin = False
                for coinPos in self.state.coinPositions:
                    if oldPosition.isTheSamePositionAs(coinPos):
                        oldObjectWasCoin = True
                if move == 'Up':
                    position.row -= 1
                if move == 'Right':
                    position.col += 1
                if move == 'Down':
                    position.row += 1
                if move == 'Left':
                    position.col -= 1
                if not self.positionIsEmptyOfSolids(position):
                    raise StageException('Move is not allowed (blocked by other object)')
                if self.positionIsOutOfBounds(position):
                    raise StageException('Move is not allowed (out of bounds)')
                
                self.state.playerPositions[i] = position
                for coinPos in self.state.coinPositions:
                    if coinPos.isTheSamePositionAs(position):
                        self.state.coinPositions.remove(coinPos)
                        player.points += 1
                player.rotation = move
                return oldObjectWasCoin
                

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
        if position.row < 0 or position.row > self.rowCount -1 or position.col < 0 or position.col > self.colCount -1:
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
