__author__ = 'aelkikhia'

import unittest


def suite():
    test_suites = unittest.TestSuite()
    test_suites.addTest(WhenTestingGameActionsTests())
    return test_suites


class WhenTestingGameActionsTests(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
