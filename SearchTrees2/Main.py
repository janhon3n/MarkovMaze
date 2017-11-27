from Simulation import *
from Stage import *
from GameObject import *
from GameWindow import *
from StageParser import *

gameWindow = GameWindow('Simulation 1', 700, 480)

stage = StageParser.parseStage('stage1', gameWindow)

gameWindow.initGrid(stage)
gameWindow.drawState(stage.state)

for player in stage.players:
    player.initialize()
simulation = Simulation(stage)
simulation.addWindow(gameWindow)
simulation.play()