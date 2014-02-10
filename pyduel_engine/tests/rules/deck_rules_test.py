
import unittest
from epicduels.content import game_state as GS
from epicduels.initializers import initializer as init


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WhenTestingDeckRules())
    return suite


class WhenTestingDeckRules(unittest.TestCase):

    def setUp(self):
        self.squad = init.setup_squad(1, GS.MACE_WINDU, GS.DARK)

    # def test_if_deck_shuffled(self):
    #     # deck = self.squad['deck']
    #     # shuffled_deck = DR.shuffle_cards(self.squad['deck'])
    #     print '********************\n'
    #     print(self.squad['deck'])
    #     print '********************\n'
    #     DR.shuffle_cards(self.squad['deck'])
    #     print(self.squad['deck'])
    #     print '********************\n'
    #     # self.assertListEqual(deck, shuffled_deck)


if __name__ == '__main__':
    unittest.main()