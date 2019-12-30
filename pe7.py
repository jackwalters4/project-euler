#Jack Walters
#Solution to Project Euler 7
#What is the 10001st prime number?
import math

def is_prime(num) :
	i = int(math.sqrt(num))
	while (i > 1) :
		if (num % i == 0) :
			return False
		i -= 1
	return True


def prime_numbers() :
	i = 2
	primes = []
	while (len(primes) < 10002) :
		if (is_prime(i)) :
			primes.append(i)
		i += 1
	return primes


print(prime_numbers()[10001])
