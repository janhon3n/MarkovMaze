from stateAnalyser import *
from player import *

class MinMaxPlayer(Player):

    stage = None
    iterations = 4
    discounting = 0
    enemyRewardMultiplier = -0.8
    thresholdToDiscard = 0.2 # if the nodes are this threshold away from the best path discard them

    def __init__(self, stage, iterations, discounting):
        self.stage = stage
        self.iterations = iterations
        self.discounting = discounting

    def move(self):
        self.stage.moveObjectTowardsDirection(self, self.findBestMove())
        
    def findBestMove(self): #called when its is selfs turn
        treeRoot = MinMaxTreeNode(self.stage.state, None, 0, None, self.discounting)
        lowestNodes = [treeRoot]
        bestReward = -1000
        for i in range(0, self.iterations):
            for playerIndex in range(0, len(self.stage.players)):
                moduloAdder = self.stage.players.index(self)# [p, p]
                playerIndex = (playerIndex + moduloAdder) % len(self.stage.players)
                newLowestNodes = []
                rewardMultiplier = 1
                if self.stage.players[playerIndex] is not self:
                    rewardMultiplier = self.enemyRewardMultiplier
                for node in lowestNodes:
                    newLowestNodes.extend(node.findChildNodes(self.stage.players[playerIndex], rewardMultiplier, bestReward - self.thresholdToDiscard))
                for node in newLowestNodes:
                    if node.cumulatedReward > bestReward:
                        bestReward = node.cumulatedReward
                lowestNodes = newLowestNodes


        enemyCount = len(self.stage.players) - 1
        bestNode = treeRoot.findMaxNode(enemyCount)
        return bestNode.findRootMove()


class MinMaxTreeNode():
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

    def findChildNodes(self, player, rewardMultiplier, discardThreshold):
        moves = StateAnalyser.getMovesFor(self.state, player)
        for move in moves:
            [newState, reward] = StateAnalyser.getNewStateFromAMove(self.state, player, move)
            newReward = self.cumulatedReward + (reward * self.discounting * rewardMultiplier)
#            if newReward > discardThreshold:
            newChildNode = MinMaxTreeNode(newState, self, self.cumulatedReward + (reward * self.discounting * rewardMultiplier), move, self.discounting * self.discounting)
            self.childNodes.append(newChildNode)
        return self.childNodes

    def findMaxNode(self, enemyCount):
        if len(self.childNodes) is 0:
            return self

        maxReward = -1000
        bestNode = None
        for node in self.childNodes:
            endNode = node.findMinNode(enemyCount, 0)
            if endNode is not None and endNode.cumulatedReward > maxReward:
                bestNode = endNode
                maxReward = endNode.cumulatedReward
        return bestNode

    def findMinNode(self, enemyCount, minIterationsDone):
        if len(self.childNodes) is 0:
            return self

        minReward = 1000
        bestNode = None
        for node in self.childNodes:
            endNode = None
            if enemyCount > minIterationsDone + 1: # if still min iterations left
                endNode = node.findMinNode(enemyCount, minIterationsDone + 1)
            else:
                endNode = node.findMaxNode(enemyCount)

            if endNode is not None and endNode.cumulatedReward < minReward:
                bestNode = endNode
                minReward = endNode.cumulatedReward

        return bestNode

    def findRootMove(self):
        rootMoveNode = self
        while rootMoveNode.parent.parent is not None:
            rootMoveNode = rootMoveNode.parent
        return rootMoveNode.move
    