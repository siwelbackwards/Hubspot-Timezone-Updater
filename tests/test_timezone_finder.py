import unittest
from src.timezone.finder import TimezoneFinder

class TestTimezoneFinder(unittest.TestCase):
    def setUp(self):
        self.finder = TimezoneFinder()

    def test_predict_timezone(self):
        timezone = self.finder.predict_timezone("USA", "New York")
        self.assertIsNotNone(timezone)
        self.assertTrue(len(timezone) > 0)

if __name__ == '__main__':
    unittest.main()