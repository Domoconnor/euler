import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

sum = 2
for i in range(3, 2000000):
	if isPrime(i):
		sum+=i
print(sum)