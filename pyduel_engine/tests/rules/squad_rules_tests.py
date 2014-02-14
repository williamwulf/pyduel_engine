
import unittest

from pyduel_engine.content.engine_states import Character as Ch
from pyduel_engine.content.engine_states import Card
from pyduel_engine.content.engine_states import Square as State
from pyduel_engine.content.engine_states import Player
from pyduel_engine.rules import squad_rules as sr


def suite():
    suites = unittest.TestSuite()
    suites.addTest(WhenTestingSquadRules())
    return suites


class WhenTestingSquadRules(unittest.TestCase):

    def setUp(self):
        self.main_l = {'name': 'main_1', 'hp': 18, 'is_main': True,
                       'max_hp': 18, 'type': Ch.main, 'state': State.light,
                       'pos': {'x': 0, 'y': 0}, 'deck': [], 'is_range': False}

        self.minor_1l = {'name': 'minor_1', 'hp': 4, 'is_main': False,
                         'max_hp': 4, 'type': Ch.minor, 'state': State.dark,
                         'pos': {'x': 6, 'y': 6}, 'deck': [], 'is_range': True}

        self.minor_2l = {'name': 'minor_2', 'hp': 4, 'is_main': False,
                         'max_hp': 4, 'type': Ch.minor,
                         'state': State.light,
                         'pos': {'x': 0, 'y': 0}, 'deck': [], 'is_range': True}

        self.main_2d = {'name': 'main_1', 'hp': 19, 'is_main': True,
                        'max_hp': 19, 'type': Ch.main, 'state': State.dark,
                        'pos': {'x': 6, 'y': 6}, 'deck': [], 'is_range': False}

        self.minor_1d = {'name': 'minor_1', 'hp': 4, 'is_main': False,
                         'max_hp': 4, 'type': Ch.minor, 'state': State.dark,
                         'pos': {'x': 0, 'y': 0}, 'deck': [], 'is_range': True}
        self.minor_2d = {'name': 'minor_2', 'hp': 4, 'is_main': False,
                         'max_hp': 4, 'type': Ch.minor, 'state': State.dark,
                         'pos': {'x': 6, 'y': 6}, 'deck': [], 'is_range': True}

        self.minor_combat = {'type': Card.combat, 'name': 'combat',
                             'attack': 5, 'defense': 1, 'owner': Ch.minor,
                             'description': ''}

        self.main_combat = {'type': Card.combat, 'name': 'combat',
                            'attack': 5, 'defense': 1, 'owner': Ch.main,
                            'description': ''}

        self.main_special = {'type': Card.special, 'name': 'combat',
                             'attack': 5, 'defense': 1, 'owner': Ch.main,
                             'description': ''}

        self.main_pa = {'type': Card.power_attack, 'name': 'combat',
                        'attack': 5, 'defense': 1, 'owner': Ch.main,
                        'description': ''}

        self.main_pd = {'type': Card.power_defense, 'name': 'combat',
                        'attack': 5, 'defense': 1, 'owner': Ch.main,
                        'description': ''}

        self.squad1 = {'player': Player.player_1,
                       'characters': [self.main_l, self.minor_1l,
                                      self.minor_2l],
                       'actions': 2, 'can_draw': True, 'deck': [], 'hand': [],
                       'discard': [], 'side': State.light}

        self.squad2 = {'player': Player.player_2,
                       'characters': [self.main_2d,
                                      self.minor_2d,
                                      self.minor_2d],
                       'actions': 2, 'can_draw': True, 'deck': [], 'hand': [],
                       'discard': [], 'side': State.dark}

    ######################## can_act(squad) ##############################

    def test_can_act_true(self):
        self.assertTrue(sr.can_act(self.squad1))

    def test_can_act_false(self):
        self.squad1['actions'] = 0
        self.assertFalse(sr.can_act(self.squad1))

    ######################## can_draw_card(squad) #########################

    def test_can_draw_card_true(self):
        self.assertTrue(sr.can_draw_card(self.squad1))

    def test_can_draw_card_false(self):
        self.squad1['can_draw'] = False
        self.assertFalse(sr.can_draw_card(self.squad1))

    def test_can_draw_card_false_no_actions(self):
        self.squad1['actions'] = 0
        self.assertFalse(sr.can_draw_card(self.squad1))

    ######################## can_play_card(squad) ########################

    def test_can_play_card_true(self):
        self.squad1['hand'].append({'test_card': None})
        self.assertTrue(sr.can_play_card(self.squad1))

    def test_can_play_card_false_no_actions(self):
        self.squad1['actions'] = 0
        self.assertFalse(sr.can_play_card(self.squad1))

    def test_can_play_card_false_no_cards(self):
        self.assertFalse(sr.can_play_card(self.squad1))

    ######################## can_heal_main(squad) ########################

    def test_can_heal_main_true(self):
        self.minor_1l['hp'] = 0
        self.minor_2l['hp'] = 0
        self.squad1['characters'] = [self.main_l, self.minor_1l, self.minor_2l]
        self.squad1['hand'].append(self.minor_combat)
        self.assertTrue(sr.can_heal_main(self.squad1))

    def test_can_heal_main_false_minors_alive(self):
        self.squad1['hand'].append(self.minor_combat)
        self.assertFalse(sr.can_heal_main(self.squad1))

    def test_can_heal_main_false_no_minor_cards(self):
        self.assertFalse(sr.can_heal_main(self.squad1))

    ######################## can_heal_minor(squad) ########################

    def test_can_heal_minor_true(self):
        self.main_l['hp'] = 0
        self.squad1['characters'] = [self.main_l, self.minor_1l, self.minor_2l]
        self.squad1['hand'].append(self.main_combat)
        self.assertTrue(sr.can_heal_minor(self.squad1))

    def test_can_heal_minor_false_main_alive(self):
        self.squad1['actions'] = 0
        self.squad1['hand'].append(self.main_combat)
        self.assertFalse(sr.can_heal_minor(self.squad1))

    def test_can_heal_minor_false_no_main_cards(self):
        self.main_l['hp'] = 0
        self.squad1['characters'] = [self.main_l, self.minor_1l, self.minor_2l]
        self.assertFalse(sr.can_heal_minor(self.squad1))

    ######################## is_main_dead(squad) #########################

    def test_is_main_dead_false(self):
        self.assertFalse(sr.is_main_dead(self.squad1))

    def test_is_main_dead_true(self):
        self.main_l['hp'] = 0
        self.squad1['characters'] = [self.main_l, self.minor_1l, self.minor_2l]
        self.assertTrue(sr.is_main_dead(self.squad1))

    ######################## are_minors_dead(squad) #########################

    def test_are_minors_dead_false_both_alive(self):
        self.assertFalse(sr.are_minors_dead(self.squad1))

    def test_are_minors_dead_test_false_one_dead(self):
        self.minor_1l['hp'] = 4
        self.minor_2l['hp'] = 0
        self.squad1['characters'] = [self.main_l, self.minor_1l, self.minor_2l]
        self.assertFalse(sr.are_minors_dead(self.squad1))

    def test_are_minors_dead_test_true_both_dead(self):
        self.minor_1l['hp'] = 0
        self.minor_2l['hp'] = 0
        self.squad1['characters'] = [self.main_l, self.minor_1l, self.minor_2l]
        self.assertTrue(sr.are_minors_dead(self.squad1))

    ###################### has_hand(squad) #################################

    def test_has_hand_true(self):
        self.squad1['hand'].append(self.main_combat)
        self.assertTrue(sr.has_hand(self.squad1))

    def test_has_hand_false(self):
        self.assertFalse(sr.has_hand(self.squad1))

    ###################### has_main_card(squad) ############################

    def test_has_main_card_true(self):
        self.squad1['hand'].append(self.main_combat)
        self.assertTrue(sr.has_main_card(self.squad1))

    def test_has_main_card_false_minor_card_only(self):
        self.squad1['hand'].append(self.minor_combat)
        self.assertFalse(sr.has_main_card(self.squad1))

    def test_has_main_card_false_no_hand(self):
        self.assertFalse(sr.has_main_card(self.squad1))

    ###################### has_minor_card(squad) ###########################

    def test_has_minor_card_true(self):
        self.squad1['hand'].append(self.minor_combat)
        self.assertTrue(sr.has_minor_card(self.squad1))

    def test_has_minor_card_false_main_card_only(self):
        self.squad1['hand'].append(self.main_combat)
        self.assertFalse(sr.has_minor_card(self.squad1))

    def test_has_minor_card_false_no_hand(self):
        self.assertFalse(sr.has_minor_card(self.squad1))

    ####### character_has_card(squad, character, card_types=None) ##########

    def test_character_has_card_true_main(self):
        self.squad1['hand'].append(self.main_combat)
        self.assertTrue(sr.character_has_card(self.squad1, self.main_l))

    def test_character_has_card_false_no_main(self):
        self.squad1['hand'].append(self.minor_combat)
        self.assertFalse(sr.character_has_card(self.squad1, self.main_l))

    def test_character_has_card_true_minor(self):
        self.squad1['hand'].append(self.minor_combat)
        self.assertTrue(sr.character_has_card(self.squad1, self.minor_1l))

    def test_character_has_card_false_no_minor(self):
        self.squad1['hand'].append(self.main_combat)
        self.assertFalse(sr.character_has_card(self.squad1, self.minor_1l))

    def test_character_has_card_false_no_hand(self):
        self.assertFalse(sr.character_has_card(self.squad1, self.main_l))

    def test_character_has_card_true_main_combat(self):
        self.squad1['hand'].append(self.main_combat)
        self.assertTrue(sr.character_has_card(self.squad1, self.main_l,
                                              [Card.combat]))

    def test_character_has_card_false_main_combat(self):
        self.squad1['hand'].append(self.minor_combat)
        self.assertFalse(sr.character_has_card(self.squad1, self.main_l,
                                               [Card.combat]))

    ################## has_attack_card(squad, character) ###################

    def test_has_attack_card_true_main(self):
        self.squad1['hand'].append(self.main_combat)
        self.squad1['hand'].append(self.minor_combat)
        self.squad1['hand'].append(self.main_pa)
        self.assertTrue(sr.has_attack_card(self.squad1, self.main_l))

    def test_has_attack_card_false_no_main_cards(self):
        self.squad1['hand'].append(self.minor_combat)
        self.assertFalse(sr.has_attack_card(self.squad1, self.main_l))

    def test_has_attack_card_false_no_attack(self):
        self.squad1['hand'].append(self.minor_combat)
        self.squad1['hand'].append(self.main_pd)
        self.assertFalse(sr.has_attack_card(self.squad1, self.main_l))

    ################## has_defense_card(squad, character) ##################

    def test_has_defense_card_true_main(self):
        self.squad1['hand'].append(self.main_combat)
        self.squad1['hand'].append(self.minor_combat)
        self.squad1['hand'].append(self.main_pd)
        self.assertTrue(sr.has_defense_card(self.squad1, self.main_l))

    def test_has_defense_card_false_no_defense(self):
        self.squad1['hand'].append(self.minor_combat)
        self.squad1['hand'].append(self.main_pa)
        self.assertFalse(sr.has_defense_card(self.squad1, self.main_l))

    ################## has_special_card(squad, character) ##################

    def test_has_special_card_true_main(self):
        self.squad1['hand'].append(self.main_combat)
        self.squad1['hand'].append(self.minor_combat)
        self.squad1['hand'].append(self.main_pd)
        self.squad1['hand'].append(self.main_special)
        self.assertTrue(sr.has_special_card(self.squad1, self.main_l))

    def test_has_defense_card_false_no_special(self):
        self.squad1['hand'].append(self.minor_combat)
        self.squad1['hand'].append(self.main_pa)
        self.assertFalse(sr.has_special_card(self.squad1, self.main_l))

if __name__ == '__main__':
    unittest.main()
