
import unittest

from pyduel_engine.content.engine_states import Character as Cs
from pyduel_engine.content.engine_states import Square as State
from pyduel_engine.content.engine_states import Player


def suite():
    test_suites = unittest.TestSuite()
    test_suites.addTest(WhenTestingGameRules())
    return test_suites


class WhenTestingGameRules(unittest.TestCase):

    def setUp(self):
        self.main_1l = {'name': 'main_1', 'hp': 18, 'is_main': True,
                        'max_hp': 18, 'type': Cs.main, 'state': State.light,
                        'pos': {'x': 0, 'y': 0}, 'deck': [], 'is_range': False}

        self.minor_1l = {'name': 'minor_1', 'hp': 19, 'is_main': True,
                         'max_hp': 19, 'type': Cs.minor_1, 'state': State.dark,
                         'pos': {'x': 6, 'y': 6}, 'deck': [], 'is_range': True}

        self.minor_2l = {'name': 'minor_2', 'hp': 18, 'is_main': True,
                         'max_hp': 18, 'type': Cs.minor_2,
                         'state': State.light,
                         'pos': {'x': 0, 'y': 0}, 'deck': [], 'is_range': True}

        self.main_2d = {'name': 'main_1', 'hp': 19, 'is_main': True,
                        'max_hp': 19, 'type': Cs.main, 'state': State.dark,
                        'pos': {'x': 6, 'y': 6}, 'deck': [], 'is_range': False}

        self.minor_1d = {'name': 'minor_1', 'hp': 18, 'is_main': True,
                         'max_hp': 18, 'type': Cs.minor_1, 'state': State.dark,
                         'pos': {'x': 0, 'y': 0}, 'deck': [], 'is_range': True}
        self.minor_2d = {'name': 'minor_2', 'hp': 19, 'is_main': True,
                         'max_hp': 19, 'type': Cs.minor_2, 'state': State.dark,
                         'pos': {'x': 6, 'y': 6}, 'deck': [], 'is_range': True}

        self.squad1 = {'player': Player.player_1,
                       'characters': [self.main_1l,
                                      self.minor_1l,
                                      self.minor_2l],
                       'actions': 2,
                       'deck': [],
                       'hand': [],
                       'discard': [],
                       'side': State.light}

        self.squad2 = {'player': Player.player_2,
                       'characters': [self.main_2d,
                                      self.minor_2d,
                                      self.minor_2d],
                       'actions': 2,
                       'deck': [],
                       'hand': [],
                       'discard': [],
                       'side': State.dark}
