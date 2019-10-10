# Medium

#Given an array of integers, find the maximum subset containing integers that the sum of any two integers will not be divisible by a value k
# Example: if you have [1,7,2,4] the greatest non divisible subset is [1,7,4]
def nonDivisibleSubset(k, s):
	# Create an array for the possible remainders of K when it divides a number
	counts = [0] * k
	#loop through s and find the number of times a remainder of value Y occurs for K when K divides a number
	for number in s:
		counts[number % k] += 1

	# If K evenly divides a number we can take at most one because adding that one with any other one will produce a number easily divisible by k
	count = min(counts[0], 1)
	# from one to the middle of K compare the number of numbers that have that remainder with its correspondent part
	# Example for k = 5, [0,1,2,3,4] -- the numbers here represent the indexes.
	# We compare 1,4 and 2,3
	# Take the maximum between each number and it's correspondent since we finding the mximum subset
	for i in range(1, (k//2)+1):
		# We check for the equality to avoid the case of even numbers
		# for example for six, pairs will be 1,5 2,4 and 3,3
		#hence we ignore the 3,3 case
		if i != k - i:
			count += max(counts[i], counts[k-i])
	# we add that 3,3 case here snce it can only ever be a single number
	if k % 2 == 0: 
		count += 1
	return count