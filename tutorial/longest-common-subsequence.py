
def lcsubseq(s,t,m,n,lookup):
	if m == 0 or n == 0:
		return 0
	key = str(m) + "," + str(n)
	if lookup.get(key, -1) == -1:
		if s[m - 1] == t[n - 1]:
			return lcsubseq(s,t,m - 1,n - 1, lookup) + 1
		else:
			return max(lcsubseq(s,t,m - 1,n, lookup),lcsubseq(s,t,m,n - 1, lookup))
	return lookup[key]

print(lcsubseq("ACE","ABCDE", 3, 5, {}))

#if x[m] == y[n] -- LCS(x[1...m], y[1...n]) = LCS(x[1...m-1], y[1...n-1]) + 1
#if x[m] != y[n] -- LCS(x[1...m], y[1...n]) = MAX{LCS(x[1...m - 1], y[1...n]), LCS(x[1...m], y[1...n - 1])}