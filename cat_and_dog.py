class Animal(object):
	pass

class Cat(Animal):
	def __init__(self, name, color, noise, size, weight):
		self.name = name
		self.color = color
		self.noise = noise
		self.size = size
		self.weight = weight

	def naming(self):
		print "The cat's name is", self.name
	def coloring(self):
		print "The cat's color is", self.color
	def noising(self):
		print "Miaou"
	def sizing(self):
		print "Size: 4x4"
	def weighting(self):
		print "Weight: 2 kg"

diesel = Cat("Diesel", "grey", "miau miau", "2x2", "2 kg")

