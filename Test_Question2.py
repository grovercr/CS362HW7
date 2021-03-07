import unittest
import Question2


class LeapYear_Testing(unittest.TestCase):
    def test_leap_year(self):
        result = Question2.leap_year(4)
        self.assertEqual(result, 'Leap Year')
        result = Question2.leap_year(3)
        self.assertEqual(result, 'Not a Leap Year')

if __name__ == "__main__":
    unittest.main()