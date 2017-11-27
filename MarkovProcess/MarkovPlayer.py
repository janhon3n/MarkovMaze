from Player import *
import numpy as numpy

class MarkovPlayer(Player):

    policyMatrix = None
    qVector = None

    def initialize(self):
        self.policyMatrix = numpy.zeros((3,4))
        self.qVector = numpy.zeros((5, 1))
        print(self.policyMatrix)

    def move(self):
        self.stage.movePlayer(self, 'Up')