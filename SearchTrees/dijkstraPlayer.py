from player import *
from stage import *
from stateAnalyser import *
import time

class PathFinderPlayer(Player):

    activeNodes = None
    moves = None
    gameWindow = None

    def __init__(self, stage, gameWindow):
        super().__init__(stage)
        self.gameWindow = gameWindow
        self.searchMap = StateAnalyser.getEmptyState(stage.rowCount, stage.colCount)
        self.checkedStates = []

    def initialize(self): # find the path and store it in the moves list
        self.activeNodes = []
        self.activeNodes.append(TreeNode(self.stage.state, None, None, 0))
        while len(self.activeNodes) > 0:
            if self.checkForSearchEnd():
                return
            else:
                node = self.popNodeToAppend()
                self.activeNodes.append(node.getChildren())
        raise Exception('Path not found')        

    def popNodeToAppend(self):
        nodeWithMostReward = self.activeNodes[0]
        for i in range(1, len(self.activeNodes)):
            if self.activeNodes[i].collectedReward > nodeWithMostReward.collectedReward:
                nodeWithMostReward = self.activeNodes[i]
        self.activeNodes.remove(nodeWithMostReward)
        return nodeWithMostReward

    def checkForSearchEnd():
        for node in self.activeNodes:


    def move(self):
        self.stage.moveObjectTowardsDirection(self, self.moves.pop(0))
        time.sleep(0.5)



class TreeNode:
    move = None
    state = None
    parent = None
    collectedReward = None

    def __init__(self, state, move, parent, collectedReward):
        self.state = state
        self.move = move
        self.parent = parent
        self.collectedReward = collectedReward
