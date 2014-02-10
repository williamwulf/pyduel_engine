
import unittest
from epicduels.content import game_state as GS
from epicduels.content import characters as CS
from epicduels.content import boards as BS
from epicduels.initializers import initializer as init


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WhenTestingInitializer())
    return suite


class WhenTestingInitializer(unittest.TestCase):

    def setUp(self):
        self.player_number = 1
        self.character_type = GS.BOBA_FETT
        self.position = {'y': 2, 'x': 6}
        self.side = GS.LIGHT
        self.board = {'board_type': 2, 'max_x': 10, 'max_y': 7,
                      'board': [[0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 3, 0, 0],
                                [0, 0, 0, 0, 3, 3, 0],
                                [0, 0, 0, 3, 3, 3, 0],
                                [0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0],
                                [4, 4, 0, 0, 0, 4, 4],
                                [4, 4, 0, 0, 0, 4, 4],
                                [4, 4, 0, 0, 0, 4, 4],
                                [4, 0, 0, 0, 0, 0, 4]]}

        self.board_type = GS.KAMINO
        self.squad = CS.SQUADS[GS.BOBA_FETT]

    def test_character_initializer(self):
        character = init.character_initializer(self.character_type,
                                               self.position,
                                               self.side)
        self.assertEqual(character['side'], self.side)

    def test_squad_initializer(self):
        squad = init.setup_squad(1, self.character_type, self.side)
        self.assertEqual(squad['side'], self.side)

    def test_board_initializer(self):
        self.assertDictEqual(init.board_initializer(self.board_type),
                             self.board)

if __name__ == '__main__':
    unittest.main()