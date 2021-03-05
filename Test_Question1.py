import unittest
import Question1


class FizzBuzz_Testing(unittest.TestCase):

    def test_Fizz(self):
        result = Question1.Fizz(3)
        self.assertEqual(result, 'Fizz')
        result = Question1.Fizz(2)
        self.assertNotEqual(result,'Fizz')










if __name__ == "__main__":
    unittest.main()