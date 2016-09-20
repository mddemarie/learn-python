# this imports argv from sys
from sys import argv

# this creates the variable for additional file
script, input_file = argv

# this reads some file
def print_all(f):
	print(f.read())

# 0 seeks for the beginning of the file f (1 would mean current file position, 2 - the end)
def rewind(f):
	f.seek(0)

# this function prints number of the line and reads a line from a file
def print_a_line(line_count, f):
	print (line_count, f.readline())

# creates variable with open function
current_file = open(input_file)

# prints the sentence
print("First let's print the whole file:\n")

# it executes the function print_all for variable current_file
print_all(current_file)

# prints the sentence
print("Now let's rewind, kind of like a tape.")

# it executes rewind function for variable current_file
rewind(current_file)

# prints the sentence
print("Let's print three lines:")

# it creates variable current_line with number 1 in it
# it executes print_a_line function with 2 new paramenters
current_line = 1
for i in range(3):
	print_a_line(current_line, current_file)
	current_line += 1