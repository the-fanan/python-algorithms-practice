l = [1,2,3,4,5]

def rotateLeft(l, rotations):
	n = len(l)

	if n == rotations:
		return l
	elif n < rotations:
		if rotations % n == 0:
			return l
		else:
			rotations = rotations % n
	l = l[rotations:] + l[:rotations]
	return l

#l = rotateLeft(l, 51)


def rotateRight(l, rotations):
	n = len(l)

	if n == rotations:
		return l
	elif n < rotations:
		if rotations % n == 0:
			return l
		else:
			rotations = rotations % n
	l = l[n - rotations:] + l[:n - rotations]
	return l

l = rotateRight(l, 7)
print(l)

