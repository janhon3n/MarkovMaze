from SearchTreePlayer import *

class UpdatingSearchTreePlayer(SearchTreePlayer):
    maxIterations = 40

    def initialize(self):
        self.gameWindow = None
        return

    def move(self):
        move = self.findPathWithMaxReward(self.maxIterations)
        self.stage.executePlayerMove(self, move)


    def findPathWithMaxReward(self, maxIterations):
        self.activeNodes = []
        self.deadNodes = []
        self.moveToGoalState = []
        startTime = time.time()
        self.activeNodes.append(TreeNode(self.stage.state.copy(), None, None, 0, None, 1))
        iteration = 1
        while iteration < maxIterations:
            nodeToExpand = self.popANodeToExpand()
            if self.gameWindow is not None:
                if nodeToExpand.move is not None:
                    self.rotation = nodeToExpand.move
                self.gameWindow.drawStateWithMarkers(nodeToExpand.state, nodeToExpand.markers)
            newNodes = self.expandNode(nodeToExpand)
            self.deadNodes.append(nodeToExpand)
            if self.checkGoalCondition(nodeToExpand, newNodes):
                return self.getRootMoveFromNode(nodeToExpand)
            self.checkIfAnyNodesAlreadyInTree(newNodes)
            self.activeNodes.extend(newNodes)
            print("Current node depth: "+str(nodeToExpand.treeLayer) +", Reward: "+("{0:.2f}".format(nodeToExpand.cumulatedReward))+", Dead nodes: "+str(len(self.deadNodes))+", Active nodes: "+str(len(self.activeNodes))+", Elapsed time: " + ("{0:.2f}".format(time.time() - startTime)))
            iteration += 1
        return self.getRootMoveFromNode(self.findBestActiveNode())


    def getRootMoveFromNode(self, node):
        return self.getPathFromRoot(node).pop()

    def findBestActiveNode(self):
        bestValue = -1000
        bestNode = None
        for node in self.activeNodes:
            if node.cumulatedReward > bestValue:
                bestNode = node
                bestValue = node.cumulatedReward
        return bestNode



    def checkGoalCondition(self, nodeToExpand, newNodes):
        if len(nodeToExpand.state.coinPositions) == 0:
            return True
        return False
        