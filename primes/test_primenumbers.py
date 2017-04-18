import unittest
from primenumbers import primes,isPrime

class PrimeNumberTest(unittest.TestCase):
	def test_primes_returns_correct_result(self):
		result = primes(20)
		self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19], result)

	def test_primes_function_returns_list(self):
		result = primes(20)
		self.assertIsInstance(result, list)

	def test_primes_function_returns_error_if_arg_not_integer(self):
		result = primes(20)
		self.assertRaises(TypeError, primes, 'string')

	def test_primes_function_returns_error_if_arg_negative_number(self):
		self.assertRaises(ValueError, primes, -20)

	def test_isPrime_function_returns_bool(self):
		result = isPrime(23)
		self.assertIsInstance(result, bool)

	def test_isPrime_function_returns_correct_result(self):
		result = isPrime(23)
		self.assertEqual(True, result)
				
if __name__ == '__main__':
    unittest.main()