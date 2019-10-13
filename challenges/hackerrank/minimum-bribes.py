#Hard

# people in a line are assienged sequential numbers
# each person can bribe at most two persons in front of them
# based on the configuration of the aray givem, determine the minimum bribe given or Too chaotic if someone bribed more than two persons

# trick is to count how many people might have bribed someone
def minimumBribes(q):
	n = len(q)
	totalBribes = 0
	for i in range(n):
		if (q[i] - 1) - i > 2:
			totalBribes = "Too chaotic"
			break
		# look trhough my original postion - 1 to my current position + 1 and count how many elements have a value larger than mine
		for j in range(max(0, q[i] - 2), i):
			if q[j] > q[i]:
				totalBribes += 1
	print(totalBribes) 