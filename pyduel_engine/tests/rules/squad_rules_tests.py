__author__ = 'aelkikhia'


import unittest

from pyduel_engine.content.engine_states import Character as Cs
from pyduel_engine.content.engine_states import Square as State
from pyduel_engine.content.engine_states import Player
from pyduel_engine.rules import squad_rules as sr


def suite():
    suites = unittest.TestSuite()
    suites.addTest(WhenTestingSquadRules())
    return suites


class WhenTestingSquadRules(unittest.TestCase):

    def setUp(self):
        self.main_1l = {'name': 'main_1', 'hp': 18, 'is_main': True,
                        'max_hp': 18, 'type': Cs.main, 'state': State.light,
                        'pos': {'x': 0, 'y': 0}, 'deck': [], 'is_range': False}

        self.minor_1l = {'name': 'minor_1', 'hp': 4, 'is_main': True,
                         'max_hp': 4, 'type': Cs.minor_1, 'state': State.dark,
                         'pos': {'x': 6, 'y': 6}, 'deck': [], 'is_range': True}

        self.minor_2l = {'name': 'minor_2', 'hp': 4, 'is_main': True,
                         'max_hp': 4, 'type': Cs.minor_2,
                         'state': State.light,
                         'pos': {'x': 0, 'y': 0}, 'deck': [], 'is_range': True}

        self.main_2d = {'name': 'main_1', 'hp': 19, 'is_main': True,
                        'max_hp': 19, 'type': Cs.main, 'state': State.dark,
                        'pos': {'x': 6, 'y': 6}, 'deck': [], 'is_range': False}

        self.minor_1d = {'name': 'minor_1', 'hp': 4, 'is_main': True,
                         'max_hp': 4, 'type': Cs.minor_1, 'state': State.dark,
                         'pos': {'x': 0, 'y': 0}, 'deck': [], 'is_range': True}
        self.minor_2d = {'name': 'minor_2', 'hp': 4, 'is_main': True,
                         'max_hp': 4, 'type': Cs.minor_2, 'state': State.dark,
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

    def are_minors_dead_false_both_alive(self):
        self.assertFalse(sr.are_minors_dead(self.squad1))

    def are_minors_dead_test_false_one_dead(self):
        self.minor_1l['hp'] = 4
        self.minor_2l['hp'] = 0
        self.squad1['characters'] = [self.main_1l,
                                     self.minor_1l,
                                     self.minor_2l]
        self.assertFalse(sr.are_minors_dead(self.squad1))

    def are_minors_dead_test_true_both_dead(self):
        self.minor_1l['hp'] = 0
        self.minor_2l['hp'] = 0
        self.squad1['characters'] = [self.main_1l,
                                     self.minor_1l,
                                     self.minor_2l]
        self.assertTrue(sr.are_minors_dead(self.squad1))

    def test_can_act_true(self):
        self.assertTrue(sr.can_act(self.squad1))

    def test_can_act_false(self):
        self.squad1['actions'] = 0
        self.assertFalse(sr.can_act(self.squad1))

    def test_can_play_card_false_no_actions(self):
        self.squad1['actions'] = 0
        self.assertFalse(sr.can_play_card(self.squad1))

    def test_can_play_card_false_no_cards(self):
        self.assertFalse(sr.can_play_card(self.squad1))

    def test_can_play_card_true(self):
        self.squad1['hand'].append({'test_card': None})
        self.assertTrue(sr.can_play_card(self.squad1))


if __name__ == '__main__':
    unittest.main()