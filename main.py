from simulation import *
from stage import *
from player import *
from bot import *
from gameWindow import *
import time


stage = Stage(16,22)
player = Player(stage)
stage.placeObject(player, {'row':1,'col':1})
gameWindow = GameWindow('Simulation 1', 700, 480)
gameWindow.initGrid(stage)
gameWindow.drawStage(stage)

time.sleep(5)

#simulation = Simulation(stage, player, ai)     