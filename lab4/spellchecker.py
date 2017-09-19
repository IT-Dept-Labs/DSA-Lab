class Hashtable:

	def __init__(self):
		self.T=[None for i in range(30)]

	def insertk(self,k):
		key=0
		for i in range(len(k)-1,0,-1):
			key=(key+ord(k[i:i+1]))*33
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




		if self.T[key]==None:

			return ("False")
		else:
			tmp=self.T[key]
			while tmp.next!=None:
				if tmp.value==k:
					return("Valid")

				tmp=tmp.next
			if tmp.value==k:
				return("Valid")
			else:
				return("Invalid")


	def keys(self):
		for i in range(0,30):
			if self.T[i]!=None:
				c=0
				tmp=self.T[i]


				while(tmp.next!=None):
					c=c+1
					tmp=tmp.next
				tmp=self.T[i]
				for j in range(0,c+1):
					print(tmp.value)
					tmp=tmp.next




class ListNode:
    def __init__(self):
        self.value=0
        self.next=None

def main():
	H=Hashtable()
	f=open("small.dict","r")
	con=f.readlines()
	con=[x.strip() for x in con]
	for i in range(len(con)):
                H.insertk(con[i])
	word=input("Enter a String: ")
	f1=open("ispell.dict","r")
	inp=f1.readlines()
	inp=[x.strip() for x in inp]
	for i in inp:
		print(H.search(i.lower()))
	
if __name__ == '__main__':
	main()

