import sys


class Node:
	def __init__(self,val):
		self.val=val
		self.next=None
		self.start=0
		self.end=0
		self.color='white'
		self.pred=None


class Graph:
	def __init__(self,v):
		self.adjList = [None] *v
		self.time=0
		self.visited=[False] *v
		

	def insertEdge(self, a, b):
		n1 = Node(b)
		n2 = Node(a)
		if self.adjList[a] is None:
			self.adjList[a] = n1
		else:
			n1.next = self.adjList[a]
			self.adjList[a] = n1

		if self.adjList[b] == None:
			self.adjList[b] = n2
		else:
			n2.next = self.adjList[b]
			self.adjList[b] = n2

	def DFS(self,u):
		self.time+=1
		print('------',self.adjList[u].val,self.adjList[u].next.val)
		self.adjList[u].next.start=self.time+1
		self.adjList[u].next.color='grey'
		self.visited[u]=True
		# for i in range(len(self.adjList)):
		#     if self.adjList[i] != None:
		tr = self.adjList[u].next
		while tr != None:
			if tr.color=='white' or self.visited[tr.val]==False:
				self.DFS(tr.val)
				self.pred=u
			tr = tr.next
		self.adjList[u].color='black'
		self.time+=1
		self.adjList[u].end=self.time+1
		


def main():
	v=int(input('Enter the number of the vertices:'))
	g=Graph(v)
	x=int(input('Enter the number of edges: '))
	print('Enter the edges: ')
	for i in range(x):
		a,b=map(int,sys.stdin.readline().split())
		g.insertEdge(a,b)
	g.DFS(0)
	for i in range(v):
		print('vertex',i,g.adjList[i].start,g.adjList[i].end)

if __name__ == '__main__':
	main()

