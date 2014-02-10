
import unittest
from epicduels.content import game_state as GS
from epicduels.initializers import initializer as init
from epicduels.rules import board_rules as BR


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WhenTestingCardRules())
    return suite


class WhenTestingCardRules(unittest.TestCase):

    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()
