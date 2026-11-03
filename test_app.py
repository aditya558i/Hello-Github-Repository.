import unittest
from app import hello_devops


class TestHelloDevops(unittest.TestCase):

    def test_hello_devops(self):
        self.assertEqual(hello_devops(), "Hello, Git!")


if __name__ == "__main__":
    unittest.main()
