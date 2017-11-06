from graphics import *
from stage import *
from player import *
from coin import *

class GameWindow(GraphWin):
    drawObjects = []

    def __init__(self, title, width, height):
        super(GameWindow, self).__init__(title, width, height)

    def initGrid(self, stage):
        for i in range(stage.colCount-1):
            l = Line(Point((self.width / stage.colCount)*(i+1), 0), Point((self.width/stage.colCount)*(i+1), self.height))
            l.draw(self)

        for i in range(stage.rowCount-1):
            l = Line(Point(0, (self.height / stage.rowCount)*(i+1)), Point(self.width, (self.height / stage.rowCount) * (i+1)))
            l.draw(self)


    def drawStage(self, stage):
        self.clearStage()
        gridBoxWidth = self.width / stage.colCount
        gridBoxHeight = self.height / stage.rowCount
        padding = gridBoxWidth * 0.2
        drawBoxSideLength = min(gridBoxWidth, gridBoxHeight) - padding
        objects = stage.getObjects()
        for o in objects:
            x = o['position']['col']*gridBoxWidth + (gridBoxWidth / 2)
            y = o['position']['row']*gridBoxHeight + (gridBoxHeight / 2)
            if issubclass(type(o['object']), Player):
                circle = Circle(Point(x, y), drawBoxSideLength / 2)
                circle.setWidth(3)
                circle.setFill("lightblue")
                line1 = None
                line2 = None
                if o['object'].rotation == 'Up':
                    line1 = Line(Point(x+(drawBoxSideLength / 7), y - (drawBoxSideLength / 2)), Point(x+(drawBoxSideLength / 7), y - (drawBoxSideLength / 2.5) + (drawBoxSideLength / 3)))
                    line2 = Line(Point(x-(drawBoxSideLength / 7), y - (drawBoxSideLength / 2)), Point(x-(drawBoxSideLength / 7), y - (drawBoxSideLength / 2.5) + (drawBoxSideLength / 3)))
                if o['object'].rotation == 'Down':
                    line1 = Line(Point(x+(drawBoxSideLength / 7), y + (drawBoxSideLength / 2)), Point(x+(drawBoxSideLength / 7), y + (drawBoxSideLength / 2.5) - (drawBoxSideLength / 3)))
                    line2 = Line(Point(x-(drawBoxSideLength / 7), y + (drawBoxSideLength / 2)), Point(x-(drawBoxSideLength / 7), y + (drawBoxSideLength / 2.5) - (drawBoxSideLength / 3)))
                if o['object'].rotation == 'Left':
                    line1 = Line(Point(x-(drawBoxSideLength / 2), y + (drawBoxSideLength / 7)), Point(x-(drawBoxSideLength / 2.5) + (drawBoxSideLength / 3), y + (drawBoxSideLength / 7)))
                    line2 = Line(Point(x-(drawBoxSideLength / 2), y - (drawBoxSideLength / 7)), Point(x-(drawBoxSideLength / 2.5) + (drawBoxSideLength / 3), y - (drawBoxSideLength / 7)))
                if o['object'].rotation == 'Right':
                    line1 = Line(Point(x+(drawBoxSideLength / 2), y + (drawBoxSideLength / 7)), Point(x+(drawBoxSideLength / 2.5) - (drawBoxSideLength / 3), y + (drawBoxSideLength / 7)))
                    line2 = Line(Point(x+(drawBoxSideLength / 2), y - (drawBoxSideLength / 7)), Point(x+(drawBoxSideLength / 2.5) - (drawBoxSideLength / 3), y - (drawBoxSideLength / 7)))

                line1.setWidth(3)
                line2.setWidth(3)
                circle.draw(self)
                line1.draw(self)
                line2.draw(self)
                
                self.drawObjects.append(circle)
                self.drawObjects.append(line1)
                self.drawObjects.append(line2)
            if issubclass(type(o['object']), Coin):
                circle = Circle(Point(x,y), drawBoxSideLength / 4)
                circle.setWidth(2)
                circle.setFill("yellow")
                circle.draw(self)
                self.drawObjects.append(circle)

    def clearStage(self):
        for drawObject in self.drawObjects:
            drawObject.undraw()
        self.drawObjects.clear()