# You are given a string. Delete characters in a string until you get an alternating string
# Return an integer denoting the maximum length alternating string you can find
# Example. Given beabeefeab, the maimum alternating string is babab -- 5

def validateAlt(s):
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			return False
	return True

def alternate(s):
	# get a list of distinct values in the string
	st = list(set(s))
	maxl = 0
	# Loop through the letters
	for x in range(len(st)):
		# Loop through the letters except what you have looped through
		for y in range(x+1, len(st)):
			#if the current character is either x or y then append to the string cpy
			cpy = ""
			for c in s:
				if c == st[x] or c == st[y]:
					cpy = cpy + c
			if validateAlt(cpy):
				maxl = max(maxl, len(cpy))
	return maxl
s = "asdcbsdcagfsdbgdfanfghbsfdab"
# expects 8
print(alternate(s))
#	cpy = [c for c in s if c==st[x] or c==st[y]]
# Rather than actually delete to get you answer tr and generate values from the given numbers and compare