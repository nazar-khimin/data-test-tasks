import unittest
import math


class TriangleNotValidArgumentException(Exception):
    pass


class TriangleNotExistException(Exception):
    pass


class Triangle:
    def __init__(self, sides):
        is_valid_type = isinstance(sides, (list, tuple))
        if not is_valid_type:
            raise TriangleNotValidArgumentException("Not valid arguments")

        has_three_slides = len(sides) != 3
        if has_three_slides:
            raise TriangleNotValidArgumentException("Not valid arguments")

        are_all_numeric = all(isinstance(side, (int, float)) for side in sides)
        if not are_all_numeric:
            raise TriangleNotValidArgumentException("Not valid arguments")

        self.a, self.b, self.c = sorted(sides)

        if self.a <= 0 or self.a + self.b <= self.c:
            raise TriangleNotExistException("Can`t create triangle with this arguments")

    def get_area(self):
        s = (self.a + self.b + self.c) / 2  # Semi-perimeter
        a, b, c = self.a, self.b, self.c
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return round(area, 2)


class TriangleTest(unittest.TestCase):
    def test_valid_triangles(self):
        valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]
        for sides, expected_area in valid_test_data:
            with self.subTest(sides=sides):
                triangle = Triangle(sides)
                self.assertAlmostEqual(triangle.get_area(), expected_area, places=2)

    def test_invalid_triangles(self):
        not_valid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]
        for sides in not_valid_triangle:
            with self.subTest(sides=sides):
                with self.assertRaises(TriangleNotExistException):
                    Triangle(sides)

    def test_invalid_arguments(self):
        not_valid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            10
        ]
        for sides in not_valid_arguments:
            with self.subTest(sides=sides):
                with self.assertRaises(TriangleNotValidArgumentException):
                    Triangle(sides)


if __name__ == "__main__":
    unittest.main()
