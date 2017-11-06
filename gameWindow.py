from graphics import *
from stage import *
from player import *

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
        gridBoxWidth = self.width / stage.colCount
        gridBoxHeight = self.height / stage.rowCount
        padding = gridBoxWidth * 0.2
        objects = stage.getObjects()
        for o in objects:
            x = o['position']['col']*gridBoxWidth + (gridBoxWidth / 2)
            y = o['position']['row']*gridBoxHeight + (gridBoxHeight / 2)
            if issubclass(type(o['object']), Player):
                c = Circle(Point(x, y), gridBoxWidth / 2 - padding)
                c.setWidth(3)
                c.draw(self)
                self.drawObjects.append(c)