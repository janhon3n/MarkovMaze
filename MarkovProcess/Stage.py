from solidObject import *
from stageException import *
from coin import *
from stateAnalyser import *
import random


class Stage:
    state = None
    moveSuccessPropability = 0.7

    def __init__(self, state):
        self.state = state

    def movePlayer(self, player, moveDirection):
        if random.uniform(0,1) < moveSuccessPropability:
            self.movePlayerTowardsDirection(player, moveDirection)
        else:
            orthogonalMoves = self.findOrthogonalMoves(moveDirection)
            if random.uniform(0,1) < (1 - moveSuccessPropability) / 2:
                movePlayerTowardsDirection(player, orthogonalMoves[0])
            else:
                movePlayerTowardsDirection(player, orthogonalMoves[1])
                

    def movePlayerTowardsDirection(self, player, moveDirection):
        position = self.state.getPositionOf(player)
        if moveDirection == 'Up':
            position['row'] = position['row'] - 1
        else if moveDirection == 'Right':
            position['col'] = position['col'] + 1
        else if moveDirection == 'Down':
            position['row'] = position['row'] + 1
        else if moveDirection == 'Left'
            position['col'] = position['col'] - 1
        else:
            raise StageException('Unrecognised move direction was given')
        self.state.moveObjectToPosition(player, position)
        


class StageException(Exception):
    pass