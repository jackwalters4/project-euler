#Jack Walters
#Solution to Project Euler 10
#Find the sum of all the primes below two million.

#Not efficient enough, look for more efficient way to find primes
#Sieve of Eratosthenes

import math

def is_prime(num) :
	i = int(math.sqrt(num))
	while (i > 1):
		if (num % i == 0) :
			return False
		i -= 1
	return True

i = 2
upper_bound = 2000000
x = 0
while (i < upper_bound) :
	if (is_prime(i)) :
		x += i
	i += 1