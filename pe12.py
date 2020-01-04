#Jack Walters
#Solution to Project Euler 12
#What is the value of the first triangle number to have over five hundred divisors?

import math

#factors function from project euler 3
def factors(num) :
	i = int(math.sqrt(num))
	x = []
	while (i > 0) :
		if (num % i == 0) :
			x.append(i)
		i -= 1
	return x

def triangle_number(num) :
	return sum(i for i in range(1, num + 1))
		

factors_triangle = []
i = 1
while(len(factors_triangle) < 500) :
	factors_triangle = factors(triangle_number(i))
	i += 1

print(triangle_number(i)) 