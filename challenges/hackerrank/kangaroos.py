# EASY
#Given two kangaroos with start point x1 and x2 and spead v1 and v2, determine if the Kangaroos will meet

def kangaroo(x1, v1, x2, v2):
	if (x1 > x2 and v1 >= v2) or (x2 > x1 and v1 <= v2):
		return "NO"
	if (x1-x2) % (v2-v1) == 0:
		return "YES"
	else:
		return "NO"