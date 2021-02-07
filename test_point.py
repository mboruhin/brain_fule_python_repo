import unittest
from point import Point


class PointTest(unittest.TestCase):
    def test_point_repr(self):
        p1 = Point(3, 4)
        print("PointTest.test_point_repr!!!")
        self.assertEqual("x: 3, y: 4", str(p1))

    def test_dist_from_origin(self):
        p1 = Point(3, 4)
        print("PointTest.test_dist_from_origin!!!")
        self.assertEqual(p1.dist_from_origin(), 5)