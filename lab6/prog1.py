
class TreeNode:
	def __init__(self,value):
		self.val=value
		self.parent=None
		self.right=None
		self.left=None
		self.height=0

class AVLTree:
	def __init__(self,rootVal):
		self.root=TreeNode(rootVal)
		self.prev=self.root

	def search(self,key):
		trav=self.root
		
		while trav!=None:
			if trav.val==key:
				return trav
			if trav.val>key:
				self.prev=trav
				trav=trav.left
			else:
				self.prev=trav
				trav=trav.right
		else:
			return self.prev


	def  insert(self,key):
		node=TreeNode(key)
		temp=self.root
		#flag is used to decide the which child is the new node
		#if flag is 0 then new node is left child of temp else it is the right child 
		flag=0
		while temp!=None:
			if temp.val>=key:
				prev=temp
				temp=temp.left
				node.parent=prev
				flag=0
			else:
				prev=temp
				temp=temp.right
				node.parent=prev
				flag=1
			print('ht',prev.height,'val',prev.val)
		print('val',prev.val)
		
		if flag==0:
			prev.left=node
		else:
			prev.right=node

	
		trav=self.root
		
		while trav!=None:
			if trav.val>=key:
				if trav.left and trav.right:
					trav.height=max(trav.left.height+1,trav.right.height+1)
				else:
					trav.height+=1
				trav=trav.left
			else:
				if trav.left and trav.right:
					trav.height=max(trav.left.height+1,trav.right.height+1)
				else:
					trav.height+=1
				trav=trav.right


def preorderTraversal(trav):
	if trav:
		print(trav.val)
	if trav.left!=None:
		preorderTraversal(trav.left)
	if trav.right!=None:
		preorderTraversal(trav.right)

def main():
	t=AVLTree(5)
	t.insert(12)
	t.insert(1)
	t.insert(7)
	t.insert(20)
	preorderTraversal(t.root)
	print()
	print(t.root.right.left.height)
if __name__ == '__main__':
	main()



