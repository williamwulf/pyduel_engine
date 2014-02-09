
import random

from pyduel_engine.content.engine_states import Rolls


class Dice(object):

    def __init__(self, sides=5):
        self.sides = sides
        self.result = self.roll()

    def print_result(self):
        return Rolls[self.result]

    def roll(self):
        self.result = Rolls[random.randint(0, self.sides)]
        return self.result
