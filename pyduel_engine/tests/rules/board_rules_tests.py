__author__ = 'aelkikhia'

import unittest

from pyduel_engine.content.engine_states import Character as Cs
from pyduel_engine.content.engine_states import Square as State
from pyduel_engine.content.engine_states import Boards as Bs
from pyduel_engine.rules import board_rules as br


def suite():
    test_suites = unittest.TestSuite()
    test_suites.addTest(WhenTestingBoardRules())
    return test_suites


class WhenTestingBoardRules(unittest.TestCase):

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

    ######################### is_diagonal ####################################
    def test_if_square_is_diagonal_true(self):
        self.assertTrue(br.is_diagonal(self.char1['pos'], self.char2['pos']))

    def test_if_square_is_diagonal_false(self):
        self.char2['pos'] = {'x': 5, 'y': 6}
        self.assertFalse(br.is_diagonal(self.char1['pos'], self.char2['pos']))

    ######################### is_parallel ####################################
    def test_if_squares_are_parallel_false(self):
        self.assertFalse(br.is_parallel(self.char1['pos'], self.char2['pos']))

    def test_if_squares_are_parallel_true(self):
        self.char2['pos'] = {'x': 0, 'y': 6}
        self.assertTrue(br.is_parallel(self.char1['pos'], self.char2['pos']))

    ######################### is_adjacent ####################################
    def test_if_squares_are_adjacent_false(self):
        self.assertFalse(br.is_adjacent(self.char1['pos'], self.char2['pos']))

    def test_if_squares_are_adjacent_true(self):
        self.char2['pos'] = {'x': 0, 'y': 1}
        self.assertTrue(br.is_adjacent(self.char1['pos'], self.char2['pos']))

    ######################### is_parallel_clear ##############################
    def test_if_parallel_squares_are_clear_false_not_parallel(self):
        self.assertFalse(br.is_parallel_clear(
            self.board['board'], self.char1['pos'], self.char2['pos']))

    def test_parallel_squares_are_clear_on_x_axis_orig_less_target_true(self):
        self.assertTrue(br.is_parallel_clear(self.board['board'],
                                             {'x': 2, 'y': 2},
                                             {'x': 2, 'y': 5}))

    def test_parallel_squares_are_clear_on_x_axis_orig_more_target_true(self):
        self.assertTrue(br.is_parallel_clear(self.board['board'],
                                             {'x': 2, 'y': 5},
                                             {'x': 2, 'y': 2}))

    def test_parallel_squares_are_clear_on_x_axis_target_less_orig_true(self):
        self.assertTrue(br.is_parallel_clear(self.board['board'],
                                             {'x': 2, 'y': 2},
                                             {'x': 2, 'y': 5}))

    def test_parallel_squares_are_clear_on_x_axis_target_more_orig_true(self):
        self.assertTrue(br.is_parallel_clear(self.board['board'],
                                             {'x': 2, 'y': 2},
                                             {'x': 5, 'y': 2}))

    def test_parallel_squares_are_clear_on_x_axis_adjacent_true(self):
        self.assertTrue(br.is_parallel_clear(self.board['board'],
                                             {'x': 2, 'y': 2},
                                             {'x': 2, 'y': 3}))

    def test_parallel_squares_are_clear_on_y_plane_adjacent_false(self):
        self.board['board'][3][0] = State.obstacle
        self.assertFalse(br.is_parallel_clear(self.board['board'],
                                              {'x': 0, 'y': 0},
                                              {'x': 6, 'y': 0}))

    ######################### is_diagonal_clear ##############################
    def test_board_is_diagonal_clear_true(self):
        self.assertTrue(br.is_diagonal_clear(self.board['board'],
                                             {'x': 1, 'y': 3},
                                             {'x': 4, 'y': 0}))

    def test_board_is_diagonal_clear_true_inverse(self):
        self.assertTrue(br.is_diagonal_clear(self.board['board'],
                                             {'x': 1, 'y': 3},
                                             {'x': 4, 'y': 0}))

    def test_board_is_diagonal_clear_false(self):
        self.board['board'][2][2] = State.dark
        self.assertFalse(br.is_diagonal_clear(self.board['board'],
                                              {'x': 1, 'y': 3},
                                              {'x': 4, 'y': 0}))

    ######################### is_legal_target ##############################
    def test_board_is_legal_target_melee_not_adjacent_false(self):
        self.assertFalse(br.is_legal_target(self.char1, self.char2))

    def test_board_is_legal_target_same_alignment_false(self):
        self.assertFalse(br.is_legal_target(self.char1, self.char1))

    def test_board_is_legal_target_true(self):
        self.char1['pos'] = {'x': 2, 'y': 2}
        self.char2['pos'] = {'x': 2, 'y': 3}
        self.assertTrue(br.is_legal_target(self.char1, self.char2))

    ######################### can_melee_attack ##############################
    def test_can_melee_attack_true(self):
        self.char1['pos'] = {'x': 2, 'y': 2}
        self.char2['pos'] = {'x': 2, 'y': 3}
        self.assertTrue(br.can_melee_attack(self.char1, self.char2))

    def test_can_melee_attack_false(self):
        self.assertFalse(br.can_melee_attack(self.char1, self.char2))

    ######################### can_range_attack ##############################
    def test_can_range_attack_false(self):
        self.assertFalse(br.can_range_attack(self.board['board'], self.char1,
                                             self.char2))

    def test_can_range_attack_true(self):
        self.char1['is_range'] = True
        self.assertTrue(br.can_range_attack(self.board['board'], self.char1,
                                            self.char2))

    ######################### is_obstructed ##############################
    def test_is_obstructed_surrounded_true(self):
        self.board['board'][3][5] = State.light
        self.board['board'][3][6] = State.dark
        self.board['board'][4][5] = State.dark
        self.board['board'][2][5] = State.dark
        self.board['board'][3][4] = State.dark
        self.assertTrue(br.is_obstructed(self.board, {'x': 3, 'y': 5}))

    def test_is_obstructed_obstacles_true(self):
        self.board['board'][3][5] = State.light
        self.board['board'][3][6] = State.obstacle
        self.board['board'][4][5] = State.obstacle
        self.board['board'][2][5] = State.obstacle
        self.board['board'][3][4] = State.obstacle
        self.assertTrue(br.is_obstructed(self.board, {'x': 3, 'y': 5}))

    def test_is_obstructed_false_one_friendly(self):
        self.board['board'][3][5] = State.light
        self.board['board'][3][6] = State.light
        self.board['board'][4][5] = State.dark
        self.board['board'][2][5] = State.dark
        self.board['board'][3][4] = State.dark
        self.assertFalse(br.is_obstructed(self.board, self.char1['pos']))

    def test_is_obstructed_false_one_empty(self):
        self.board['board'][3][5] = State.light
        self.board['board'][3][6] = State.dark
        self.board['board'][4][5] = State.dark
        self.board['board'][2][5] = State.dark
        self.board['board'][3][4] = State.empty
        self.assertFalse(br.is_obstructed(self.board, self.char1['pos']))

    ######################### find_moves ##############################
    # TODO: Fix these tests to compare proper list of coordinates
    def test_find_moves_roll_1_true(self):
        self.board['board'][4][2] = State.dark
        self.assertEqual(len(br.find_moves(
            self.board, 1, {'x': 4, 'y': 2})), 5)

    def test_find_moves_roll_2_true(self):
        self.board['board'][4][2] = State.dark
        self.assertEqual(len(br.find_moves(
            self.board, 2, {'x': 4, 'y': 2})), 13)

    def test_find_moves_roll_3_true(self):
        self.board['board'][4][2] = State.dark
        self.assertEqual(len(br.find_moves(
            self.board, 3, {'x': 4, 'y': 2})), 25)

    # TODO: fix out of bounds issues if number of moves is too high
    # def test_find_moves_roll_4_true(self):
    #     self.board['board'][4][2] = State.dark
    #     self.assertEqual(len(br.find_moves(
    #         self.board, 4, {'x': 4, 'y': 2})), 13)

    # def test_find_moves_roll_5_true(self):
    #     self.board['board'][4][2] = State.dark
    #     self.assertEqual(len(br.find_moves(
    #         self.board, 5, {'x': 4, 'y': 2})), 25)

    # def test_find_moves_true(self):
    #     self.maxDiff = None
    #     self.board['board'][4][2] = State.dark
    #     self.assertListEqual(br.find_moves(self.board, 2, {'x': 4, 'y': 2}),
    #                          [{'x': 3, 'y': 2},
    #                           {'x': 3, 'y': 3},
    #                           {'x': 2, 'y': 2},
    #                           {'x': 5, 'y': 2},
    #                           {'x': 4, 'y': 3},
    #                           {'x': 3, 'y': 1},
    #                           {'x': 4, 'y': 1},
    #                           {'x': 4, 'y': 4},
    #                           {'x': 4, 'y': 0},
    #                           {'x': 5, 'y': 1},
    #                           {'x': 5, 'y': 3},
    #                           {'x': 6, 'y': 2},
    #                           {'x': 4, 'y': 2},
    #                           {'x': 3, 'y': 1},
    #                           {'x': 4, 'y': 1}])

    # def test_find_moves_true_ish(self):
    #     self.maxDiff = None
    #     self.board['board'][4][2] = State.dark
    #     self.assertListEqual(br.find_moves(self.board, 3, {'x': 4, 'y': 2}),
    #                          [{'x': 3, 'y': 4},
    #                           {'x': 3, 'y': 1},
    #                           {'x': 2, 'y': 1},
    #                           {'x': 5, 'y': 3},
    #                           {'x': 6, 'y': 2},
    #                           {'x': 5, 'y': 0},
    #                           {'x': 6, 'y': 3},
    #                           {'x': 3, 'y': 2},
    #                           {'x': 4, 'y': 5},
    #                           {'x': 5, 'y': 4},
    #                           {'x': 4, 'y': 2},
    #                           {'x': 1, 'y': 2},
    #                           {'x': 4, 'y': 1},
    #                           {'x': 3, 'y': 3},
    #                           {'x': 5, 'y': 2},
    #                           {'x': 4, 'y': 4},
    #                           {'x': 4, 'y': -1},
    #                           {'x': 2, 'y': 2},
    #                           {'x': 3, 'y': 0},
    #                           {'x': 4, 'y': 0},
    #                           {'x': 4, 'y': 3},
    #                           {'x': 2, 'y': 3}])

if __name__ == '__main__':
    unittest.main()