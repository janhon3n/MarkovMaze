from GameWindow import *

class Simulation:
    stage = None
    gameWindow = None

    def __init__(self, stage):
        self.stage = stage

    def addWindow(self, gameWindow):
        self.gameWindow = gameWindow

    def play(self):
        self.playLoop()

        if self.gameWindow is not None:
            self.gameWindow.getMouse()

    def playLoop(self):
        while True:
            for player in self.stage.players:
                if self.stage.gameIsOver():
                    return
                player.move()
                if self.gameWindow is not None:
                    self.gameWindow.drawState(self.stage.state)
