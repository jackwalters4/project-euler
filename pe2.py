#Jack Walters
#Solution to Project Euler 2
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
#find the sum of the even-valued terms.

a = 1
b = 2
result = 0
upper_bound = 4000000

while (b < upper_bound) :
	if (b % 2 == 0) :
		result += b 
	temp = a + b
	a = b
	b = temp

print(result)
