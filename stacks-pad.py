#Python Algorithms and Data Structures

# Last In First Out (LIFO) protocol

#used in solving maze problem
class ListStack : 
	def __init__(self):
		self.items = list()
		self.size = 0

	def __len__(self):
		return self.size

	def __contains__(self, data):
		return True

	def isEmpty(self):
		return self.size == 0

	def pop(self):
		assert not self.isEmpty(), "Cannot pop from an empty stack"
		return self.items.pop()

	def push(self, item):
		self.items.append( item )

	def peek(self):
		assert not self.isEmpty(), "Cannot peek at an empty stack"
		return self.items[-1]

class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None

class LinkedListStack :
	def __init__():
		self.size = 0
		self.top = None

	def __len__( self ):
		return self.size
	
	def isEmpty( self ):
		return self.top is None

	def peek(self):
		assert not self.isEmpty(), "Cannot pop from an empty stack"
		return self.top.item
	
	def push(self, item):
		newNode = Node(item)
		newNode = self.top 
		self.top = newNode
		self.size += 1
	
	def pop(self):
		assert not self.isEmpty(), "Cannot pop from an empty stack"
		node = self.top
		self.top = self.top.next
		self._size -= 1
		return node.item