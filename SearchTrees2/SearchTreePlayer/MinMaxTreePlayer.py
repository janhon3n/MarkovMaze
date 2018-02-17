from SearchTreePlayer import *

class MinMaxTreePlayer(SearchTreePlayer):

    activeLayer = []
    deadBranchNodes = []

    def expandLayer(self, player):
        newLayer = []
        for node in self.activeLayer:
            tempNodes = self.expandNode(node, player)
            newLayer.extend(tempNodes)

    def findPathWithMaxReward(self, maxIterations):
        self.activeNodes = []
        self.deadNodes = []
        self.moveToGoalState = []
        startTime = time.time()
        self.activeNodes.append(TreeNode(self.stage.state.copy(), None, None, 0, None, 1)) # add startnode to tree


        while True:

            if len(self.activeNodes) == 0: # if no more active nodes
                break

            nodeToExpand = self.popANodeToExpand()
            
            if self.gameWindow is not None: # if there is a gamewindow, draw the state of the node to be expanded
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
