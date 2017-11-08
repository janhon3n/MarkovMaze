from player import *
from stage import *
from stateAnalyser import *
import time

class PathFinderPlayer(Player):

    goalNode = None
    moves = None
    gameWindow = None
    checkedStates = None

    def __init__(self, stage, gameWindow):
        super().__init__(stage)
        self.gameWindow = gameWindow
        self.searchMap = StateAnalyser.getEmptyState(stage.rowCount, stage.colCount)
        self.checkedStates = []

    def findPath(self):
        layerCounter = 1
        searchMap = []
        moveTreeRoot = MoveTreeRoot(list(self.stage.state), self)
        self.checkedStates.append(self.stage.state)
        [lowestNodes, goalNode] = moveTreeRoot.findChildNodes(self.gameWindow)
        while goalNode is None:
            newLowestNodes = []
            for lowestNode in lowestNodes:
                [tempLowestNodes, goalNode] = lowestNode.findChildNodes(self.gameWindow)
                newLowestNodes.extend(tempLowestNodes)
                if goalNode is not None:
                    break
            lowestNodes = newLowestNodes
            layerCounter += 1
            print(layerCounter)
        self.goalNode = goalNode
        self.moves = self.goalNode.getMovesFromRoot()
        

    def move(self):
        self.stage.moveObjectTowardsDirection(self, self.moves.pop(0))
        time.sleep(0.5)

    def stateIsNotChecked(self, state):
        for checkedState in self.checkedStates:
            if StateAnalyser.isTheSameState(checkedState, state):
                return False
        return True



class MoveTreeRoot:
    state = None
    childNodes = None
    player = None
    parent = None
    move = None
    goalReached = False

    def __init__(self, state, player):
        self.state = state
        self.player = player
        self.childNodes = []

    def findChildNodes(self, gameWindow):
        goalNode = None
        moves = StateAnalyser.getMovesFor(self.state, self.player)
        for move in moves:
            newState = StateAnalyser.getNewStateFromAMove(self.state, self.player, move)
            if not self.player.stateIsNotChecked(newState):
                continue
            self.player.checkedStates.append(newState)
            if gameWindow is not None:
                gameWindow.drawState(newState)
            newChildNode = MoveTreeNode(newState, self.player, move, self)
            self.childNodes.append(newChildNode)
            if StateAnalyser.goalIsReached(newChildNode.state):
                newChildNode.goalReached = True
                goalNode = newChildNode
        return [self.childNodes, goalNode]


class MoveTreeNode(MoveTreeRoot):

    def __init__(self, state, player, move, parent):
        self.state = state
        self.player = player
        self.move = move
        self.childNodes = []
        self.parent = parent

    def getMovesFromRoot(self):
        moves = None
        if issubclass(type(self.parent), MoveTreeNode):
            moves = self.parent.getMovesFromRoot()
            moves.append(self.move)
            return moves
        else:
            return [self.move]

