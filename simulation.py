from gameWindow import *

class Simulation:
    stage = None
    gameWindow = None

    def __init__(self, stage):
        self.stage = stage

    def addWindow(self, gameWindow):
        self.gameWindow = gameWindow

    def play(self):
        while not self.stage.gameIsOver():
            self.stage.player.move()

            if self.gameWindow is not None:
                self.gameWindow.drawState(self.stage.state) 
        if self.gameWindow is not None:
            self.gameWindow.getMouse()