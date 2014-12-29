def isPalindrome(num):
	num = str(num)
	if num == num [::-1]:
		return True
	else:
		return False

current = 0

for i in range(0,999):
	for x in range(0, 999):
			product = x * i

			if isPalindrome(product) and product > current:
				current = product

print(current)


			