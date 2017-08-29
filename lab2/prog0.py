class ListNode:
	def __init__(self, val=None, nxt=None):
		self.val=val
		self.nxt=nxt
class LinkedList:
	def __init__(self):
		self.head=ListNode()

	def insert(self,x,p):
		temp=ListNode()
		temp.val=x
		temp.nxt=p.nxt
		p.nxt=temp

	def delete(self,p):
		p.nxt=p.nxt.nxt

	def printNode(self):
		node=self.head.nxt
		while node!=None:
			#if node.val==None:
				#continue
			#else:
			print(node.val,end=' ')
			node=node.nxt
		print('')
#-------------------------------------------------------------
	def insertAtIndex(self,x,i):
		node=self.head
		while i>0:
			node=node.nxt
			i-=1
		self.insert(x,node)

#-------------------------------------------------------------

	def search(self,x):
		node=self.head
		while node.nxt!=None:
			if x == node.val:
				return node
			else:
				node=node.nxt
		else:
			return None

	def len(self):
		node=self.head
		c=0
		while node.nxt!=None:
			c+=1
			node=node.nxt
		return c

	def isEmpty(self):
		if self.head.nxt==None:
			return True
		else:
			return False

def main():
	L=LinkedList()
	print('Empty List Check:',L.isEmpty())
	L.insert(10,L.head)
	L.printNode()
	L.insert(15,L.head.nxt)
	L.printNode()
	L.insert(12,L.head.nxt)
	L.printNode()
	L.insert(2,L.head)
	L.printNode()
	L.delete(L.head)
	L.printNode()
	print('Size of L is ',L.len())
	L.insert(12,L.head.nxt)
	L.insert(18,L.head.nxt)
	L.insert(15,L.head.nxt)
	L.insertAtIndex(2,0)
	L.printNode()
	print("SearchNode:", L.search(15))
	print("SearchNode:", L.search(78))
	L.delete(L.head.nxt)
	L.printNode()
	print('Empty List Check:',L.isEmpty())


if __name__ == '__main__':
	main()