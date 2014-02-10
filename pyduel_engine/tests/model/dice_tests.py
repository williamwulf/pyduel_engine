
import unittest
from epicduels.content import game_state as GS
from epicduels.model.dice import Dice


class WhenTestingDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()

    def test_dice(self):
        self.assertIn(self.dice.print_result(), GS.ROLLS)
