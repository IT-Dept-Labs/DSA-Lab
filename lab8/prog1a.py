class TrieNode:
	def __init__(self):
		self.children=[None] * 26
		self.end = False




class Trie:
	def __init__(self):
		self.root = TrieNode()

	def getIndex(self,ch):
		return ord(ch)-ord('a')

	def insert(self,key):
		travNode=self.root
		keyLen=len(key)
		for i in range(keyLen):
			index=self.getIndex(key[i])
			if not travNode.children[index]:
				travNode.children[index]=TrieNode()
			travNode=travNode.children[index]
		travNode.end=True
			

	def search(self,key):
		length=len(key)
		trav=self.root
		flag=False
		for i in range(length):
			if trav.children[self.getIndex(key[i])]!=None and trav.end==False:
				trav=trav.children[self.getIndex(key[i])]
			if trav.end==True:
				flag=True

		if not flag:
				return False

		return True

		
	"""def printTrie(self):
		trav=self.root
		print(self.root.children[0].children)"""

def main():
	t=Trie()
	t.insert('action')
	t.insert('apple')
	t.insert('hello')
	print(t.search('hello'))
	print(t.search('act'))
	



	# print("Press 0 to quit")
	# x=input("Enter the word: ")
	# while x!='0':
	# 	x=input("Enter the word: ")
	# 	t.insert(x)


if __name__ == '__main__':
			main()		