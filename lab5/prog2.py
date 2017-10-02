import operator

class TreeNode:
	def __init__(self,value):
		self.val=value
		self.parent=None
		self.right=None
		self.left=None

	def getLeft(self):
		return self.left.val

	def getRight(self):
		return self.right.val

	def getRootVal(self):
		return self.val


class Parsetree:
	def __init__(self):
		self.root=TreeNode('')

	def insert(self,exp):
		tree=self.root
		curr=tree
		#print(curr,'\n\n')
		for i in exp:
			if i == '(':
				temp=TreeNode('')
				curr.left=temp
				temp.parent=curr
				curr=temp
			#print(curr.left)
			#print(i)
			if i in ['+', '-', '*', '/']:
				curr.val=i
				temp=TreeNode('')
				curr.right=temp
				temp.parent=curr
				curr=temp

			if i==')':
				curr=curr.parent

			if i.isdigit():
				curr.val=i
				curr=curr.parent




def printPrefix(trav):
	if trav:
		print(trav.val,end=" ")
	
	if trav.left!=None:
		printPrefix(trav.left)
	if trav.right!=None:
		printPrefix(trav.right)


def printPostFix(trav):
	if trav:
		printPostFix(trav.left)

		printPostFix(trav.right)

		print(trav.val,end=" ")
		#evaluate(trav.val)


def evaluate(trav):
	opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
	leftC=trav.getLeft()
	rightC=trav.getRight()
	if leftC.isdigit():
		leftC=int(leftC)
	if rightC.isdigit():
		rightC=int(rightC)

	if leftC and rightC:
		fn = opers[trav.getRootVal()]
		return fn(evaluate(leftC),evaluate(rightC))
	else:
		return trav.getRootVal()





def main():
	pt=Parsetree()
	pt.insert('((4+3)*(5-2))')
	printPrefix(pt.root)
	print()
	printPostFix(pt.root)
	print()
	#print(pt.root.left.right.val)
	evaluate(pt.root)

if __name__ == '__main__':
	main()