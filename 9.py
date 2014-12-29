x = 1000
for a in range(1,x/3):
	for b in range(a+1,x/2):
		c = x-a-b
		if c**2 == a**2 + b**2:
			print(a*b*c)
			