i = 0
numbers = []

def while_loop(x):
	while i < x:
		global i
		print("At the top i is %d" % i)
		numbers.append(i)

		i += 1
		print("Numbers now: ", numbers)
		print("At the bottom i is %d" % i)
	return
while_loop(4)



print("The numbers: ")

for num in numbers:
	print(num)