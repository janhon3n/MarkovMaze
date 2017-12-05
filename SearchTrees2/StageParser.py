from Stage import *
from GameObject import *
from Stage import *
from SearchTreePlayer import *
from UpdatingSearchTreePlayer import *
import glob, os

# Creates a stage from a file
# File structure:
#
# first line:
# [Playertype],[Enemytype]
#
# rest of the file:
# object positions coded with the following letters
# _ = nothing
# P = player
# C = coin
# W = wall

class StageParser:

  @staticmethod
  def getListOfStages():
    stages = []
    for file in glob.glob("../stages/*.mmstg"):
      stages.append(file.split("\\").pop().split("/").pop().split(".")[0]) 
    return stages
      


  @staticmethod
  def parseStage(stagename, gameWindow):
    file = open('../stages/'+stagename+'.mmstg', 'r')
    data = file.read()
    rows = [s.strip() for s in data.splitlines()]
    firstRow = rows[0]
    rows.remove(firstRow)
    playerCommands = firstRow.split(' ')
    players = []
    for playerCommand in playerCommands:
      [playerType, argString] = playerCommand.split('/')
      args = argString.split(',')
      players.append([playerType, args])

    rowCount = len(rows)
    colCount = len(rows[0])
    
    stage = Stage(rowCount, colCount)
    for rowNumber in range(0, rowCount):
      for colNumber in range(0, colCount):
        position = Position(rowNumber, colNumber)

        if rows[rowNumber][colNumber] == '1':
          player = StageParser.createNewPlayer(players[0], stage, gameWindow)
          stage.placeObject(player, position)
        if rows[rowNumber][colNumber] == '2':
          player = StageParser.createNewPlayer(players[1], stage, gameWindow)
          stage.placeObject(player, position)
        if rows[rowNumber][colNumber] == '3':
          player = StageParser.createNewPlayer(players[2], stage, gameWindow)
          stage.placeObject(player, position)
        if rows[rowNumber][colNumber] == '4':
          player = StageParser.createNewPlayer(players[3], stage, gameWindow)
          stage.placeObject(player, position)
        if rows[rowNumber][colNumber] == '5':
          player = StageParser.createNewPlayer(players[4], stage, gameWindow)
          stage.placeObject(player, position)
        if rows[rowNumber][colNumber] == 'C':
          coin = Coin(stage)
          stage.placeObject(coin, position) 
        
        if rows[rowNumber][colNumber] == 'W':
          wall = Wall(stage)
          stage.placeObject(wall, position)
    return stage

  @staticmethod
  def createNewPlayer(playerData, stage, gameWindow):
    if playerData[0] == 'Human':
      return HumanPlayer(stage, gameWindow)
    if playerData[0] == 'SearchTree' or playerData[0] == 'BredthFirstSearchTree' or playerData[0] == 'BredthFirst':
      return SearchTreePlayer(stage, gameWindow)
    if playerData[0] == 'DepthFirstSearchTree' or playerData[0] == 'DepthFirst':
      return DepthFirstSearchTreePlayer(stage, gameWindow)
    if playerData[0] == 'DijkstraSearchTree' or playerData[0] == 'Dijkstra':
      return DijkstraSearchTreePlayer(stage, gameWindow)
    if playerData[0] == 'AStarSearchTree' or playerData[0] == 'AStar':
      return AStarSearchTreePlayer(stage, gameWindow)
    if playerData[0] == 'UpdatingSearchTree':
      return UpdatingSearchTreePlayer(stage, gameWindow)
#    if playerData[0] == 'MinMax':
#      return MinMaxPlayer(stage, int(playerData[1][0]), float(playerData[1][1]))
    raise StageParsingException('Undefined playertype')



class StageParsingException(Exception):
  pass
