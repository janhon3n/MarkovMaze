from SimulationListener import SimulationListener

class Simulation:
    stage = None
    listeners = None

    def __init__(self, stage):
        self.stage = stage
        self.listeners = []

    def addListener(self, listener: SimulationListener):
        self.listeners.append(listener)

    def play(self):
        self.playLoop()

    def playLoop(self):
        while True:
            for player in self.stage.agents:
                if self.stage.gameIsOver():
                    return
                player.move()
                if self.listeners.count is not 0:
                    for listener in self.listeners:
                        listener.update(self.stage.state)
