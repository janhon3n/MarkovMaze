from Simulation import *
from Stage import *
from GameObject import *
from GameWindow import *
from StageParser import *
import sys
import traceback

gameWindow = None
while True:
    stages = StageParser.getListOfStages()
    try:
        gameWindow = GameWindow('PathFindingSimulator', 960, 480)
        stageIndex = self.askUserForStageIndex()
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
        traceback.print_tb(ex.__traceback__)
    
    if gameWindow is not None:
        gameWindow.close()
        gameWindow = None


def askUserForStageIndex(self):
    for i in range(0, len(stages)):
        print(str(i) + ". "+stages[i])
    userInput = input("Choose a stage: ")
    stageIndex = int(userInput)
    if stageIndex < 0 or stageIndex >= len(stages):
        raise ValueError('User input invalid')
    return stageIndex
