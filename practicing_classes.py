class Cat(object):
	def __init__(self, name="Marie"):
		self.name = name
	def introduce(self):
		print "my cat ", self.name


# Why can I use this?
Cat.introduce(Cat())

# Why cannot I use this?
# A.cat(name, "Tom")

# Why cannot I use this?
# A.cat(self, "Tom")

# How come that this does not work?
#first_cat = Cat("Diesel")
#second_cat = Cat("Mica")

#first_cat.introduce()
#second_cat.introduce()