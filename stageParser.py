from stage import *
from pathFinderPlayer import *
from player import *
from wall import *
from coin import *

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
  def parseStage(stagename, gameWindow):
    file = open('stages/'+stagename+'.mmstg', 'r')
    data = file.read()
    rows = [s.strip() for s in data.splitlines()]
    firstRow = rows[0]
    rows.remove(firstRow)
    [playerType, enemyType] = firstRow.split(',')
    
    rowCount = len(rows)
    colCount = len(rows[0])
    
    stage = Stage(rowCount, colCount)
    for rowNumber in range(0, rowCount):
      for colNumber in range(0, colCount):
        position = {'row':rowNumber, 'col':colNumber}

        if rows[rowNumber][colNumber] == 'P':
          if playerType == 'PathFinder':
            player = PathFinderPlayer(stage, gameWindow)
            stage.placePlayer(player, position)
        
        if rows[rowNumber][colNumber] == 'C':
          coin = Coin(stage)
          stage.placeObject(coin, position) 
        
        if rows[rowNumber][colNumber] == 'W':
          wall = Wall(stage)
          stage.placeObject(wall, position)
    return stage
