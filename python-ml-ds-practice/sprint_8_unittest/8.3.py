import unittest
import math

def quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError("'a' cannot be zero")

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return None

    if discriminant == 0:
        x = -b / (2 * a)
        return x

    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    return x1, x2


class QuadraticEquationTest(unittest.TestCase):

    def test_discriminant_greater_than_zero(self):
        result = quadratic_equation(1, -3, 2)
        self.assertEqual(result, (2, 1))

    def test_discriminant_equal_to_zero(self):
        result = quadratic_equation(1, -2, 1)
        self.assertEqual(result, 1)

    def test_discriminant_less_to_zero(self):
        result = quadratic_equation(1, 0, 1)
        self.assertEqual(result, None)

    def test_discriminant_all_zero(self):
        with self.assertRaises(ValueError):
            quadratic_equation(0, 0, 0)

if __name__ == "__main__":
    unittest.main()
