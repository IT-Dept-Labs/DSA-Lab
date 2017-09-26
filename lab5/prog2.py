class TreeNode:
	def __init__(self,value):
		self.val=value
		self.parent=None
		self.right=None
		self.left=None

class Parsetree:
	def __init__(self):
		self.root=TreeNode('')

	def insert(self,exp):
		tree=self.root
		curr=tree
		for i in exp:
			if i == '(':
				temp=TreeNode('')
				curr.left=temp
				curr.parent=curr
				curr=temp
			print(curr)
			print(i)
			if i=='+' or i=='-' or i=='*' or i=='/':
				curr.val=i
			if i==')':
				curr=curr.parent
			if i.isdigit():
				if curr.left!=None:
					temp=TreeNode(i)
					temp.parent=curr
					curr.left=temp
				elif curr.right!=None: 
					temp=TreeNode(i)
					temp.parent=curr
					curr.right=temp
				curr=curr.parent


def preorderTree(trav):
	if trav:
		print(trav.val),
	
	if trav.left!=None:
		preorderTree(trav.left)
	if trav.right!=None:
		preorderTree(trav.right)

def main():
	pt=Parsetree()
	pt.insert('(4+3)*(5-2)')
	preorderTree(pt)

if __name__ == '__main__':
	main()