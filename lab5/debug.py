class TreeNode:
	def __init__(self,value):
		self.val=value
		self.parent=None
		self.right=None
		self.left=None

	def insertLeft(self,node):
		self.left=node
		node.parent=self

	def insertRight(self,node):
		self.right=node
		node.parent=self

class BinSearchTree:
	def __init__(self):
		self.root=TreeNode('')

