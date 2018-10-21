import unittest
from app.data import Data

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.data = Data()

    def test_integer_data(self):
        self.assertEqual(self.data.get_integer_data(), 1234,
                         'incorrect integer data returned')

    def test_string_data(self):
        self.assertEqual(self.data.get_string_data(), "1234",
                         'incorrect string data returned')
