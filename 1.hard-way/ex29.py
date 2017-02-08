people = 20
cats = 5
dogs = 17

if people < cats:
	print("Too many cats! The world is doomed!")

if people > cats:
	print("Not many cats! The world is saved!")

if people < dogs:
	print("The world is drooled on!")

if people > dogs:
	print("The world is dry!")


dogs += 5

if people >= dogs:
	print("People are greater than or equal to dogs.")

if people <= dogs:
	print("People are less than or equal to dogs.")

if people == dogs:
	print("People are dogs.")


if not (True or False) == False:
	print("That is correct.")

if False and True:
	print("False")

if people != 19:
	print("People are there")

if people != 20:
	print("No people.")

if people == people:
	print("Yes")