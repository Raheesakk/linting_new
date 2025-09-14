"""Unit tests for the greeting module."""
import unittest
from greet import greet
class TestGreet(unittest.TestCase):
    """Greeter class provides a method to greet users."""
    def test_greet(self):
        """Test that greet() returns the correct greeting string."""
        self.assertEqual(greet("World"), "Hello, World!")
if __name__ == '__main__':
    unittest.main()
