from simulation import *
from stage import *
from player import *
from pathFinderPlayer import *
from gameWindow import *
from coin import *
from wall import *
from stageParser import *
import time


gameWindow = GameWindow('Simulation 1', 700, 480)
stage = StageParser.parseStage('stage1', gameWindow)

gameWindow.initGrid(stage.state)
gameWindow.drawState(stage.state)

for player in stage.players:
    player.initialize()
simulation = Simulation(stage)
simulation.addWindow(gameWindow)
simulation.play()

#simulation = Simulation(stage, player, ai)     