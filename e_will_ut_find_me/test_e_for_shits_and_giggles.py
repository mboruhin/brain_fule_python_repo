import unittest
from e_for_shits_and_giggles import ShitsAndGiggles


class First(unittest.TestCase):
    def test_shits(self):
        s1 = ShitsAndGiggles(2, 3)
        print("First.test_shits")
        self.assertEqual(s1.num_of_shits, 2)

    def test_giggles(self):
        s1 = ShitsAndGiggles(2, 3)
        print("First.test_giggles")
        self.assertEqual(s1.num_of_giggles, 3)
