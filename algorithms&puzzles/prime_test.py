import unittest
import prime

class PrimeTestCase(unittest.TestCase):
	"""Tests for 'prime_num.py'."""

	def test_prime_true(self):
		"""Passing tests for prime numbers"""
		self.assertEqual(prime.is_prime(2), True)
		self.assertEqual(prime.is_prime(3), True)
		self.assertEqual(prime.is_prime(5), True)
		self.assertEqual(prime.is_prime(7), True)
		self.assertEqual(prime.is_prime(11), True)
		self.assertEqual(prime.is_prime(103357), True)


	def test_prime_false(self):
		"""Passing tests for non-prime numbers"""
		self.assertEqual(prime.is_prime(1), False)
		self.assertEqual(prime.is_prime(4), False)
		self.assertEqual(prime.is_prime(6), False)
		self.assertEqual(prime.is_prime(9), False)
		self.assertEqual(prime.is_prime(15), False)
		self.assertEqual(prime.is_prime(22), False)
		self.assertEqual(prime.is_prime(103358), False)

	def test_prime_incorrect_type(self):
		"""If anything other than integer is given, TypeError should be raised"""
		with self.assertRaises(TypeError):
			prime.is_prime('Puschki')
		with self.assertRaises(TypeError):
			prime.is_prime(1.1)
		with self.assertRaises(TypeError):
			prime.is_prime(['Puschki'])

	def test_prime_incorrect_value(self):
		"""If anything other than a positive integer is given, ValueError should
		be raised"""
		with self.assertRaises(ValueError):
			prime.is_prime(-4)
		with self.assertRaises(ValueError):
			prime.is_prime(0)


if __name__ == '__main__':
	unittest.main()