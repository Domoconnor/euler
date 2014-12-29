import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

i=0
primes = []
found = False
while found == False:
	if isPrime(i):
		primes.append(i)
		if len(primes) == 10001:
			found = True
	i += 1
print(primes[10000])