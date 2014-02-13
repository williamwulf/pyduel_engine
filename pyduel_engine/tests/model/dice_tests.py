
import unittest
from pyduel_engine.content.engine_states import Rolls
from pyduel_engine.model.dice import Dice


def suite():
    test_suites = unittest.TestSuite()
    test_suites.addTest(WhenTestingDice())
    return test_suites


class WhenTestingDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()

    def test_dice(self):
        self.assertIn(self.dice.print_result(), Rolls)

if __name__ == '__main__':
    unittest.main()