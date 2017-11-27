from Simulation import *
from Stage import *
from GameObject import *
from GameWindow import *
from StageParser import *
import sys

gameWindow = None
stages = StageParser.getListOfStages()
while True:
    try:
        for i in range(0, len(stages)):
            print(str(i) + ". "+stages[i])

        userInput = input("Choose a stage: ")
        stageIndex = int(userInput)
        gameWindow = GameWindow('PathFindingSimulator', 700, 480)
        stage = StageParser.parseStage(stages[stageIndex], gameWindow)

        gameWindow.initGrid(stage)
        gameWindow.drawState(stage.state)

        for player in stage.players:
            player.initialize()
        simulation = Simulation(stage)
        simulation.addWindow(gameWindow)
        simulation.play()
    except Exception as ex:
        print(ex)
    
    if gameWindow is not None:
        gameWindow.close()
        gameWindow = None