__author__ = 'aelkikhia'


import unittest
from pyduel_engine.rules import squad_rules as sr


def suite():
    test_suites = unittest.TestSuite()
    test_suites.addTest(WhenTestingSquadRules())
    return test_suites


class WhenTestingSquadRules(unittest.TestCase):

    def setUp(self):
        self.main_character = {'name': 'main', 'hp': 20, 'is_main': True,
                               'max_hp': 20, 'type': 'main', 'state': 'light',
                               'pos': None, 'is_range': False, 'deck': []}
        self.minor_1 = {'name': 'minor_1', 'hp': 4, 'is_main': False,
                        'max_hp': 4, 'type': 'minor_1', 'state': 'light',
                        'pos': None, 'is_range': True, 'deck': []}
        self.minor_2 = {'name': 'minor_2', 'hp': 4, 'is_main': False,
                        'max_hp': 4, 'type': 'minor_2', 'state': 'light',
                        'pos': None, 'is_range': True, 'deck': []}
        self.squad = {'player': 0, 'characters': [self.main_character,
                                                  self.minor_1, self.minor_2],
                      'actions': 2, 'deck': [], 'hand': [], 'discard': [],
                      'side': 'light'}

    def are_minors_dead_test_false(self):
        self.assertFalse(sr.are_minors_dead(self.squad))

    def are_minors_dead_test_true_both_dead(self):
        self.minor_1['hp'] = 0
        self.minor_2['hp'] = 0
        self.squad['characters'] = [self.main_character,
                                    self.minor_1,
                                    self.minor_2]
        self.assertTrue(sr.are_minors_dead(self.squad))

    def are_minors_dead_test_false_one_dead(self):
        self.minor_1['hp'] = 4
        self.minor_2['hp'] = 0
        self.squad['characters'] = [self.main_character,
                                    self.minor_1,
                                    self.minor_2]
        self.assertFalse(sr.are_minors_dead(self.squad))


if __name__ == '__main__':
    unittest.main()
