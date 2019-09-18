#Python Algorithms and Data Structures

# ROOT is the topmost Node -- does not have an incoming edge and is the entry point of any tree

# NODES are arranged in levels with root node at level 0
# DEPTH is the distance between a node and the root
# HEIGHT of a tree is the number of levels the tree has
# WIDTH is the number of levels containing most nodes
# SIZE is the number of nodes in the tree
# minimum height of a tree is log(n) + 1 where log in base 2

class BinayTreeNode :
	def __init__(self):
		self.data = None
		self.right = None
		self.left = None

# Depth first traversal
def traverseBinaryTree(node):
	if node is not None:	
		traverseBinaryTree(node.left)
		print(node.data)
		traverseBinaryTree(node.right)

def postOrderTraversal(node):
	if node is not None:	
		traverseBinaryTree(node.left)
		traverseBinaryTree(node.right)
		print(node.data)

def reverseTravesal(node):
	if node is not None:	
		traverseBinaryTree(node.right)
		print(node.data)
		traverseBinaryTree(node.left)
		
# Breath First Traversal
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

def breadthFirstTraversal( bintree ):
	# Create a queue and add the root node to it.
	q =  LinkedListQueue()
	q.enqueue( bintree )
	# Visit each node in the tree.
	while not q.isEmpty() :
		# Remove the next node from the queue and visit it.
		node = q.dequeue()
		print( node.data )
		# Add the two children to the queue.
		if node.left is not None :
			q.enqueue( node.left )
		if node.right is not None :
			q.enqueue( node.right )

root = BinayTreeNode()
left = BinayTreeNode()
right = BinayTreeNode()

root.data = 10
left.data = 5
right.data = 20

root.left = left
root.right = right

#breadthFirstTraversal(root)

# HEAPS 
# MAX HEAP - largest value is alwaysat the top, smallest values in leaf nodes. The Parent node value is larger than both of it's children

#Heaps are not stored as linked lists but rather as array with nodes having the relationship:
# parent = (i - 1) // 2
# left = 2 * i + 1
# right = 2 * i + 2

# An array-based implementation of the max-heap.
class MaxHeap :
# Create a max-heap with maximum capacity of maxSize.
	def __init__( self, maxSize ):
		self._elements = maxSize * [None]
		self._count = 0
		# Return the number of items in the heap.
	def __len__( self ):
		return self._count
	# Return the maximum capacity of the heap.
	def capacity( self ):
		return len( self._elements )
	# Add a new value to the heap.
	def add( self, value ):
		assert self._count < self.capacity(), "Cannot add to a full heap."
		# Add the new value to the end of the list.
		self._elements[ self._count ] = value
		self._count += 1
		# Sift the new value up the tree.
		self._siftUp( self._count - 1 )
		# Extract the maximum value from the heap.
	def extract( self ):
		assert self._count > 0, "Cannot extract from an empty heap."
		# Save the root value and copy the last heap value to the root.
		value = self._elements[0]
		self._count -= 1
		self._elements[0] = self._elements[ self._count ]
		# Sift the root value down the tree.
		self._siftDown( 0 )
	# Sift the value at the ndx element up the tree.
	def _siftUp( self, ndx ):
		if ndx > 0 :
			parent = ndx - 1 // 2
			if self._elements[ndx] > self._elements[parent] :
				tmp = self._elements[ndx]
				self._elements[ndx] = self._elements[parent]
				self._elements[parent] = tmp
				self._siftUp( parent )
	# Sift the value at the ndx element down the tree.
	def _siftDown( self, ndx ):
		left = 2 * ndx + 1
		right = 2 * ndx + 2
		# Determine which node contains the larger value.
		largest = ndx
		if left < count and self._elements[left] >= self._elements[largest] :
			largest = left
		elif right < count and self._elements[right] >= self._elements[largest]:
			largest = right
		# If the largest value is not in the current node (ndx), swap it with
		# the largest value and repeat the process.
		if largest != ndx :
			swap( self._elements[ndx], self._elements[largest] )
			#node is now at the largest index, sift it down again
			_siftDown( largest )

def simpleHeapSort( theSeq ):
	# Create an array-based max-heap.
	n = len(theSeq)
	heap = MaxHeap( n )
	# Build a max-heap from the list of values.
	for item in theSeq :
		heap.add( item )
	# Extract each value from the heap and store them back into the list.
	for i in range( n, 0, -1 ) :
		theSeq[i] = heap.extract()

# Min HEAP - smallest value at the top, larger values in leaf nodes. Parent node value is less than that of both it's chldren