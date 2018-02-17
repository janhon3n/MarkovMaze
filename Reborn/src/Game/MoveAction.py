from Action import Action

class MoveAction(Action):

    direction = None

    def __init__(self, initiator, direction):
        super(MoveAction, self).__init__(self, initiator)
        self.direction = direction

    def execute(self, state):
        if self.direction == 'RIGHT':
            return self.moveRight(state)
        elif self.direction == 'UP:
            return self.moveUp(state)
        elif self.direction == 'LEFT':
            return self.moveLeft(state)
        elif self.direction == 'DOWN':
            return self.moveDown(state)

    def moveRight(self, state):
        

        if move == 'Stay':
            return False
        for i in range(0, len(self.players)):
            if self.players[i] is player:
                oldPosition = self.state.playerPositions[i]
                position = oldPosition.copy()
                oldObjectWasCoin = False
                for coinPos in self.state.coinPositions:
                    if oldPosition.isTheSamePositionAs(coinPos):
                        oldObjectWasCoin = True
                if move == 'Up':
                    position.row -= 1
                if move == 'Right':
                    position.col += 1
                if move == 'Down':
                    position.row += 1
                if move == 'Left':
                    position.col -= 1
                if not self.positionIsEmptyOfSolids(position):
                    raise StageException('Move is not allowed (blocked by other object)')
                if self.positionIsOutOfBounds(position):
                    raise StageException('Move is not allowed (out of bounds)')
                
                self.state.playerPositions[i] = position
                for coinPos in self.state.coinPositions:
                    if coinPos.isTheSamePositionAs(position):
                        self.state.coinPositions.remove(coinPos)
                        player.points += 1
                player.rotation = move
                return oldObjectWasCoin
