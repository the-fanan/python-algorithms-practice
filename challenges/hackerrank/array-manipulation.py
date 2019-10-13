# Hard
# you are given
# arrayManipulation has the following parameters:
#n - the number of elements in your array
#queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.

def arrayManipulation(n, queries):
	e = [0] * (n + 1)
	for query in queries:
		e[query[0] - 1] += query[2]
		e[query[1]] -= query[2]
		#only store how much the boundaries changed from their predecessors
	
	maxS = x = 0
	#sum the changes and return the max sum gotten as the array was traversed
	for val in e:
		x = x + val
		if maxS < x:
			maxS = x
	return maxS