#Python Algorithms and Data Structures


#linear search --  this has comlexity of O(n) can work for up to 10^9 items in 1 second
obj = 5
arr = [1,2,5,3,4,6,7,9,11,8,10, 13]
sortedArr = range(20)
def linearSearchUnsorted(obj, arr):
	for i in range(len(arr)):
		if obj == arr[i]:
			return True
	return False
#print(linearSearchUnsorted(obj, arr))

def linearSearchSorted(obj, sortedArr):
	for i in range(len(arr)):
		if obj == arr[i]:
			return True
		if obj < arr[i]:
			return False
	return False

#print(linearSearchSorted(obj, arr))

def findSmallestValue(arr):
	smallestValue = arr[0]
	for i in range(len(arr)):
		if smallestValue > arr[i]:
			smallestValue = arr[i]
	return smallestValue
#print(findSmallestValue(sortedArr))

#binary search -- has runtime of O(log n) >10^9 
def binarySearch(obj, sortedArray):
	low = 0
	high = len(sortedArray) -1 

	while low <= high:
		mid = (low + high) // 2
		if obj == sortedArray[mid]:
			return True
		elif obj < sortedArray[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return False
#print(binarySearch(45,sortedArr))

def findInsertIndex(obj, sortedArray):
	low = 0
	high = len(sortedArray) -1 

	while low <= high:
		mid = (low + high) // 2
		if obj == sortedArray[mid]:
			return mid
		elif obj < sortedArray[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return low
#print(findInsertIndex(45,sortedArr))
def insertItemInASortedManner(obj,arr):
	index = findInsertIndex(obj, arr)
	arr.append(0)
	pos = len(arr) - 1
	#shift items to right
	while pos > index:
		arr[pos] = arr[pos - 1]
		pos -= 1
	arr[index] = obj
	return arr

#print(insertItemInASortedManner(6,list(range(6)) + list(range(7,10))))


