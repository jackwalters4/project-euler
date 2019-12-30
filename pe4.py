#Jack Walters
#Solution to Project Euler 4
#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num) :
	word = str(num)
	for i in range(len(word) - 1):
		if (word[i] != word[len(word) - 1 -i]) :
			return False
	return True

max = 0
for i in range(100,999) :
	for j in range(100,999) :
		if (is_palindrome(i*j) and (i*j > max)) :
			max = i * j


print(max)