from stateAnalyzer import *
from player import *

class RewardSearchPlayer(Player):



    @staticmethod
    def findBestMoveFor(object, state, iterations, rewardOptimizationFunction): #objectiveType: {'min', 'max'}
        treeRoot = TreeNode(state, None, 0)
        lowestNodes = [treeRoot]
        for i in range(0, iteration):
            newLowestNodes = []
            for node in lowestNodes:
                newLowestNodes.extend(node.findChildNodes(self))
            lowestNodes = newLowestNodes

        bestNode = lowestNodes[0]        
        for i in range(1, len(lowestNodes)):
            if rewardOptimizationFunction(lowestNodes[i].cumulatedReward, bestNode.cumulatedReward):
                bestNode = lowestNodes[i]
        
        return bestNode.findRootMove()


class TreeNode():
    state = None
    childNodes = None
    parentNode = None
    cumulatedReward = 0

    def __init__(self, state, parent, reward):
        self.state = state
        self.parent = parent
        self.reward = reward

    def findChildNodes(self, player):
        moves = StateAnalyser.getMovesFor(self.state, self.player)
        for move in moves:
            [newState, reward] = StateAnalyser.getNewStateFromAMove(self.state, self.player, move)
            self.cumulatedReward += reward
            newChildNode = MoveTreeNode(newState, self.player, move, self)
            self.childNodes.append(newChildNode)
        return self.childNodes


    def findRootMove(self):
