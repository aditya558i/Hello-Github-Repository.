import unittest
from app import hello_git


class TestHellogit(unittest.TestCase):

    def test_hello_git(self):
        self.assertEqual(hello_git(), "Hello, Git!")


if __name__ == "__main__":
    unittest.main()
