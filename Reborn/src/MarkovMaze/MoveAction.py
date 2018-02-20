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

    def moveRight(self, state: GameState) -> GameState:
        self