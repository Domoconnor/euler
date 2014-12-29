currentNum = 1
prevNum = 1
sum = 0

while currentNum < 4000000:
	if currentNum % 2 == 0:
		sum += currentNum

	tmp = currentNum + prevNum
	prevNum = currentNum
	currentNum = tmp

print sum 