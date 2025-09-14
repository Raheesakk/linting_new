"""Unit tests for the greeting module."""

import unittest
from greet import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        """Test that greet() returns the correct formatted string."""
        self.assertEqual(greet("World"), "Hello, World!")

if __name__ == '__main__':
    unittest.main()

