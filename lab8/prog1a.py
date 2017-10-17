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
		for i in range(length):
			if trav.children[self.getIndex(key[i])]==None and trav.end==True:
				return False
			else:
				trav=trav.children[self.getIndex(key[i])]
		return True

		
	"""def printTrie(self):
		trav=self.root
		print(self.root.children[0].children)"""

def main():
	t=Trie()
	t.insert('abcd')
	t.insert('acd')
	#t.printTrie()
	print(t.search('abcd'))
	print(t.search('abc'))


if __name__ == '__main__':
			main()		