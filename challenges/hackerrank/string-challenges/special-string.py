# Medium
# A string is said to be a special string if either of two conditions is met:

# All of the characters are the same, e.g. aaa.
# All characters except the middle one are the same, e.g. aadaa.
# A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.
# n * (n + 1) / 2 -- total number of possible substrings

def genSims(s):
	n = len(s)
	i = n - 1
	j = n - 2
	sims = [0] * n
	while j >= 0:
		if s[i] == s[j]:
			sims[j] = sims[i] + 1
		else:
			sims[j] = 0
		j -= 1
		i -= 1
	return sims
# Complete the substrCount function below.
def substrCount(n, s):
	sims = genSims(s)
	i = 0
	specialChars = 0
	while i < n:
	if sims[i] > 0:
		# we have encountered repeating strings so compute their possible sub strings and skip to the next index after my repetitions
		specialChars += ((sims[i] + 1) * (sims[i] + 2))//2
		i = sims[i] + i + 1
	else:
		# this is not a repeated string occurence
		#the character itself is a special character
		specialChars += 1
		#check for the characters middle palindrome
		j = i - 1
		k = i + 1
		prev = -1
		while j >= 0 and k < n and s[j] == s[k]:
			if prev == -1:
				specialChars += 1
				prev = s[j]
			else:
				if s[j] == prev:
						specialChars += 1
				else:
						break
			j -= 1
			k += 1
		i += 1
	return specialChars
