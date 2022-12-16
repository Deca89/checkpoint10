import unittest

class TestSumma(unittest.TestCase):
    #test sum_numbers
    def test_sum_numbers_returns_sum_of_integers(self):
        result = 5
        self.assertEqual(result, 5)