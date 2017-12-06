from State import *
from Stage import *

# An interface class for state manipulation
class StateAnalyser:

    # get possible actions for player in specific state
    @staticmethod
    def getPossibleActions(player, stage, state):
        playerIndex = stage.getIndexOfPlayer(player)
        oldPosition = state.playerPositions[playerIndex]
        actions = []
        directions = ['Up', 'Right', 'Down', 'Left']
        for direction in directions:
            newPosition = oldPosition.getNewPositionFromAction(direction)
            if (not stage.positionIsOutOfBounds(newPosition)) and stage.positionIsEmptyOfWalls(newPosition):
                emptyOfPlayers = True
                for playerPos in state.playerPositions:
                    if newPosition.isTheSamePositionAs(playerPos):
                        emptyOfPlayers = False
                if emptyOfPlayers:
                    actions.append(direction)
        if len(actions) == 0:
            actions.append('Stay')
        return actions


    @staticmethod
    def getStateFromAction(player, stage, state, action):
        newState = state.copy()
        playerIndex = stage.getIndexOfPlayer(player)
        newState.playerPositions[playerIndex] = newState.playerPositions[playerIndex].getNewPositionFromAction(action)
        reward = 0
        for coinPosition in newState.coinPositions:
            if coinPosition.isTheSamePositionAs(newState.playerPositions[playerIndex]):
                newState.coinPositions.remove(coinPosition)
                return [newState, 1]
        return [newState, 0]

    @staticmethod
    def isGoalState(player, stage, state):
        if len(state.coinPositions) == 0:
            return True
        return False
