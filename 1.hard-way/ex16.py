from sys import argv

script, filename = argv

print("We're going to erase %s." % filename)
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file.  Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line = input("line 1: "), input("line 2: "), input("line 3: ")

print ("I'm going to write these to the file.")

for item in line:
	target.write(item)
	target.write("\n")

print ("And finally, we close it.")
target.close()