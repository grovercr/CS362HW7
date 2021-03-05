import unittest
import Question1


class FizzBuzz_Testing(unittest.TestCase):

    def test_Fizz(self):
        result = Question1.Fizz(3)
        self.assertEqual(result, 'Fizz')
        result = Question1.Fizz(2)
        self.assertNotEqual(result,'Fizz')

    def test_Fuzz(self):
        result = Question1.Fuzz(5)
        self.assertEqual(result, 'Fuzz')
        result = Question1.Fuzz(3)
        self.assertNotEqual(result,'Fuzz')








if __name__ == "__main__":
    unittest.main()