
import unittest


def suite():
    test_suites = unittest.TestSuite()
    test_suites.addTest(WhenTestingActionRules())
    return test_suites


class WhenTestingActionRules(unittest.TestCase):

    def setUp(self):
        pass
    #     self.squad1 = init.setup_squad(1, GS.MACE_WINDU, GS.LIGHT)
    #     self.squad2 = init.setup_squad(2, GS.COUNT_DOOKU, GS.DARK)
    #     self.main_card = cards.BATTLEMIND
    #     self.main_card['owner'] = GS.MACE_WINDU
    #     self.secondary_card = cards.COMBAT_1_2
    #     self.secondary_card['owner'] = GS.TROOPER
    #
    # def test_attack(self):
    #     pass
    #
    # def test_minors_dead_false_both_alive(self):
    #     for character in self.squad1['characters']:
    #         if not character['is_main']:
    #             character['hp'] = 2
    #     self.assertFalse(AR.minors_dead(self.squad1))
    #
    # def test_minors_dead_true(self):
    #     for character in self.squad1['characters']:
    #         if not character['is_main']:
    #             character['hp'] = 0
    #     self.assertTrue(AR.minors_dead(self.squad1))
    #
    # # def test_minors_dead_false_one_dead(self):
    # #     for character in self.squad1['characters']:
    # #         if not character['is_main']:
    # #             character['hp'] = 0
    # #             if character['number'] == 1:
    # #                 character['hp'] = 2
    # #     self.assertFalse(AR.minors_dead(self.squad1))
    #
    # def test_can_act_true(self):
    #     self.assertTrue(AR.can_act(self.squad1))
    #
    # def test_can_act_false(self):
    #     self.squad1['actions'] = 0
    #     self.assertFalse(AR.can_act(self.squad1))
    #
    # def test_can_play_card_false_no_actions(self):
    #     self.squad1['actions'] = 0
    #     self.squad1['hand'].append(self.squad1['deck'].pop())
    #     self.assertFalse(AR.can_play_card(self.squad1))
    #
    # def test_can_play_card_false_no_cards(self):
    #     self.assertFalse(AR.can_play_card(self.squad1))
    #
    # def test_can_play_card_true(self):
    #     self.squad1['hand'].append(self.squad1['deck'].pop())
    #     self.assertTrue(AR.can_play_card(self.squad1))
    #
    # def test_draw_card(self):
    #     old_len = len(self.squad1['deck'])
    #     AR.draw_card(self.squad1)
    #     self.assertTrue(len(self.squad1['hand']) == 1 and
    #                     (len(self.squad1['deck']) + 1) == old_len)
    #
    # def test_choose_card(self):
    #     pass
    #
    # def test_defense(self):
    #     pass
    #
    # def test_discard_card(self):
    #     AR.draw_card(self.squad1)
    #     old_len = len(self.squad1['hand'])
    #     AR.discard_card(self.squad1, 0)
    #     self.assertTrue(((len(self.squad1['hand']) + 1) == old_len) and
    #                     (len(self.squad1['discard']) == 1))
    #
    # def test_discard_heal_false_secondary_character_alive(self):
    #     self.squad1['hand'].append(self.main_card)
    #     self.squad1['hand'].append(self.secondary_card)
    #     self.assertFalse(AR.discard_heal(self.squad1, 0))
    #
    # def test_discard_heal_false_no_hand(self):
    #     for character in self.squad1['characters']:
    #         if not character['is_main']:
    #             character['hp'] = 0
    #     self.assertFalse(AR.discard_heal(self.squad1, 0))
    #
    # def test_discard_heal_false_no_secondary_cards(self):
    #     self.squad1['hand'].append(self.main_card)
    #     self.assertFalse(AR.discard_heal(self.squad1, 0))
    #
    # def test_discard_heal_true(self):
    #     for character in self.squad1['characters']:
    #         if character['is_main']:
    #             character['hp'] = 1
    #     self.squad1['hand'].append(self.secondary_card)
    #     hand_size = len(self.squad1['hand'])
    #     AR.discard_heal(self.squad1, 0)
    #     self.assertTrue(len(self.squad1['hand']) + 1 == hand_size)
    #
    #     new_health = 0
    #     for character in self.squad1['characters']:
    #         if character['is_main']:
    #             new_health = character['hp']
    #     self.assertTrue(new_health == 2)
    #
    # def test_has_hand_false(self):
    #     self.assertFalse(AR.has_hand(self.squad1))
    #
    # def test_has_hand_true(self):
    #     self.squad1['hand'].append(self.main_card)
    #     self.assertTrue(AR.has_hand(self.squad1))
    #
    # def test_has_minor_card_false(self):
    #     self.squad1['hand'].append(self.main_card)
    #     self.assertFalse(AR.has_minor_card(self.squad1))
    #
    # def test_has_minor_card_true(self):
    #     self.squad1['hand'].append(self.secondary_card)
    #     self.assertTrue(AR.has_minor_card(self.squad1))
    #
    # def test_has_main_card_false(self):
    #     self.squad1['hand'].append(self.secondary_card)
    #     self.assertFalse(AR.has_main_card(self.squad1))
    #
    # def test_has_main_card_true(self):
    #     self.squad1['hand'].append(self.main_card)
    #     self.assertTrue(AR.has_main_card(self.squad1))

if __name__ == '__main__':
    unittest.main()