import unittest
import os
from app import suma

class TestApp(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)   
        self.assertEqual(suma(-1, 1), 1)

if __name__ == "__main__":
    unittest.main()
