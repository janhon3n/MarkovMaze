from simulation import *
from stage import *
from player import *
from pathFinderPlayer import *
from gameWindow import *
from coin import *
from wall import *
import time


stage = Stage(6,8)
gameWindow = GameWindow('Simulation 1', 700, 480)
player = PathFinderPlayer(stage, gameWindow)

stage.placePlayer(player, {'row':0,'col':0})

stage.placeObject(Coin(5), {'row':2,'col':1})
stage.placeObject(Coin(5), {'row':3,'col':5})
stage.placeObject(Coin(5), {'row':4,'col':5})
stage.placeObject(Coin(5), {'row':5,'col':3})
stage.placeObject(Coin(5), {'row':3,'col':7})
stage.placeObject(Wall(stage), {'row':2, 'col':2})
stage.placeObject(Wall(stage), {'row':3, 'col':4})
stage.placeObject(Wall(stage), {'row':5, 'col':4})
stage.placeObject(Wall(stage), {'row':4, 'col':5})

gameWindow.initGrid(stage.state)
gameWindow.drawState(stage.state)

player.findPath()
simulation = Simulation(stage)
simulation.addWindow(gameWindow)
simulation.play()

#simulation = Simulation(stage, player, ai)     