import unittest

import collatzSequence


class TestCollatzSequence(unittest.TestCase):
    def setUp(self):
        self.collatz = collatzSequence.CollatzSequence(5)
        pass

    def tearDown(self):
        pass

    def testCollatz(self):
        ''' Test the collatz sequencer is accurate'''
        expected_test_data = {
            1: 1,
            2: 1,
            3: 10,
            4: 2,
            5: 16,
            6: 3,
            7: 22,
            8: 4,
            9: 28,
            10: 5
        }

        for input, exp_result in expected_test_data.items():
            result = self.collatz.collatz(input)
            self.assertTrue(exp_result == result,
                            "Expected: %s, Actual: %s" % (exp_result, result))


if __name__ == '__main__':
    unittest.main()