l = [1,2,3,4,5]
r = [1,2,3,4,5]
def rotateLeft(l, rotations):
	n = len(l)
	rotations = rotations % n
	if rotations == 0:
		return l
	else:
		l = l[rotations:] + l[:rotations]
	return l

print(rotateLeft(l, 2))


def rotateRight(l, rotations):
	n = len(l)
	rotations = rotations % n
	if n == rotations:
		return l
	else:
		l = l[n - rotations:] + l[:n - rotations]
	return l
print(rotateRight(r, 2))

