#Python Algorithms and Data Structures


# 1. Recursive solution must have a BASE CASE
# 2. Recursive solution must have a RECURSIVE CASE
# 3. Recursive solution must move towards the base case

# Use when you have something to be returned. If you don't have anything to be returned use normal loops

# Can be used with stacks (Back tracking) to find next best move or optimal paths

def printReverse(n):
	if n > 0:
		print(n)
		printReverse(n - 1)

def factorial(n):
	assert n>= 0, "Only positive numbers can have factorials"
	if n < 2:
		return 1
	else:
		return n * factorial(n - 1)

def fibonnaci(n):
	assert n >=0, "Fibonacci only allowed for n > 1"
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonnaci(n - 1) + fibonnaci(n - 2)

#print(fibonnaci(30))

def dynamicFibonnaci(n):
	values = n * [0]
	return recFib(n,values)

def recFib(n,values):
	assert n >=0, "Fibonacci only allowed for n > 1"
	if n == 0:
		values[0] = 1
		return 0
	elif n == 1:
		values[1] = 1
		return 1
	else:
		if values[n - 1] != 0:
			left = values[n - 1]
		else:
			values[n - 1] = recFib(n - 1, values)
			left = values[n - 1]
		if values[n - 2] != 0:
			right = values[n - 2]
		else:
			values[n - 2] = recFib(n - 2, values)
			right = values[n - 2]
		return left + right

def recBinarySearch( target, theSeq, first, last ):
	# If the sequence cannot be subdivided further, we are done.
	if first > last :
	# base case #1
		return False
	else :
	# Find the midpoint of the sequence.
		mid = (last + first) // 2
	# Does the element at the midpoint contain the target?
		if theSeq[mid] == target :
			return True
		# base case #2
		# or does the target precede the element at the midpoint?
		elif target < theSeq[mid] :
			return recBinarySearch( target, theSeq, first, mid - 1 )
		# or does it follow the element at the midpoint?
		else :
		return recBinarySearch( target, theSeq, mid + 1, last )

# Tower of Hannoi Solution
# n is number of discs
# the base rquired 3 operations
# here nothing is to be returned however, towers of Hannoi can only be solved by recursion so we use recursion in place of loops
def move( n, src, dest, temp ):
	if n >= 1 :
		move( n - 1, src, temp, dest )
		print( "Move top disc from tower %d -> tower %d" % (src, dest))
		move( n - 1, temp, dest, src )

# Recursion better than iteration for exponents -- O(log n)
	def exp( x, n ):
		if n == 0 :
			return 1
		result = exp( x * x, n // 2 )
		if n % 2 == 0 :
			return result
		else :
			return x * result

	