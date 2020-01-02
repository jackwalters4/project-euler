#Jack Walters
#Solution to Project Euler 9
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def is_triplet(a, b, c) :
	return (a*a + b*b == c*c)

for a in range(1, 1001):
	for b in range(1, 1001):
		c = 1000 - (a + b)
		if (is_triplet(a,b,c)):
			print(a*b*c)
			exit()
