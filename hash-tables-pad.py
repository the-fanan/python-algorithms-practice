#Python Algorithms and Data Structures

#non-comparison-based algorithm

# collisions -- constant, quadratic and key hashing solutions

# REHASHING

#for developing hash functions
# 1. Simple for quick results
# 2. result must not be random. Same value must return same key
# 3. if a key contains multiple parts, every part must be used in calculating the hash
# 4. Table size should be a prime number

#PROBES
#   i is the iTH probe in the sequence, home is the position the key was originaly mapped to
# Liniear = (home + i) % N
# Modified Linear = (home + i ∗ c) % N
# Quadratic = (home + i^2 ) % M
# Double hashing = (home + i ∗ hp(key)) % M where hp(key) = 1 + key % P where P < M and M & P are prime

def divisionHash(key, N):
	# N =  length f hash table
	return key % N

# use when you know the length of data
def truncationHash(key):
	newKey = str(key.index(0)) + str(key.index(3)) + str(key.index(4))
	return int(newKey)

def foldHash(key):
	# 456789 -> 45 + 67 + 89
	return None

# String hash s0 a^n−1 + s1 a^n−2 + · · · + sn−3 a^2 + sn−2 a + sn−1
# a is a Constant, s is the ASCII integer equivalent of the string