
import unittest


def suite():
    test_suites = unittest.TestSuite()
    test_suites.addTest(WhenTestingActionRules())
    return test_suites


class WhenTestingActionRules(unittest.TestCase):

    def setUp(self):
        pass

if __name__ == '__main__':
    unittest.main()
