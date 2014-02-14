__author__ = 'aelkikhia'

import unittest


def suite():
    test_suites = unittest.TestSuite()
    test_suites.addTest(WhenTestingBoardActionsTests())
    return test_suites


class WhenTestingBoardActionsTests(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
