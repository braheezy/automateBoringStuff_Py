import unittest

import fantasyGame

class TestInventory(unittest.TestCase):

    def setUp(self):
        game = fantasyGame.FantasyGame()

    def tearDown(self):
        pass

    def testDisplayInventory(self):
        '''Test inventory display function
        '''
        test_data = {
            'rope': 1,
            'torch': 6,
            'gold coin': 42,
            'dagger': 1,
            'arrow': 12
        }
        


if __name__ == "__main__":
    unittest.main()