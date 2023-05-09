# A utility function to search a given key in BST
def search(root, key):

	# Base Cases: root is null or key is present at root
	if root is None or root.val == key:
		return root

	# Key is greater than root's key
	if root.val < key:
		return search(root.right, key)

	# Key is smaller than root's key
	return search(root.left, key)

# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

	# A utility function to insert
	# a new node with the given key
	def insert(self, key):
		if self.val == key:
			return
		elif self.val < key:
			if self.right is None:
				self.right = Node(key)
			else:
				self.right.insert(key)
		else:
			if self.left is None:
				self.left = Node(key)
			else:
				self.left.insert(key)

# A utility function to do inorder tree traversal
def inorder(root):
	if root:
		inorder(root.left)
		print(root.val, end=" ")
		inorder(root.right)

# Driver code
if __name__ == '__main__':
	r = Node(50)
	r.insert(30)
	r.insert(20)
	r.insert(40)
	r.insert(70)
	r.insert(60)
	r.insert(80)

	# Print inoder traversal of the BST
	inorder(r)
