# with and as keywords:
with open('text.txt', 'w') as f:
	f.write('Hi there!')

# practicing continue
x = [1, 2, 3, 4]
for x in range(0,3):
	print(x)
	continue
	print(x - 1)

# practicing exec
exec('print("hi!")')

choice = [1, 2]
for item in choice:
	print(choice)

# practicing is
if choice is x:
	print(choice)
	print(x)

# practicing lambda
s = lambda b: b ** b; s(3)

# practicing pass
def empty():
	pass
	print(2 + 3) 
# practicing string escape sequences
print("Yesterday I had a late\v shift, I am happy that I can sleep longer than usually.")

# practicing operators
print("Hi!"); print("Hello!")

this = [1, 3]
for i in this:
	i %= i
	print(i)

# practicing yield
def new():
	yield Z
new().next()

# practicing raise
raise SyntaxError("No!")

