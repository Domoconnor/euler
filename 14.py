def rules(n):
	if n % 2 == 0:
		return n/2
	else:
		return (3*n)+1

maxCounter = 0
maxNumber = 0

for i in range(13,1000000):
	counter = 0
	num = i
	while num > 1:
		num = rules(num)
		counter += 1

	if counter>maxCounter:
		maxCounter = counter
		maxNumber = i
print(maxNumber)