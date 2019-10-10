s = "asdrgoticdfgh"
t = "asefgotiaser"
def lcs(s,t):
	m = len(s)
	n = len(t)
	#create an m * n list
	lcsA = [[0 for k in range(n + 1)] for l in range(m + 1)]
	maxsub = 0
	for i in range(m + 1):
		for j in range(n + 1):
			if i == 0 or j == 0:
				lcsA[i][j] = 0
			elif s[i - 1] == t[j - 1]:
				lcsA[i][j] = lcsA[i - 1][j - 1] + 1
				maxsub = max(maxsub,lcsA[i][j])
			else:
				lcsA[i][j] = 0
	return maxsub

print(lcs(s,t))