from GameObject import *
from Stage import *
from StateAnalyser import *
import time

class SearchTreePlayer(Player):

    activeNodes = None
    deadNodes = None
    leafNodes = None
    actionsToGoalState = None
    gameWindow = None

    goalNode = None

    actionCost = 0.2
    discounting = 1.0

    def __init__(self, stage, gameWindow):
        super().__init__(stage)
        self.gameWindow = gameWindow

    def move(self):
        self.stage.executePlayerMove(self, self.actionsToGoalState.pop())
        time.sleep(0.1)

    def initialize(self):
        self.activeNodes = []
        self.actionsToGoalState = []
        self.deadNodes = []
        self.leafNodes = []
        self.executeSearch()


    def executeSearch(self):
        startTime = time.time()

        self.setupStartingNodes()

        while self.continueSearch():
            nodeToExpand = self.popANodeToExpand()

            if self.gameWindow is not None: # draw search process if gameWindow is setup
                if nodeToExpand.action is not None:
                    self.rotation = nodeToExpand.action
                self.gameWindow.drawStateWithMarkers(nodeToExpand.state, nodeToExpand.markers)

            newNodes = self.expandNode(nodeToExpand, self)
            self.deadNodes.append(nodeToExpand)
            self.fixNewNodes(nodeToExpand, newNodes)   # can alter the newNodes list
            self.activeNodes.extend(newNodes)   # add new nodes to active nodes

            print("Current node depth: "+str(nodeToExpand.treeLayer) +", Reward: "+("{0:.2f}".format(nodeToExpand.cumulatedReward))+", Dead nodes: "+str(len(self.deadNodes))+", Active nodes: "+str(len(self.activeNodes))+", Elapsed time: " + ("{0:.2f}".format(time.time() - startTime)))
        
        self.finishSearch()
        

    #==== Functions used with executeSearch(), can be overwriten when modifying the search type ====

    def setupStartingNodes(self): # by default add node with current state to the tree
        self.activeNodes.append(TreeNode(self.stage.state.copy(), None, None, 0, None, 1))

    def continueSearch(self): # by default continue search while active nodes exist
        if self.goalNode is not None:
            return False
        if len(self.activeNodes) > 0:
            return True
        return False

    def popANodeToExpand(self):
        return self.activeNodes.pop(0)

    def expandNode(self, node, player):
        newNodes = []
        actions = StateAnalyser.getPossibleActions(player, self.stage, node.state)
        for action in actions:
            [newState, reward] = StateAnalyser.getStateFromAction(player, self.stage, node.state, action)
            reward -= self.actionCost
            treeLayer = node.treeLayer + 1
            reward *= self.discounting ** treeLayer
            markers = node.markers.copy()
            markers.append(newState.playerPositions[self.stage.getIndexOfPlayer(player)])
            newNodes.append(TreeNode(newState, node, action, node.cumulatedReward + reward, markers, treeLayer))
        return newNodes


    def fixNewNodes(self, nodeThatWasExpanded, newNodes): # by default removes dublicate nodes if necessary
        for node in newNodes:
            if StateAnalyser.isGoalState(self, self.stage, node.state):
                self.goalNode = node

        nodePairsToHandle = []
        searchSpace = []
        searchSpace.extend(self.deadNodes)
        searchSpace.extend(self.activeNodes)
        for newNode in newNodes:
            sameNode = None
            for node in searchSpace: # check for duplicates in dead nodes
                if newNode.state.isTheSameStateAs(node.state):
                    nodePairsToHandle.append([newNode, node])
                    break
        self.handleDuplicateNodes(nodePairsToHandle, nodeThatWasExpanded, newNodes)
        

    def handleDuplicateNodes(self, nodesToHandle, nodeThatWasExpanded, allNewNodes): #nodesToHandle is an 2d array where [x][0] = newNode, [x][1] = oldNode
        for nodePair in nodesToHandle:
            self.handleADublicateNodePair(nodePair[1], nodePair[0], allNewNodes)

    def handleADublicateNodePair(self, oldNode, newNode, allNewNodes): # by default remove new duplicates
        allNewNodes.remove(newNode)


    def finishSearch(self):
        if self.goalNode is None:
            raise SearchException('Could not find path to goal state')
        else:
            self.actionsToGoalState = self.goalNode.getPathFromRoot()




class DepthFirstSearchTreePlayer(SearchTreePlayer):

    def popANodeToExpand(self):
        return self.activeNodes.pop()

class DijkstraSearchTreePlayer(SearchTreePlayer):

    def popANodeToExpand(self):
        reward = -10000
        nodeToExpand = None
        for node in self.activeNodes:
            if node.cumulatedReward > reward:
                reward = node.cumulatedReward
                nodeToExpand = node
        self.activeNodes.remove(nodeToExpand)
        return nodeToExpand


    def fixNewNodes(self, nodeThatWasExpanded, newNodes): # by default removes dublicate nodes if necessary
        if StateAnalyser.isGoalState(self, self.stage, nodeThatWasExpanded.state):
            self.goalNode = nodeThatWasExpanded

        nodePairsToHandle = []
        searchSpace = []
        searchSpace.extend(self.deadNodes)
        searchSpace.extend(self.activeNodes)
        for newNode in newNodes:
            sameNode = None
            for node in searchSpace: # check for duplicates in dead nodes
                if newNode.state.isTheSameStateAs(node.state):
                    nodePairsToHandle.append([newNode, node])
                    break
        self.handleDuplicateNodes(nodePairsToHandle, nodeThatWasExpanded, newNodes)


    def handleADublicateNodePair(self, oldNode, newNode, newNodes):
        if newNode.cumulatedReward > oldNode.cumulatedReward:
            oldNode.parent = newNode.parent
            oldNode.cumulatedReward = newNode.cumulatedReward
            oldNode.treeLayer = newNode.treeLayer
            oldNode.action = newNode.action
            oldNode.markers = newNode.markers
        newNodes.remove(newNode)
   
   


class AStarSearchTreePlayer(DijkstraSearchTreePlayer):

    cumulatedRewardWeight = 1
    heuresticWeight = 1

    def popANodeToExpand(self):
        bestValue = -10000
        nodeToExpand = None
        for node in self.activeNodes:
            value = node.cumulatedReward * self.cumulatedRewardWeight + self.calculateHeuresticForState(node.state) * self.heuresticWeight
            if value > bestValue:
                bestValue = value
                nodeToExpand = node
        self.activeNodes.remove(nodeToExpand)
        return nodeToExpand

    def calculateHeuresticForState(self, state):
        minCoinDistance = 1000
        for playerIndex in range(0, len(self.stage.players)):
            if self.stage.players[playerIndex] is self:
                ownPosition = state.playerPositions[playerIndex]
                for coinPos in state.coinPositions:
                    distance = ownPosition.calculateDistanceTo(coinPos) 
                    if distance < minCoinDistance:
                        minCoinDistance = distance

        return (1 / minCoinDistance)






class TreeNode:
    state = None
    cumulatedReward = 0
    action = None
    parent = None
    markers = None
    treeLayer = 0

    def __init__(self, state, parent, action, cumulatedReward, markers, treeLayer):
        self.state = state
        self.parent = parent
        self.action = action
        self.cumulatedReward = cumulatedReward
        self.treeLayer = treeLayer
        if markers is not None:
            self.markers = markers.copy()
        else:
            self.markers = []


    def getPathFromRoot(self):
        tempNode = self
        actions = []
        while tempNode.parent is not None:
            actions.append(tempNode.action)
            tempNode = tempNode.parent
        return actions



class SearchException(Exception):
    pass