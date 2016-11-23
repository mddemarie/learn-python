import datetime

def age_in_days(date_of_birth):
	if type(date_of_birth) is str or type(date_of_birth) is int:
		raise TypeError("You did not pass a date.")
	if date_of_birth > datetime.date(2001, 1, 1):
		raise ValueError("The date cannot be in the future.")

	millenium_date = datetime.date(2001, 1, 1)
	difference = millenium_date - date_of_birth
	difference = difference.days
	return difference
