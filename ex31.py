print("You enter a dark room with four doors. Do you go through door #1, door #2, door #3 or #4?")

door = input("> ")

if door == "1":
	print("There's a giant bear here eating a cheese cake. What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")

	bear = input("> ")

	if bear == "1":
		print("The bear eats your face off. Good job!")
	elif bear == "2":
		print("The bear eats your legs off. Good job!")
	else:
		print("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
	print("You stare into the mirror of virtual reality and you see yourself in it. What do you do?")
	print("1. You entrance the mirror and explore the world of parallel reality.")
	print("2. You throw a stone into mirror and the mirror breaks into many peaces.")
	print("3. You start to speak to yourself in the mirror.")

	insanity = input("> ")

	if insanity == "1":
		print("Your body becomes virtual and there is no option to escape your virtual body. Good job!")
	elif insanity == "2":
		print("The peaces become liquid and start to hunt you. Good job!")
	elif insanity == "3":
		print("You in the mirror is answering but is the true opposite of you and attempts become you. Good job!")
	else:
		print("You chose %s. The mirror disappeared and you can continue walking." % insanity)

elif door == "3":
	print("There's Schrödinger's cat and miaows cutely. What do you do?")
	print("1. Pet the cat.")
	print("2. Steal the cat and run away.")
	print("3. Expel the cat and live there alone.")

	cat = input("> ")

	if cat == "1":
		print("Cat chains you to the ground and runs away instead. You gave a freedom to the cat and became Schrödinger's human kind instead. Good job!")
	elif cat == "2":
		print("Cat bites you and you get a new dangerous infectious disease of existence/non-existence. Good job!")
	elif cat == "3":
		print("Cat becomes a jaguar and eats you/does not eat you. Good job!")
	else:
		print("%s interrupts the Schrödinger's algorithm and you appear at home with your puppy." % cat) 

elif door == "4":
	print("There are 3 doors in the room. One door on the left (1), one door on the right (2) and one door in front (3). Entrance one of them.")

	room = input("> ")

	if room == "1":
		print("The door is locked. Find the key.")
		room = input("Try it again:" ) #maybe a bug here
		if room == "2":
			print ("There is a box. What will you do?")
			box = input("> ")
			if box == "open" or "unpack" or "unlock" or "open the box" or "unpack the box" or "unlock the box":
				print("There is a key! Take the key.")
				take_key = input("> ")
				if take_key == "Take the key" or "take the key" or "take" or "take it":
					print("The key was taken. What do you wanna do next?")
					print("1. Go into the previous room.")
					print("2. Open the door on the right side.")
					print("3. Open the door on the left side.")
					next = input("> ")
					if next == "1":
						print("What do you want to do now?")
						prev_room = input("> ")
						if prev_room == "Open door on the left" or "open the door" or "open the left door" or "open the door 1":
							print("The door is opened and there is a bear again. Good job!")
					elif next == "2":
						print("You freed a cat. Good job!")
					elif next == "3":
						print("You have got out of the magic house. Congratulations!")
					else:
						print("Not possible! You lost")
				else:
					print("You cannot do this! You lost")
			else:
				print("You cannot do this! That's wrong. Game over!")
		elif room == "3":
			print("There is another room! Open it!" ">write 'open'<")
			op_door1 = input("> ")
			if op_door1 == "Open" or "open":
				print("You are in another room. There is another door!")
				op_door2 = input("> ")
				if op_door2 == "Open" or "open":
					print("You are in another room. There is another door!")
					op_door3 = input("> ")
					if op_door3 == "Open" or "open":
						print("There are infinite doors and rooms. You are forever lost! Haha!")
					else:
						print("Game over, try again!")
				else:
					print("Game over, try again!")
			else:
				print("Not possible, game over!")
		else:
			print("Not possible, game over!")
	elif room == "2":
		print ("There is a box. What will you do?")
		box = input("> ")
		if box == "open" or "unpack" or "unlock" or "open the box" or "unpack the box" or "unlock the box" or "Open" or "Unpack" or "Unlock" or "Open the box":
			print("There is a key! Take the key.")
			take_key = input("> ")

			if take_key == "Take the key" or "take the key" or "take" or "take it":
				print("The key was taken. What do you wanna do next?")
				print("1. Go into the previous room.")
				print("2. Open the door on the right side.")
				print("3. Open the door on the left side.")

				next = input("> ")
				if next == "1":
					print("What do you want to do now?")
					prev_room = input("> ")

					if prev_room == "Open door on the left" or "open the door" or "open the door 1" or "open left door" or "open the left door":
						print("The door is opened and there is a bear again. Good job!")
				elif next == "2":
					print("You freed a cat. Good job!")
				elif next == "3":
					print("You have got out of the magic house. Congratulations!")
				else:
					print("Not possible! You lost")
				
			else:
				print("You cannot do this! You lost")
		else:
			print("You cannot do this! That's wrong. Game over!")
	elif room == "3":
		print("There is another room! Open it!" ">write 'open'<")
		op_door1 = input("> ")
		if op_door1 == "Open" or "open":
			print("You are in another room. There is another door!")
			op_door2 = input("> ")
			if op_door2 == "Open" or "open":
				print("You are in another room. There is another door!")
				op_door3 = input("> ")
				if op_door3 == "Open" or "open":
					print("There are infinite doors and rooms. You are forever lost! Haha!")
				else:
					print("Game over, try again!")
			else:
				print("Game over, try again!")

		else:
			print("Not possible, game over!")
	else:
		print("Not possible, game over!")
else:
	print("You stumble around and fall into black hole and die. Good job!")
