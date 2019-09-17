mapping = [1,2,4,5,6,8,9,3,7,0]
num = ['990', '034', '16','116', '34','09']
#geberate the correct value and the oder 'num' in ascending order according p their actual values. If two actual values are same then follow order of occurrence in 'num'
def createListOfLists2(mapping, num):
	listOflists = list()
	if len(num) > 1:
		listOflists = listOflists + createListOfLists(mapping, num[:int(len(num)/2)])
		listOflists = listOflists + createListOfLists(mapping, num[int(len(num)/2):])
	else:
		actualValue = "";
		for i in range(len(num[0])):
			actualValue = actualValue + str(mapping.index(int(num[0][i])))
		listOflists.append([actualValue,num[0]])
	return listOflists

def recCLOL(mapping, num, newArr, start, end):
	n = len(num)
	if start == end:
		actualValue = ""
		for i in range(len(num[start])):
			actualValue = actualValue + str(mapping.index(int(num[start][i])))
		newArr[start] = [actualValue, num[start]]
	else:
		mid = (start + end) // 2
		recCLOL(mapping, num, newArr, start, mid)
		recCLOL(mapping, num, newArr, mid + 1, end)

def createListOfLists(mapping, num):
	n = len(num)
	newArr = len(num) * [0]
	recCLOL(mapping, num, newArr, 0, n - 1)
	return newArr

def mergeSortedLists(arr1,arr2):
	new = list()
	a = 0
	b = 0
	while a < len(arr1) and b < len(arr2):
		if int(arr1[a][0]) < int(arr2[b][0]):
			new.append(arr1[a])
			a += 1
		elif int(arr1[a][0]) == int(arr2[b][0]):
			indexOf1 = num.index(arr1[a][1])
			indexOf2 = num.index(arr2[b][1])
			if indexOf1 < indexOf2:
				new.append(arr1[a])
				a += 1
			else:
				new.append(arr2[b])
				b += 1
		else:
			new.append(arr2[b])
			b += 1
	if a < len(arr1):
		new = new + arr1[a:]
	
	if b < len(arr2):
		new = new + arr2[b:]
	return new
#imlements bubble sort
def sortListOfLists2(arr, num):
	sorting = True
	while sorting:
		swaps = 0
		for i in range(len(arr) - 1):
			if int(arr[i][0]) > int(arr[i + 1][0]):
				tempVal = arr[i]
				arr[i] = arr[i + 1]
				arr[i + 1] = tempVal
				swaps += 1
			elif int(arr[i][0]) == int(arr[i + 1][0]):
				indexOf1 = num.index(arr[i][1])
				indexOf2 = num.index(arr[i + 1][1])
				if indexOf1 > indexOf2:
					tempVal = arr[i]
					arr[i] = arr[i + 1]
					arr[i + 1] = tempVal
					swaps += 1
		if swaps == 0:
			sorting = False
	return arr
#implements merge sort
def sortListOfLists(arr, num):
	n = len(arr)
	if n == 1:
		return arr
	else:
		aL = sortListOfLists(arr[n//2:], num)
		bL = sortListOfLists(arr[:n//2], num)
		return mergeSortedLists(aL,bL)
	return arr

listOfLists = list();
listOfLists = sortListOfLists2(createListOfLists(mapping, num), num)

orderedList = list()
for i in range(len(listOfLists)):
	orderedList.append(listOfLists[i][1])

print(orderedList)		
print(listOfLists)

#<10^4 Bubble or Insertion sort
#<10^9 Merge or Heap sort
#for loops can be used for items less than 100



