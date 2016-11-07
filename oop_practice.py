class Dog(object):

	color = 'red' # class attribute

	def __init__(self, color='red', size='small'):
		self.color = color # instance attribute
		self.size = size

	def bark(self):
		print 'Woof!'



puschki = Dog(color='grey')
print puschki.color
print puschki.size

dog = Dog()
print dog.color # instance attr
print Dog.color # class attr