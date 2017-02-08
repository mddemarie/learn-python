numbers = []
def while_loop():
	for number in range(0,6):
		print("At the top i is %d" % number)
		numbers.append(number)
		print("Numbers now: ", numbers)
		print("At the bottom i is %d" % number)
	return
while_loop()
print("The numbers: ")
for num in numbers:
	print(num)