
import unittest
from epicduels.content import game_state as GS
from epicduels.initializers import initializer as init
from epicduels.rules import board_rules as BR


def suite():
    test_suites = unittest.TestSuite()
    test_suites.addTest(WhenTestingBoardRules())
    return test_suites


class WhenTestingBoardRules(unittest.TestCase):

    def setUp(self):
        self.char1 = init.character_initializer(GS.MACE_WINDU,
                                                {'x': 0, 'y': 0},
                                                GS.LIGHT)
        self.char2 = init.character_initializer(GS.COUNT_DOOKU,
                                                {'x': 6, 'y': 6},
                                                GS.DARK)
        self.board = init.board_initializer(GS.GEONOSIS)

    def test_if_square_is_diagonal_true(self):
        self.assertTrue(BR.is_diagonal(self.char1['pos'], self.char2['pos']))

    def test_if_square_is_diagonal_false(self):
        self.char2['pos'] = {'x': 5, 'y': 6}
        self.assertFalse(BR.is_diagonal(self.char1['pos'], self.char2['pos']))

    def test_if_squares_are_parallel_false(self):
        self.assertFalse(BR.is_parallel(self.char1['pos'], self.char2['pos']))

    def test_if_squares_are_parallel_true(self):
        self.char2['pos'] = {'x': 0, 'y': 6}
        self.assertTrue(BR.is_parallel(self.char1['pos'], self.char2['pos']))

    def test_if_squares_are_adjacent_false(self):
        self.assertFalse(BR.is_adjacent(self.char1['pos'], self.char2['pos']))

    def test_if_squares_are_adjacent_true(self):
        self.char2['pos'] = {'x': 0, 'y': 1}
        self.assertTrue(BR.is_adjacent(self.char1['pos'], self.char2['pos']))

    def test_if_parallel_squares_are_clear_false_not_parallel(self):
        self.assertFalse(BR.is_parallel_clear(
            self.board['board'], self.char1['pos'], self.char2['pos']))

    def test_parallel_squares_are_clear_on_x_axis_orig_less_target_true(self):
        self.assertTrue(BR.is_parallel_clear(self.board['board'],
                                             {'x': 2, 'y': 2},
                                             {'x': 2, 'y': 5}))

    def test_parallel_squares_are_clear_on_x_axis_orig_more_target_true(self):
        self.assertTrue(BR.is_parallel_clear(self.board['board'],
                                             {'x': 2, 'y': 5},
                                             {'x': 2, 'y': 2}))

    def test_parallel_squares_are_clear_on_x_axis_target_less_orig_true(self):
        self.assertTrue(BR.is_parallel_clear(self.board['board'],
                                             {'x': 2, 'y': 2},
                                             {'x': 2, 'y': 5}))

    def test_parallel_squares_are_clear_on_x_axis_target_more_orig_true(self):
        self.assertTrue(BR.is_parallel_clear(self.board['board'],
                                             {'x': 2, 'y': 2},
                                             {'x': 5, 'y': 2}))

    def test_parallel_squares_are_clear_on_x_axis_adjacent_true(self):
        self.assertTrue(BR.is_parallel_clear(self.board['board'],
                                             {'x': 2, 'y': 2},
                                             {'x': 2, 'y': 3}))

    def test_parallel_squares_are_clear_on_y_plane_adjacent_false(self):
        self.board['board'][3][0] = GS.OBSTACLE
        self.assertFalse(BR.is_parallel_clear(self.board['board'],
                                              {'x': 0, 'y': 0},
                                              {'x': 6, 'y': 0}))

    def test_board_is_diagonal_clear_true(self):
        self.assertTrue(BR.is_diagonal_clear(self.board['board'],
                                             {'x': 1, 'y': 3},
                                             {'x': 4, 'y': 0}))

    def test_board_is_diagonal_clear_true_inverse(self):
        self.assertTrue(BR.is_diagonal_clear(self.board['board'],
                                             {'x': 1, 'y': 3},
                                             {'x': 4, 'y': 0}))

    def test_board_is_diagonal_clear_false(self):
        self.board['board'][2][2] = GS.DARK
        self.assertFalse(BR.is_diagonal_clear(self.board['board'],
                                              {'x': 1, 'y': 3},
                                              {'x': 4, 'y': 0}))

    def test_board_is_legal_target_melee_not_adjacent_false(self):
        self.assertFalse(BR.is_legal_target(self.char1, self.char2))

    def test_board_is_legal_target_same_alignment_false(self):
        self.assertFalse(BR.is_legal_target(self.char1, self.char1))

    def test_board_is_legal_target_true(self):
        self.char1['pos'] = {'x': 2, 'y': 2}
        self.char2['pos'] = {'x': 2, 'y': 3}
        self.assertTrue(BR.is_legal_target(self.char1, self.char2))

    def test_can_melee_attack_true(self):
        self.char1['pos'] = {'x': 2, 'y': 2}
        self.char2['pos'] = {'x': 2, 'y': 3}
        self.assertTrue(BR.can_melee_attack(self.char1, self.char2))

    def test_can_melee_attack_false(self):
        self.assertFalse(BR.can_melee_attack(self.char1, self.char2))

    def test_can_range_attack_false(self):
        self.assertFalse(BR.can_range_attack(self.board['board'], self.char1,
                                             self.char2))

    def test_can_range_attack_true(self):
        self.char1['is_range'] = True
        self.assertTrue(BR.can_range_attack(self.board['board'], self.char1,
                                            self.char2))

    def test_is_obstructed_surrounded_true(self):
        self.board['board'][3][5] = GS.LIGHT
        self.board['board'][3][6] = GS.DARK
        self.board['board'][4][5] = GS.DARK
        self.board['board'][2][5] = GS.DARK
        self.board['board'][3][4] = GS.DARK
        self.assertTrue(BR.is_obstructed(self.board, {'x': 3, 'y': 5}))

    def test_is_obstructed_obstacles_true(self):
        self.board['board'][3][5] = GS.LIGHT
        self.board['board'][3][6] = GS.OBSTACLE
        self.board['board'][4][5] = GS.OBSTACLE
        self.board['board'][2][5] = GS.OBSTACLE
        self.board['board'][3][4] = GS.OBSTACLE
        self.assertTrue(BR.is_obstructed(self.board, {'x': 3, 'y': 5}))

    def test_is_obstructed_false_one_friendly(self):
        self.board['board'][3][5] = GS.LIGHT
        self.board['board'][3][6] = GS.LIGHT
        self.board['board'][4][5] = GS.DARK
        self.board['board'][2][5] = GS.DARK
        self.board['board'][3][4] = GS.DARK
        self.assertFalse(BR.is_obstructed(self.board, self.char1['pos']))

    def test_is_obstructed_false_one_empty(self):
        self.board['board'][3][5] = GS.LIGHT
        self.board['board'][3][6] = GS.DARK
        self.board['board'][4][5] = GS.DARK
        self.board['board'][2][5] = GS.DARK
        self.board['board'][3][4] = GS.EMPTY
        self.assertFalse(BR.is_obstructed(self.board, self.char1['pos']))

    def test_find_moves_true(self):
        self.maxDiff = None
        self.board['board'][4][2] = GS.DARK
        self.assertListEqual(BR.find_moves(self.board, 2, {'x': 4, 'y': 2}),
                             [{'x': 3, 'y': 2},
                              {'x': 4, 'y': 1},
                              {'x': 3, 'y': 1},
                              {'x': 3, 'y': 3},
                              {'x': 4, 'y': 0},
                              {'x': 5, 'y': 2},
                              {'x': 4, 'y': 4},
                              {'x': 4, 'y': 3},
                              {'x': 5, 'y': 3},
                              {'x': 4, 'y': 2},
                              {'x': 6, 'y': 2},
                              {'x': 2, 'y': 2}])

    def test_find_moves_true_ish(self):

        self.maxDiff = None
        self.board['board'][4][2] = GS.DARK
        self.assertListEqual(BR.find_moves(self.board, 3, {'x': 4, 'y': 2}),
                             [{'x': 3, 'y': 4},
                              {'x': 3, 'y': 1},
                              {'x': 2, 'y': 1},
                              {'x': 5, 'y': 3},
                              {'x': 6, 'y': 2},
                              {'x': 5, 'y': 0},
                              {'x': 6, 'y': 3},
                              {'x': 3, 'y': 2},
                              {'x': 4, 'y': 5},
                              {'x': 5, 'y': 4},
                              {'x': 4, 'y': 2},
                              {'x': 1, 'y': 2},
                              {'x': 4, 'y': 1},
                              {'x': 3, 'y': 3},
                              {'x': 5, 'y': 2},
                              {'x': 4, 'y': 4},
                              {'x': 4, 'y': -1},
                              {'x': 2, 'y': 2},
                              {'x': 3, 'y': 0},
                              {'x': 4, 'y': 0},
                              {'x': 4, 'y': 3},
                              {'x': 2, 'y': 3}])


if __name__ == '__main__':
    unittest.main()