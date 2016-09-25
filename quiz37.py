# allows us to access a random 'key' in the dictionary
import random

# the questions/answers dictionary
my_dict = {"how to import function from library" : "from module import function", "what shows the list of functions from module" : "dir()", "what is abs() good for" : "gives positive value", "empty block" : "pass", "extend the list" : ".append(' ')", "slice of the list letters = ['a', 'b', 'c'], only a, b" : "letters[0:1]", "insert a dog into the list 'animals' to the second place" : "animals.insert(1, 'dog')", "print the value of the key 'Puffin' in dictionary 'residents'" : "print(residents['Puffin'])", "put 'Chicken' with the price 14.50 into the dictionary 'menu'" : "menu['Chicken'] = 14.50", "remove 'Puffin' from the dictionary 'residents'" : "del residents['Puffin']", "remove 'dagger' from 'backpack' list" : "backpack.remove('dagger')", "the beginning of the line in regex" : "^", "the end of the line in regex" : "$", "how to import regex" : "import.re", "how do you look for regex in text" : "re.search", "how do you look for index in string" : "find()"}

# welcome message
print("Python Revision Quiz")
print("====================")

# the quiz will end when this variable becomes 'False'
playing = True

# While the game is running
while playing == True:
	
	#set the score to 0
	score = 0

	#gets the number of questions the player wants to answer
	num = int(input("\nHow many questions would you like: "))

	#loop the correct number of times
	for i in range(num):

		#the question is one of the dictionary keys, picked at random
		question = (random.choice(list(my_dict.keys())))
		
		#the answer is the string mapped to the question key
		answer = my_dict[question]

		#print the question, along with the question number
		print("\nQuestion" + str(i+1))
		print(question + "?")

		#get the user's answer attempt
		guess = input("> ")

		#if their guess is the same as the answer
		if guess.lower() == answer.lower():
			#add 1 to the score and print a message
			print("Correct!")
			score += 1
		else:
			print("Nope!")

	#after the quiz, print their final score
	print("\nYour final score was " + str(score))

	#store the user's input...
	again = input("Enter any key to play again, or 'q' to quit.")

	#... and quit if they type 'q'
	if again.lower() == 'q':
		playing = False
