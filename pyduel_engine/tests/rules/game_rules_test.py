
import unittest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WhenTestingActionRules())
    return suite


class WhenTestingActionRules(unittest.TestCase):

    def setUp(self):
        pass

if __name__ == '__main__':
    unittest.main()
