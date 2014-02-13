
import unittest


def suite():
    test_suites = unittest.TestSuite()
    test_suites.addTest(WhenTestingCardRules())
    return test_suites


class WhenTestingCardRules(unittest.TestCase):

    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()
