import unittest
import datetime
import age

class AgeTestCase(unittest.TestCase):
	"""Tests for 'age.py'."""

	def test_day_before(self):
		"""What is the age (in days) on 1.1.2001
		of the person who was born on 31.12.2000?
		1 day"""
		date_of_birth = datetime.date(2000, 12, 31)
		my_age_in_days = age.age_in_days(date_of_birth)
		self.assertEqual(my_age_in_days, 1)

	def test_my_birthday(self):
		"""What is the age (in days) on 1.1.2001
		of me who was born on 17.12.1987?
		4764 days"""
		date_of_birth = datetime.date(1987, 12, 17)
		my_age_in_days = age.age_in_days(date_of_birth)
		self.assertEqual(my_age_in_days, 4764)

	def test_specific_date(self):
		"""What is the age (in days) on 1.1.2001
		of the person who was born on 12.9.133?
		682019 days"""
		date_of_birth = datetime.date(133, 9, 12)
		my_age_in_days = age.age_in_days(date_of_birth)
		self.assertEqual(my_age_in_days, 682019)

	def test_future_date(self):
		"""If the future date is given, the function should raise
		this exception: ValueError"""
		date_of_birth = datetime.date(2356, 3, 26)
		with self.assertRaises(ValueError):
			age.age_in_days(date_of_birth)

	def test_passing_string(self):
		"""If the string is given, the function should raise
		this exception: TypeError"""
		date_of_birth = "Puschki"
		with self.assertRaises(TypeError):
			age.age_in_days(date_of_birth)

	def test_passing_number(self):
		"""If the number is given, the function should raise
		this exception: TypeError"""
		date_of_birth = 42
		with self.assertRaises(TypeError):
			age.age_in_days(date_of_birth)

if __name__ == '__main__':
	unittest.main()