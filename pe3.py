#Jack Walters
#Solution to Project Euler 3
#What is the largest prime factor of the number 600851475143 ?

import math

def factors(num) :
	i = int(math.sqrt(num))
	x = []
	while (i > 0) :
		if (num % i == 0) :
			x.append(i)
		i -= 1
	return x

def is_prime(num) :
	return len(factors(num)) == 1


x = factors(600851475143)
for i in x :
	if (is_prime(i)) :
		print(i)
		break


