def factor(value):
    factors = []
    for i in range(1, int(value**0.5)+1):
        if value % i == 0:
            factors.append((i, value / i))
    return factors

currentNum = 1
total = 1

found = False

while found == False:
	currentNum +=1
	total += currentNum
	if len(factor(total))>250:
		print(total)
		found = True
