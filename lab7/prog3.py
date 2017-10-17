class TreeNode:
	def __init__(self,value):
		self.val=value
		self.parent=None
		self.right=None
		self.left=None

class BinSearchTree:
	def __init__(self,rootval):
		self.root=TreeNode(rootval)


	def search(self,key):
		trav=self.root
		
		while trav!=None:
			if trav.val==key:
				return trav
			if trav.val>key:
				trav=trav.left
			else:
				trav=trav.right
		else:
			return


	def insert(self,val):
		node=TreeNode(val)
		temp=self.root
		#flag is used to decide the which child is the new node
		#if flag is 0 then new node is left child of temp else it is the right child 
		flag=0
		while temp!=None:
			if temp.val>=val:
				prev=temp
				temp=temp.left
				flag=0
			else:
				prev=temp
				temp=temp.right
				flag=1
		node.parent=prev
		if flag==0:
			prev.left=node
		else:
			prev.right=node

	def delete(self,val):
		node=self.search(val)
		#node is a leaf
		if node.left==None and node.right==None:
			if node.parent.val<node.val:
				node.parent.right=None
			else:
				node.parent.left=None
			node.parent=None
		#node has exactly one child
		elif node.left==None or node.right==None:
			if node.left==None:
				curr=node.right
				node.right=None
			else:
				curr=node.left
				node.left=None
			curr.parent=node.parent
			if node.parent.val<node.val:
				node.parent.right=curr
			else:
				node.parent.left=curr
			node.parent=None
		#node has two children
		else:
			curr=self.successor()
			curr.parent=node.parent
			curr.left=node.left
			curr.right=node.right
			node.parent=None
			node.left=None
			node.right=None


def isBinHeap(tree):
	par=tree.root
	while(par!=None):
		left=tree.root.left
		right=tree.root.right		
		if par.val<left.val or par.val<right.val:
			return False
		else:
			par=par.left
	par=tree.root
	while(par!=None):
		left=tree.root.left
		right=tree.root.right		
		if par.val<left.val or par.val<right.val:
			return False
		else:
			par=par.right
	return True




def main():

	node=BinSearchTree(25)
	node.insert(12)
	node.insert(15)
	node.insert(123)
	node.insert(45)
	print(isBinHeap(node))


if __name__ == '__main__':
	main()