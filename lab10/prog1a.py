class Vertex:


	def __init__(self):
		self.stime=None
		self.etime=None
		self.colour="U"
		self.pred=None
		self.next=None

class Node:

	def __init__(self,k):
		self.val=k
		self.next=None

L=[]



def main():
	n=int(input("Enter number of vertices:"))
	for i in range(n):
		L.append(Vertex())
	#M=[[0 for i in range(0,n)]for j in range(0,n)]
	e=int(input("Enter number of edges:"))
	print("Enter the edges:")
	for i in range(0,e):
		v1,v2=input().split()
		v1,v2=int(v1),int(v2)
		
		N1=Node(v1)

		N2=Node(v2)
		if L[v1].next==None:
			L[v1].next=N2
		else:
			tmp=L[v1].next
			N2.next=tmp
			L[v1].next=N2
			
		if L[v2].next==None:
			L[v2].next=N1
		else:
			tmp=L[v2].next
			N1.next=tmp
			L[v2].next=N1
	s=int(input("Enter the source vertex:"))
	DFS(s)
	for i in range(n):
		print("Vertex:",i,"Time:[",L[i].stime,",",L[i].etime,"]")

time=0

def DFS(u):
	global time
	time=time+1
	#print(time)
	L[u].stime=time
	L[u].colour="V"
	tmp=L[u].next
	while tmp!=None:
		if L[tmp.val].colour=="U":
			DFS(tmp.val)
			L[tmp.val].pred=u
		tmp=tmp.next
	L[u].colour="E"
	time=time+1
	#print(time)
	L[u].etime=time
	#L[u].etime=time++


if __name__ == '__main__':
	main()


