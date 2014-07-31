import unittest
import xmlrunner


class FizzBuzzTest(unittest.TestCase):
    def test_number_3_should_return_3(self):
        fizzbuzz = FizzBuzz()
        result = fizzbuzz.take(3)
        self.assertEqual(result, 'fizz')


class FizzBuzz:
    def take(self, number):
        return 'fizz'


if __name__ == "__main__":
    #unittest.main()
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
