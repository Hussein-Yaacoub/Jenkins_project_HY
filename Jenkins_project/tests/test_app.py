# tests/test_app.py
import unittest
from Jenkins_project.app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Hussein Yaacoub"), "Hello, Hussein Yaacoub!")


if __name__ == "__main__":
    unittest.main()
