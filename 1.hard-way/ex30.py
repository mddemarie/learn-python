people = 30
cars = 15
trucks = 30

if cars > people:
	print("We should take the cars.")
elif cars < people:
	print("We should not take the cars.")
else:
	print("We can't decide.")

if trucks > cars:
	print("That's too many trucks.")
elif trucks < cars:
	print("Maybe we could take the trucks.")
else:
	print("We still can't decide.")

if people > trucks:
	print("Alright, let's just take the trucks.")
else:
	print("Fine, let's stay home then.")

if people > cars or trucks == people:
	print("Take rather cars and ignore what was said before.")
elif people >= trucks:
	print("Maybe to drive a truck is not so difficult.")
else:
	print("The world is wrong.")