from State import *

class GameState(State):

    # state stores the folloing changing data:
    #   playerPositions: a list of positions for the players.
    #                   Positions are mached to the player objects by the ORDER they are in the list
    #                   nth position in list == positions of the n:th player object in the stages players list
    #
    #   coinPositions: a list of positions for the coins.

    playerPositions = None
    coinPositions = None

    def __init__(self):
        self.playerPositions = []
        self.coinPositions = []

    def equals(self, state):
        if len(self.playerPositions) != len(state.playerPositions):
            return False
        if len(self.coinPositions) != len(state.coinPositions):
            return False
        for i in range(0, len(self.playerPositions)):
            if not self.playerPositions[i].isTheSamePositionAs(state.playerPositions[i]):
                return False
        for coinPos in self.coinPositions:
            sameCoinFound = False
            for i in range(0, len(state.coinPositions)):
                if coinPos.isTheSamePositionAs(state.coinPositions[i]):
                    sameCoinFound = True
                    break
            if not sameCoinFound:
                return False
        return True

    def copy(self):
        copy = State()
        for playerPos in self.playerPositions:
            copy.playerPositions.append(playerPos.copy())
        for coinPos in self.coinPositions:
            copy.coinPositions.append(coinPos.copy())
        return copy



class Position:
    row = None
    col = None

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def isTheSamePositionAs(self, position):
        return self.row is position.row and self.col is position.col

    def copy(self):
        return Position(self.row, self.col)

    def calculateDistanceTo(self, position):
        deltaRow = self.row - position.row
        deltaCol = self.col - position.col
        return abs(deltaRow) + abs(deltaCol)

    def getNewPositionFromAction(self, action):
        newPos = self.copy()
        if action == 'Up':
            newPos.row += -1
        if action == 'Right':
            newPos.col += 1
        if action == 'Down':
            newPos.row += 1
        if action == 'Left':
            newPos.col += -1
        return newPos