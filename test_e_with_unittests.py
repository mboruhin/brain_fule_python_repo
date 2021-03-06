from unittest import TestCase
from point import Point

class Case1(TestCase):
    def test_repr(self):
        point1 = Point(3, 4)
        point_str = str(point1)
        print("Case1.test_repr")
        self.assertEqual("x: 3, y: 4", point_str)

    def test_dist(self):
        point1 = Point(3, 4)
        print("Case1.test_dist")
        self.assertEqual(point1.dist_from_origin(), 5)
