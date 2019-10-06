#Python Algorithms and Data Structures

from array import Array
# First In First Out (FIFO)

# has worst caserunning time of O(n)
class ListQueue :
	def __init__(self):
		self.items = list()
		self.size = 0

	def __len__(self):
		return self.size

	def isEmpty(self):
		return self.size == 0

	def enque(self,item):
		self.items.append(item)
		self.size += 1
	
	def deque(self):
		assert not self.isEmpty(), "Cannot dequeue from an empty queue."
		self.size -= 1
		return self.items.pop(0)

# can only handle small capacity and maximu queue size must be given
class CircularArrayQueue :
	def __init__(self, maxSize):
		self.size = 0
		self.front = 0
		self.back = 0
		self.items = Array(maxSize)
	
	def __len__(self):
		return self.size

	def isEmpty(self):
		return self.size == 0
	
	def isFull(self):
		return self.size == len(self.items)

	def enque(self, item):
		assert not self.isFull(),"Queue is full."
		self.back = (self.back + 1) % len(self.items)
		self.items[self.back] = item
		self.size += 1
	
	def deque(self):
		assert not self.isEmpty(), "Cannot dequeue from an empty queue."
		front = self.items[self.front]
		self.items[self.front] = None
		self.front = (self.front + 1) % len(self.items)
		self.size -= 1
		return front

class QueueNode( object ):
	def __init__( self, item ):
		self.item = item
		self.next = None

class LinkedListQueue :
	def __init__(self):
		self.size = 0
		self.head = None
		self.tail = None
	
	def __len__( self ):
		return self.size
	
	def isEmpty( self ):
		return self.head is None

	def enqueue( self, item ):
		node = QueueNode( item )
		if self.isEmpty() :
			self.head = node
		else :
			self.tail.next = node
		self.tail = node
		self.size += 1
	
	def dequeue( self ):
		assert not self.isEmpty(), "Cannot dequeue from an empty queue."
		node = self.head
		if self.head is self.tail :
			self.head = None
			self.tail = None
		else:
			self.head = self.head.next
		self.size -= 1
		return node.item

# Priority queues
