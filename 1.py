list = []
for x in range(0,1000):
	if x % 3 == 0 or x % 5 == 0:
		list.append(x)

sum = 0
for i in list:
	print i
	sum += i

print sum

