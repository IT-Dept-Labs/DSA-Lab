class Hashtable:

	def __init__(self):
		self.T=[None for i in range(30)]

	def insertk(self,k):
		key=0
		for i in range(len(k)-1,0,-1):
			key=key+ord(k[i:i+1])*33
		key=key+ord(k[0])
		key=key%30
		
		tmp=ListNode()
		tmp.value=k
		
		if self.T[key]==None:
			self.T[key]=tmp
		else:
			tmp.next=self.T[key]
			self.T[key]=tmp
			


	def search(self,k):
		key=0
		for i in range(len(k)-1,0,-1):
			key=key+ord(k[i:i+1])*33
		key=key+ord(k[0])
		key=key%30
		
		tmp=self.T[key]
		while tmp.next!=None:
			if tmp.value==k:
					print(tmp.value)
				
			tmp=tmp.next
		if tmp.value==k:
				print(tmp.value)
			



class ListNode:
    def __init__(self):
        self.value=0
        self.next=None

def main():
	H=Hashtable()
	f=open("ispell.dict","r")
	con=f.readlines()
	con=[x.strip() for x in con]
	
	for i in range(0,len(con)):
		H.insertk(con[i])
	st1=input("Enter a word")
	for i in range(0,len(st1)):
		for j in range(97,123):
			if st1[i]!=chr(j):
				s=st1[:i]+str(chr(j))+st1[i+1:]
				H.search(s)

	












if __name__ == '__main__':
	main()

