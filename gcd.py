#Eucledian Algorithm
def gcd(a,b):
	if a == 0:
		return b
	if b == 0:
		return a
	
	if a > b:
		return gcd(b, a%b)
	else:
		return gcd(a, b%a)
#My implementation
def ONgcd(a,b):
	gcd = 1
	minNum = 0
	if a > b:
		minNum = b
	else:
		minNum = a
	i = 1
	while i <= minNum:
		if a % i == 0 and b % i == 0:
			gcd = i
	return gcd
print(gcd(48,18))