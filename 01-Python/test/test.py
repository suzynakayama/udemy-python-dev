import unittest

import main

class TestMain(unittest.TestCase):
    def setUp(self):        # useful to run something before each test
        print('about to run a test function')

    def test_add5(self):
        test_param = 10
        result = main.add5(test_param)
        self.assertEqual(result, 15)

    def test_add5_2(self):
        test_param = 10
        result = main.add5(test_param)
        self.assertEqual(result, 10)

    def test_add5_3(self):
        test_param = 'sadfva'
        result = main.add5(test_param)
        self.assertIsInstance(result, ValueError)

    def test_add5_4(self):
        test_param = None
        result = main.add5(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_add5_5(self):
        test_param = ''
        result = main.add5(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_add5_6(self):
        test_param = 0
        result = main.add5(test_param)
        self.assertEqual(result, 5)

    def tearDown(self):         # useful to clean up after each test
        print('cleaning up')

class TestGame(unittest.TestCase):
    def test_input(self):
        result = main.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = main.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = main.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = main.run_guess(5, '11')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

    # now we can run like: `python3 -m unittest -v`