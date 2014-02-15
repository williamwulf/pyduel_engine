
import unittest

from pyduel_engine.content.engine_states import Character as Cs
from pyduel_engine.content.engine_states import Boards as Bs
from pyduel_engine.content.engine_states import Square as State
from pyduel_engine.utilities import board_utilities as bu


def suite():
    test_suites = unittest.TestSuite()
    test_suites.addTest(WhenTestingBoardUtilities())
    return test_suites


class WhenTestingBoardUtilities(unittest.TestCase):

    def setUp(self):
        self.char1 = {'name': 'main_1', 'hp': 18, 'is_main': True,
                      'max_hp': 18, 'type': Cs.main, 'state': State.light,
                      'pos': {'x': 0, 'y': 0}, 'deck': [], 'is_range': False}
        self.char2 = {'name': 'main_1', 'hp': 19, 'is_main': True,
                      'max_hp': 19, 'type': Cs.main, 'state': State.dark,
                      'pos': {'x': 6, 'y': 6}, 'deck': [], 'is_range': False}

        self.board = {'board_type': Bs.board, 'max_x': 10, 'max_y': 7,
                      'board': [[State.empty for y in range(0, 7)]
                                for x in range(0, 10)]}
