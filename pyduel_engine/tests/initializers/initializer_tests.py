
import unittest
from pyduel_engine.initializers import initializer as init


def suite():
    test_suites = unittest.TestSuite()
    test_suites.addTest(WhenTestingInitializer())
    return test_suites


class WhenTestingInitializer(unittest.TestCase):
    pass
    # def setUp(self):
    #     self.player_number = 1
    #     self.character_type = 0
    #     self.position = {'y': 2, 'x': 6}
    #     self.side = 'light'
    #     self.board = {'board_type': 2, 'max_x': 10, 'max_y': 7,
    #                   'board': [[0, 0, 0, 0, 0, 0, 0],
    #                             [0, 0, 0, 0, 3, 0, 0],
    #                             [0, 0, 0, 0, 3, 3, 0],
    #                             [0, 0, 0, 3, 3, 3, 0],
    #                             [0, 0, 0, 0, 0, 0, 0],
    #                             [0, 0, 0, 0, 0, 0, 0],
    #                             [4, 4, 0, 0, 0, 4, 4],
    #                             [4, 4, 0, 0, 0, 4, 4],
    #                             [4, 4, 0, 0, 0, 4, 4],
    #                             [4, 0, 0, 0, 0, 0, 4]]}
    #
    #     self.board_type = 'kamino'
    #     self.squad = CS.SQUADS[GS.BOBA_FETT]
    #
    # def test_character_initializer(self):
    #     character = init.character_initializer(self.character_type,
    #                                            self.position,
    #                                            self.side)
    #     self.assertEqual(character['side'], self.side)
    #
    # def test_squad_initializer(self):
    #     squad = init.setup_squad(1, self.character_type, self.side)
    #     self.assertEqual(squad['side'], self.side)
    #
    # def test_board_initializer(self):
    #     self.assertDictEqual(init.board_initializer(self.board_type),
    #                          self.board)

if __name__ == '__main__':
    unittest.main()
