#Jack Walters
#Solution to Project Euler 5
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Implementation isn't working

def gcd(a, b) :
	num = max(a,b)
	while ((num % a != 0) and (num % b != 0)) :
		num += 1
	return num


result = 1
for i in range(1,20) :
	result *= i
	result /= gcd(result, i)

print(result)