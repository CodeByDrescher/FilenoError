import unittest
from TestingCapturer.main import create_bug

class CliTestCase(unittest.TestCase):
    def test_capturer(self):
        create_bug()
