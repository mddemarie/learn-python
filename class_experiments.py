# get something from dictionary
mystuff = {'apple' : "I am an apple!"}
print(mystuff['apple'])


# get apples from function
def apple():
	print("I am an apple!")
	#return
apple()

# But I can access this function like this:
# class_experiments.apple()

# get tangerine from a file
tangerine = "Living reflection of a dream"

# But I can access this variable like this:
# class_experiments.tangerine

# In conclusion:
mystuff['apple'] # get apple from dict
# class_experiment.apple() gets apple from the module
# class_experiment.tangerine gets variable from the module


# the same as a Class:
class MyStuff(object):

	def __init__(self):
		self.tangerine = "Living reflection of a dream 2."

	def appl(self):
		print("I am an apple! @")

thing = MyStuff()
thing.appl()
print(thing.tangerine)

# simple Classes and inheritance:

class A():
	a = 1

b = A()
b.a

class B(A):
	b = 2

c = B()
c.b
c.a

