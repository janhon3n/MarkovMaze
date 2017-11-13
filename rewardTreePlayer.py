from stateAnalyser import *
from player import *

class RewardTreePlayer(Player):

    stage = None
    iterations = 4
    discounting = 0

    def __init__(self, stage, iterations, discounting):
        self.stage = stage
        self.iterations = iterations
        self.discounting = discounting

    def move(self):
        self.stage.moveObjectTowardsDirection(self, self.findBestMove())
        
    def findBestMove(self):
        treeRoot = RewardTreeNode(self.stage.state, None, 0, None, self.discounting)
        lowestNodes = [treeRoot]
        for i in range(0, self.iterations):
            newLowestNodes = []
            for node in lowestNodes:
                newLowestNodes.extend(node.findChildNodes(self))
            lowestNodes = newLowestNodes

        bestNode = lowestNodes[0]        
        for i in range(1, len(lowestNodes)):
            if lowestNodes[i].cumulatedReward > bestNode.cumulatedReward:
                bestNode = lowestNodes[i]
        
        return bestNode.findRootMove()


class RewardTreeNode():
    state = None
    childNodes = None
    parentNode = None
    move = None
    cumulatedReward = 0
    discounting = 1

    def __init__(self, state, parent, reward, move, discounting):
        self.state = state
        self.parent = parent
        self.cumulatedReward = reward
        self.move = move
        self.childNodes = []
        self.discounting = discounting

    def findChildNodes(self, player):
        moves = StateAnalyser.getMovesFor(self.state, player)
        for move in moves:
            [newState, reward] = StateAnalyser.getNewStateFromAMove(self.state, player, move)
            newChildNode = RewardTreeNode(newState, self, self.cumulatedReward + (reward * self.discounting), move, self.discounting * self.discounting)
            self.childNodes.append(newChildNode)
        return self.childNodes


    def findRootMove(self):
        rootMoveNode = self
        while rootMoveNode.parent.parent is not None:
            rootMoveNode = rootMoveNode.parent
        return rootMoveNode.move