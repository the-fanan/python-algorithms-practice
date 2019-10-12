# PATTERN MATCHING

# Brute force -- returns index where match starts from or -1 if no match was found
# O(nm)

def bruteForcePatternMatch(haystack, needle):
	h,n = len(haystack), len(needle)
	#only consider possible starting points
	for i in range(h - n + 1):
		k = 0
		while k < n and haystack[i + k] == needle[k]:
			k += 1
		if k == n:
			#end of needle was reached
			return i
	#no match was found
	return -1
haystack = "s" * 100000000
haystack = haystack + "gkr"
needle = "gkr"
#print(bruteForcePatternMatch(haystack, needle))


# Boyer-Moore Algorithm
# Looking-Glass Heuristic: When testing a possible placement of P against T, begin the comparisons from the end of P and move backward to the front of P.
#Character-Jump Heuristic: During the testing of a possible placement of P within T, a mismatch of text character T[i]=c with the corresponding pattern character P[k] is handled as follows. If c is not contained anywhere in P, then shift P completely past T[i] (for it cannot match any character in P). Otherwise, shift P until an occurrence of character c in P gets aligned with T[i].
#O(nm) worst case running time
def boyerMoorePatternMatch(haystack, needle):
	h,n = len(haystack), len(needle)
	#If needle is empty
	if n == 0:
		return 0
	last = {} #initialise a dictionary to hold the last mismatch index for each element in the needle
	#populate the the dictionary for the current last mismatch
	for k in range(n):
		last[needle[k]] = k
	#start from end
	i = n - 1
	k = n - 1
	while i < h:
		if haystack[i] == needle[k]:
			#characters match
			if k == 0:
				#the complete string has been matched
				return i
			else:
				#examine previous character character
				i -= 1
				k -= 1
		else:
			# a mismatch occured
			# if the mismatched characer is contained in the needle set j to it's index else set j to -1
			# mismatch occurs before character was aligned -- use n - j + 1
			# mismatch occurs after character that was aligned use n - k
			j = last.get(haystack[i], -1)
			i += n - min(k,j+1)
			#restart k
			k = n - 1
	return -1
#print(boyerMoorePatternMatch(haystack, needle))



# Knuth-Morris-Pratt Algorithm -- O(n + m)
def computeFail(needle):
	m = len(needle)
	fail = [0] * m
	j = 1
	k = 0
	while j < m:
		if needle[j] == needle[k]:
			fail[j] = k + 1
			j += 1
			k += 1
		elif k > 0:
			k = fail[k - 1]
		else:
			j += 1
	return fail

def knuthMorrisPratt(haystack, needle):
	h,n = len(haystack), len(needle)
	if n == 0:
		return 0
	fail = computeFail(needle)
	j = 0
	k = 0
	while j < h:
		if haystack[j] == needle[k]:
			if k == n - 1:
				return j - n + 1
			j += 1
			k += 1
		elif k > 0:
			k = fail[k - 1]
		else:
			j += 1
	return -1
#print(knuthMorrisPratt(haystack, needle))



def myBoyerMooreImplementation(haystack, needle):
	"""Boyer Moore Algorithm special case where both strings have no repeating characters

	Parameters:
	haystack (str): string to be searched
	needle (str): string to be found

	Returns:
	int: index where matched pattern begins in haystack or -1
	"""
	h,n = len(haystack), len(needle)
	lid = {}
	#build last index dictionary
	for i in range(n):
		lid[needle[i]] = i
	
	i = n - 1
	j = n - 1

	while i < h:	
		if needle[j] == haystack[i]:
			if j == 0:
				return i
			i -= 1
			j -= 1
		else:
			#a mismatch
			k = lid.get(haystack[i], -1)
			i += n - min(j, k + 1)
			#reset j
			j = n - 1
	return -1
