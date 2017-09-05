class ListNode:
	def __init__(self, val=None, nxt=None):
		self.val=val
		self.nxt=nxt




class HashMap:
    arr=[None for i in range(30)]

    def componentSum(self, string):
        s = 0
        for i in range(len(string)):
            string.split()
            s+=ord(string[i])
        return s

    def compressionMap(self,string):
        res=self.componentSum(string)
        return res%30

    def insertKey(self,string):
        k=self.compressionMap(string)

        if self.arr[k]==None:
            n=ListNode()
            n.val=string
            self.arr[k]=n

        else:
            n1=ListNode()
            n1.val=string
            n1.nxt=self.arr[k]
            self.arr[k]=n1

    def search(self,key):
        res=self.compressionMap(key)
        if self.arr[res]==None:
            print('Not found')
            return
        elif self.arr[res].val==key:
            print('Found')
        elif self.arr[res].nxt!=None:
            node=self.arr[res].nxt
            while node!=None:
                if node.val==key:
                    print('Found')
                    break
                else:
                    node=node.nxt
            else:
                print('Not found')

    def keys(self):
        for i in range(len(self.arr)):
            if self.arr[i]!=None:
                print(self.arr[i].val)
                node = self.arr[i].nxt
                while node != None:
                    print(node.val)
                    node=node.nxt

def main():
    H=HashMap()
    print("Enter q to quit")
    i=input("Enter the value: ")
    while i!='q':
        H.insertKey(i)
        i=input('Enter the value: ')
    search=input('Enter the search element: ')
    H.search(search)
    H.keys()


if __name__ == '__main__':
    main()

