import unittest

def divide(num_1, num_2):
    return float(num_1)/num_2


class DivideTest(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_negative_numbers(self):
        self.assertEqual(divide(-10, -2), 5)

    def test_positive_by_negative(self):
        self.assertEqual(divide(10, -2), -5)

    def test_negative_by_positive(self):
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_zero(self):
        self.assertEqual(divide(0, 10), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()