#Python Algorithms and Data Structures

# LINKED STRUCTURE is a collection of objects(NODES) that contain DATA and a reference(LINK) to another node
# Last node is called TAIL node and has a NULL link reference

# Suitable for large amounts of DYNAMIC data involving large number of insertions and deletions

class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None

class LinkedListBag :
	def __init__(self):
		self.size = 0
		self.head = None
		self.tail = None
	
	def __len__( self ):
		return self.size

	# Determines if an item is contained in the bag.
	def __contains__( self, target ):
		curNode = self._head
		while curNode is not None and curNode.item != target :
			curNode = curNode.next
		return curNode is not None
	
	def add(self, item):
		newNode = Node(item)
		newNode.next = self.head
		if self.size == 0:
			self.tail = newNode
		self.head = newNode
		self.size += 1
	
	def prepend(self, item):
		self.add(item)
	
	def append(self, item):
		newNode = Node(item)
		if self.head is None:
			self.head = newNode
			self.tail = self.head
		else:
			self.tail.next = newNode
			self.tail = self.tail.next
		self.size += 1
	
	def remove(self, item):
		predecessorNode = None
		currentNode = self.head
		while currentNode is not None and currentNode.data != item:
			predecessorNode = currentNode
			currentNode = currentNode.next
		if currentNode is not None:
			if currentNode == self.head:
				self.head = self.head.next
			else:
				predecessorNode.next = currentNode.next
			if currentNode is self.tail :
				self.tail = predecessorNode

			self.size -= 1
			return currentNode.item
		return None

myBag = LinkedListBag()
myBag.add(10)
print(myBag)

# Traverse a linked list
def traversal( head ):
	curNode = head
	while curNode is not None :
		print(curNode.data)
		curNode = curNode.next

# Searching a node in a linked list
def unOrderedSearch( head, target ):
	curNode = head
	while curNode is not None and curNode.data != target :
		curNode = curNode.next
	#curNode is not True evaluates to True or False
	return curNode is not None

def orderedSearch( head, target ):
	curNode = head
	while curNode is not None and curNode.data < target :
		curNode = curNode.next
	#curNode is not True evaluates to True or False
	return curNode is not None

def prependToLinkedList(item, linkedList):
	newLinkedList = ListNode(item)
	newLinkedList.next = linkedList
	return newLinkedList

def removeNode(target, linkedList):
	predNode = None
	currentNode = linkedList
	while currentNode is not None and currentNode.data != target :
		predNode = currentNode
		currentNode = currentNode.next
	if currentNode is not None :
		if currentNode is linkedList :
			linkedList = currentNode.next
		else :
			predNode.next = currentNode.next
	return linkedList

def appendNode(newNode, tailNode, headNode):
	if headNode is None :
		headNode = newNode
	else :
		tail.next = newNode

def insertNodeInSortedList(node, head):
	predNode = None
	currNode = head
	while currNode is not None and node.data > currNode.data:
		predNode = currNode
		currNode = currNode.next
	if currNode == head:
		head = node 
	else:
		predNode.next = node
		node.next = currNode
	return head

#linked = ListNode(8)
#print("Link is created")
#traversal( linked )
#print("link is increased")
#linked = prependToLinkedList(6, linked)
#linked = prependToLinkedList(2, linked)
#traversal( linked )
#print("Link is reduced")
#linked = removeNode(10, linked)
#traversal( linked )
#print("Link is ordered")
#linked = insertNodeInSortedList(ListNode(7), linked)
#traversal( linked )
