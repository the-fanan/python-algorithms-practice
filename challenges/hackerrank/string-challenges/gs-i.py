# A company invests in three companies A, B, C
# given a string shoqing all their investments for a specific time period, find all the time periods in which A, B and C were invested in

# Example, if INV = "ABBCBBA"
# investments =  7 because "ABBC", "ABBCB", "ABBCBB", "ABBCBBA", "BBCBBA", "BCBBA", "CBBA"

def investmentsDone(s):
	n = len(s)
	A = 65
	B = 66
	C = 67
	i = j = 0
	Ahol = Bhol = Chol = 0
	investments = 0
	while i < n - 2:
		if j >= n:
			break
		if ord(s[j]) == A:
			Ahol += 1
		elif ord(s[j]) == B:
			Bhol += 1
		elif ord(s[j]) == C:
			Chol += 1
		while Ahol > 0 and Bhol > 0 and Chol > 0:
			investments += n - j
			if ord(s[i]) == A:
				Ahol -= 1
			if ord(s[i]) == B:
				Bhol -= 1
			if ord(s[i]) == C:
				Chol -= 1
			i += 1
		j += 1
	return investments
#print(investmentsDone3("ABBCZBAC"))
#print(investmentsDone("ABCCBA" * 1000000))