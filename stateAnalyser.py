from solidObject import *
from coin import *
from copy import copy, deepcopy
from player import *

class StateAnalyser:

    @staticmethod
    def getMovesFor(state, object):
        moves = []
        position = StateAnalyser.getPositionOf(state, object)
        currentRow = position['row']
        currentCol = position['col']
        if StateAnalyser.positionIsEmptyOfSolids(state, {'row':currentRow - 1, 'col': currentCol}):
            moves.append('Up')
        if StateAnalyser.positionIsEmptyOfSolids(state, {'row':currentRow, 'col': currentCol + 1}):
            moves.append('Right')
        if StateAnalyser.positionIsEmptyOfSolids(state, {'row':currentRow + 1, 'col': currentCol}):
            moves.append('Down')
        if StateAnalyser.positionIsEmptyOfSolids(state, {'row':currentRow, 'col': currentCol - 1}):
            moves.append('Left')
        return moves


    @staticmethod
    def getPositionOf(state, object):
        for i in range(0, len(state)):
            for j in range(0, len(state[0])):
                if state[i][j] is object:
                    return { 'row':i, 'col':j }
        raise StateException('Give object does not exist in the state')


    @staticmethod
    def positionIsEmptyOfSolids(state, position):
        rowCount = len(state)
        colCount = len(state[0])
        if position['row'] >= rowCount or position['row'] < 0 :
            return False
        if position['col'] >= colCount or position['col'] < 0 :
            return False
        if issubclass(type(state[position['row']][position['col']]), SolidObject):
            return False
        return True


    @staticmethod
    def moveObjectTowardsDirection(state, object, direction):
        reward = 0
        position = StateAnalyser.getPositionOf(state, object)
        oldPosition = copy(position)
        if direction == "Up":
            position['row'] = position['row'] - 1
        elif direction == "Down":
            position['row'] = position['row'] + 1
        elif direction == "Right":
            position['col'] = position['col'] + 1
        elif direction == "Left":
            position['col'] = position['col'] - 1
        try:
            if type(state[position['row']][position['col']]) is Coin:
                reward = 1
            StateAnalyser.moveObject(state, object, position)
            state[oldPosition['row']][oldPosition['col']] = Marker()
            return reward
        except StateException as ex:
            pass


    @staticmethod
    def moveObject(state, object, destinationPosition):
        if destinationPosition['row'] >= len(state) or destinationPosition['row'] < 0:
            raise StateException('Given destination row is out of stage bounds')
        if destinationPosition['col'] >= len(state[0]) or destinationPosition['col'] < 0:
            raise StateException('Given destination column is out of stage bounds')

        sourcePosition = StateAnalyser.getPositionOf(state, object)
        if not issubclass(type(state[sourcePosition['row']][sourcePosition['col']]), SolidObject):
            raise StateException('There is no object to be moved at position ' + str(sourcePosition['row']) + ',' + str(sourcePosition['col']))
        if issubclass(type(state[destinationPosition['row']][destinationPosition['col']]), SolidObject):
            raise StateException('There already is an object at position ' + str(destinationPosition['row']) + ',' + str(destinationPosition['col']))
        
        state[destinationPosition['row']][destinationPosition['col']] = state[sourcePosition['row']][sourcePosition['col']]
        state[sourcePosition['row']][sourcePosition['col']] = None


    @staticmethod
    def getNewStateFromAMove(state, object, direction):
        rowCount = len(state)
        colCount = len(state[0])
        newState = []
        for rowNumber in range(0, rowCount):
            newState.append(copy(state[rowNumber]))
        reward = StateAnalyser.moveObjectTowardsDirection(newState, object, direction)
        return [newState, reward]

    @staticmethod
    def getAllCoins(state):
        objects = []
        for i in range(0, len(state)):
            for j in range(0, len(state[0])):
                if issubclass(type(state[i][j]), Coin):
                    objects.append(state[i][j])
        return objects                    

    @staticmethod
    def goalIsReached(state):
        if len(StateAnalyser.getAllCoins(state)) is 0:
            return True
        return False
        

    @staticmethod
    def getObjects(state):
        objects = []
        for i in range(0, len(state)):
            for j in range(0, len(state[0])):
                if issubclass(type(state[i][j]), GameObject):
                    dictionary = {'position': StateAnalyser.getPositionOf(state, state[i][j]), 'object': state[i][j]}
                    objects.append(dictionary)
        return objects


    @staticmethod
    def getEmptyState(rowCount, colCount):
        return [[None for x in range(colCount)] for y in range(rowCount)]

    @staticmethod
    def isTheSameState(state1, state2):
        rowCountInState1 = len(state1)
        colCountInState1 = len(state1[0])
        rowCountInState2 = len(state2)
        colCountInState2 = len(state2[0])
        if rowCountInState1 is not rowCountInState2 or colCountInState1 is not colCountInState2:
            return False
        for i in range(0, rowCountInState1):
            for j in range(0, colCountInState1):
                if type(state1[i][j]) is not type(state2[i][j]):
                    if type(state1[i][j]) is Marker and state2[i][j] is None:
                        continue
                    if type(state2[i][j]) is Marker and state1[i][j] is None:
                        continue
                    return False
        return True


class StateException(Exception):
    pass