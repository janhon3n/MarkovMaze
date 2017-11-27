from GameObject import *
from Stage import *
import time

class SearchTreePlayer(Player):

    activeNodes = None
    deadNodes = None
    pathToGoalState = None
    gameWindow = None

    def __init__(self, stage, gameWindow):
        super().__init__(stage)
        self.gameWindow = gameWindow

    def move(self):
        self.stage.executePlayerMove(self, self.pathToGoalState.pop())
        time.sleep(0.1)

    def initialize(self):
        self.activeNodes = []
        self.moveToGoalState = []
        self.deadNodes = []
        self.findPathToGoalState()


    def findPathToGoalState(self):
        self.activeNodes.append(TreeNode(self.stage.state.copy(), None, None, 0, None))
        while len(self.activeNodes) > 0:
            nodeToExpand = self.popANodeToExpand()
            if self.gameWindow is not None:
                self.gameWindow.drawStateWithMarkers(nodeToExpand.state, nodeToExpand.markers)
            newNodes = self.expandNode(nodeToExpand)
            self.deadNodes.append(nodeToExpand)
            if self.checkGoalCondition(nodeToExpand, newNodes):
                return
            self.checkIfAnyNodesAlreadyInTree(newNodes)
            self.activeNodes.extend(newNodes)
            print("Dead nodes: "+str(len(self.deadNodes)) + ", Active nodes: "+str(len(self.activeNodes)))
        raise SearchException('Could not find path to goal state')
        

    def checkIfAnyNodesAlreadyInTree(self, nodes): # removes dublicate nodes if necessary
        nodesToHandle = []
        for node in nodes:
            sameNode = None
            for deadNode in self.deadNodes:
                if node.state.isTheSameStateAs(deadNode.state):
                    sameNode = deadNode
                    break
            if sameNode is None:
                for activeNode in self.activeNodes:
                    if node.state.isTheSameStateAs(activeNode.state):
                        sameNode = activeNode
                        break
            if sameNode is not None:
                nodesToHandle.append([node, sameNode])
        for n in nodesToHandle:
            self.handleDublicateNodes(n[1],n[0], nodes)
        
    def handleDublicateNodes(self, oldNode, newNode, newNodes):
        newNodes.remove(newNode)


    def getPathFromRoot(self, node):
        tempNode = node
        moves = []
        while tempNode.parent is not None:
            moves.append(tempNode.move)
            tempNode = tempNode.parent
        return moves

    def expandNode(self, node):
        for playerIndex in range(0, len(self.stage.players)):
            if self is self.stage.players[playerIndex]:
                newNodes = []
                oldPosition = node.state.playerPositions[playerIndex]
                moveVectors = [['Up',-1,0],['Right',0,1],['Down',1,0],['Left',0,-1]]
                for moveVector in moveVectors:
                    newPos = Position(oldPosition.row + moveVector[1], oldPosition.col + moveVector[2])
                    if self.checkThatPositionIsEmptyOfSolidsInState(node.state, newPos):
                        newNode = TreeNode(node.state.copy(), node, moveVector[0], node.cumulatedReward, node.markers)
                        newNode.state.playerPositions[playerIndex] = newPos
                        newNode.markers.append(oldPosition.copy())
                        playerGotCoin = False
                        for coinPos in newNode.state.coinPositions:
                            if coinPos.isTheSamePositionAs(newPos):
                                playerGotCoin = True
                                newNode.state.coinPositions.remove(coinPos)
                                break
                            if playerGotCoin:
                                newNode.cumulatedReward += 1
                        newNodes.append(newNode)
                return newNodes

    def checkThatPositionIsEmptyOfSolidsInState(self, state, position):
        if position.row < 0 or position.row > self.stage.rowCount -1 or position.col < 0 or position.col > self.stage.colCount -1:
            return False
        if not self.stage.walls[position.row][position.col]: # if there is no wall
            emptyOfPlayer = True
            for playerPos in state.playerPositions:
                if playerPos.isTheSamePositionAs(position):
                    emptyOfPlayer = False
            if emptyOfPlayer: # and there is no player
                return True
        return False


    def popANodeToExpand(self):
        return self.activeNodes.pop(0)

    def checkGoalCondition(self, nodeToExpand, newNodes):
        for node in newNodes:
            if len(node.state.coinPositions) == 0:
                self.pathToGoalState = self.getPathFromRoot(node)
                return True
        return False
    

class DepthFirstSearchTreePlayer(SearchTreePlayer):
    
    def popANodeToExpand(self):
        return self.activeNodes.pop()

class TreeNode:
    state = None
    cumulatedReward = 0
    move = None
    parent = None
    markers = None

    def __init__(self, state, parent, move, cumulatedReward, markers):
        self.state = state
        self.parent = parent
        self.move = move
        self.cumulatedReward = cumulatedReward
        if markers is not None:
            self.markers = markers.copy()
        else:
            self.markers = []


class SearchException(Exception):
    pass