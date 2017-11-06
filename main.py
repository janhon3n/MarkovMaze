from simulation import *
from stage import *
from player import *
from bot import *
from gameWindow import *
from coin import *
import time


stage = Stage(8,14)
gameWindow = GameWindow('Simulation 1', 700, 480)
player = HumanPlayer(stage, gameWindow)
stage.placePlayer(player, {'row':1,'col':1})
coin = Coin(5)
stage.placeObject(coin, {'row':3,'col':6})

gameWindow.initGrid(stage)
gameWindow.drawStage(stage)

simulation = Simulation(stage)
simulation.addWindow(gameWindow)
simulation.play()

#simulation = Simulation(stage, player, ai)     