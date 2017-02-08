def add(a, b):
	print("ADDING %d + %d" % (a, b))
	return a + b

def subtract(a, b):
	print("SUBTRACTING %d - %d" % (a, b))
	return a - b

def multiply(a, b):
	print("MULTIPLYING %d * %d" % (a, b))
	return a * b

def divide(a, b):
	print("DIVIDING %d / %d" % (a, b))
	return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

inside = multiply(iq, 2)
mlt_inside = divide(weight, inside)
sbt_mlt = add(height, mlt_inside)
what = subtract(age, sbt_mlt)

print("That becomes: ", what, "Can you do it by hand?")

24 + 76 / 2 - 27

what = subtract(add(24, divide(76, 2)), 27)
print("This is new number: ", what)