class State:
    playerPositions = None # an array of positions of players in order
    coinPositions = None # an array of positions of coins, order does not matter

    def __init__(self):
        self.playerPositions = []
        self.coinPositions = []

    def isTheSameStateAs(self, state):
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