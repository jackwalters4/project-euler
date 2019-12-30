#Jack Walters
#Solution to Project Euler 6
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Sum of the squares
squares = [i*i for i in range(101)]
sum_squares = sum(squares)

#Square of the sum
nums = [i for i in range(101)]
square_sum = sum(nums) * sum(nums)

print(square_sum - sum_squares)
