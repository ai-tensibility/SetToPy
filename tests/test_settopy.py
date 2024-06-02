import unittest
from SetTopy import SetTopy


class TestSetTopy(unittest.TestCase):
    def test_add_contains(self):
        s = SetTopy()
        s.add(1.0, 2.0, 3.0)
        self.assertTrue(s.contains(1.0, 2.0, 3.0))
        self.assertFalse(s.contains(4.0, 5.0, 6.0))

    def test_remove(self):
        s = SetTopy()
        s.add(1.0, 2.0, 3.0)
        s.remove(1.0, 2.0, 3.0)
        self.assertFalse(s.contains(1.0, 2.0, 3.0))

    def test_size(self):
        s = SetTopy()
        self.assertEqual(s.size(), 0)
        s.add(1.0, 2.0, 3.0)
        self.assertEqual(s.size(), 1)


if __name__ == "__main__":
    unittest.main()
