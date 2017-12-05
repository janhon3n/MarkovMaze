from graphics import *
from Stage import *
from State import *
from GameObject import *
import time

class GameWindow(GraphWin):
    drawObjects = []
    pauseAfterRender = 0.005
    stage = None

    def __init__(self, title, width, height):
        super(GameWindow, self).__init__(title, width, height)

    def initGrid(self, stage):
        for i in range(stage.colCount-1):
            l = Line(Point((self.width / stage.colCount)*(i+1), 0), Point((self.width/stage.colCount)*(i+1), self.height))
            l.draw(self)

        for i in range(stage.rowCount-1):
            l = Line(Point(0, (self.height / stage.rowCount)*(i+1)), Point(self.width, (self.height / stage.rowCount) * (i+1)))
            l.draw(self)

        for i in range(0, stage.rowCount):
            for j in range(0, stage.colCount):
                if stage.walls[i][j]:
                    rect = Rectangle(Point((self.width / stage.colCount)*(j), (self.height / stage.rowCount)*(i)), Point((self.width / stage.colCount)*(j+1), (self.height / stage.rowCount)*(i+1)))
                    rect.setFill("black")
                    rect.draw(self)

        self.stage = stage
                



    def drawState(self, state):
        self.clearState()
        rowCount = self.stage.rowCount
        colCount = self.stage.colCount
        gridBoxWidth = self.width / colCount
        gridBoxHeight = self.height / rowCount
        padding = gridBoxWidth * 0.2

        drawBoxSideLength = min(gridBoxWidth, gridBoxHeight) - padding

        for position in state.coinPositions:
            x = position.col*gridBoxWidth + (gridBoxWidth / 2)
            y = position.row*gridBoxHeight + (gridBoxHeight / 2)
            circle = Circle(Point(x,y), drawBoxSideLength / 4)
            circle.setWidth(2)
            circle.setFill("yellow")
            circle.draw(self)
            self.drawObjects.append(circle)

        for playerNum in range(0, len(self.stage.players)):
            x = state.playerPositions[playerNum].col*gridBoxWidth + (gridBoxWidth / 2)
            y = state.playerPositions[playerNum].row*gridBoxHeight + (gridBoxHeight / 2)
            rotation = self.stage.players[playerNum].rotation

            circle = Circle(Point(x, y), drawBoxSideLength / 2)
            circle.setWidth(3)
            circle.setFill(Stage.getPlayerColors()[playerNum])
            
            line1 = None
            line2 = None
            if rotation == 'Up':
                line1 = Line(Point(x+(drawBoxSideLength / 7), y - (drawBoxSideLength / 2)), Point(x+(drawBoxSideLength / 7), y - (drawBoxSideLength / 2.5) + (drawBoxSideLength / 5)))
                line2 = Line(Point(x-(drawBoxSideLength / 7), y - (drawBoxSideLength / 2)), Point(x-(drawBoxSideLength / 7), y - (drawBoxSideLength / 2.5) + (drawBoxSideLength / 5)))
            if rotation == 'Down':
                line1 = Line(Point(x+(drawBoxSideLength / 7), y + (drawBoxSideLength / 2)), Point(x+(drawBoxSideLength / 7), y + (drawBoxSideLength / 2.5) - (drawBoxSideLength / 5)))
                line2 = Line(Point(x-(drawBoxSideLength / 7), y + (drawBoxSideLength / 2)), Point(x-(drawBoxSideLength / 7), y + (drawBoxSideLength / 2.5) - (drawBoxSideLength / 5)))
            if rotation == 'Left':
                line1 = Line(Point(x-(drawBoxSideLength / 2), y + (drawBoxSideLength / 7)), Point(x-(drawBoxSideLength / 2.5) + (drawBoxSideLength / 5), y + (drawBoxSideLength / 7)))
                line2 = Line(Point(x-(drawBoxSideLength / 2), y - (drawBoxSideLength / 7)), Point(x-(drawBoxSideLength / 2.5) + (drawBoxSideLength / 5), y - (drawBoxSideLength / 7)))
            if rotation == 'Right':
                line1 = Line(Point(x+(drawBoxSideLength / 2), y + (drawBoxSideLength / 7)), Point(x+(drawBoxSideLength / 2.5) - (drawBoxSideLength / 5), y + (drawBoxSideLength / 7)))
                line2 = Line(Point(x+(drawBoxSideLength / 2), y - (drawBoxSideLength / 7)), Point(x+(drawBoxSideLength / 2.5) - (drawBoxSideLength / 5), y - (drawBoxSideLength / 7)))

            line1.setWidth(3)
            line2.setWidth(3)
            circle.draw(self)
            line1.draw(self)
            line2.draw(self)
            
            pointText = Text(Point(x,y), str(self.stage.players[playerNum].points))
            pointText.draw(self)

            self.drawObjects.append(circle)
            self.drawObjects.append(line1)
            self.drawObjects.append(line2)
            self.drawObjects.append(pointText)
        time.sleep(self.pauseAfterRender)

    def drawStateWithMarkers(self, state, markers):
        rowCount = self.stage.rowCount
        colCount = self.stage.colCount
        gridBoxWidth = self.width / colCount
        gridBoxHeight = self.height / rowCount
        padding = gridBoxWidth * 0.2
        
        drawBoxSideLength = min(gridBoxWidth, gridBoxHeight) - padding
        
        self.drawState(state)
        for marker in markers:
            x = marker.col*gridBoxWidth + (gridBoxWidth / 2)
            y = marker.row*gridBoxHeight + (gridBoxHeight / 2)
            circle = Circle(Point(x,y), drawBoxSideLength / 8)
            circle.setWidth(2)
            circle.setFill("red")
            circle.draw(self)
            self.drawObjects.append(circle)

    def clearState(self):
        for drawObject in self.drawObjects:
            drawObject.undraw()
        self.drawObjects.clear()