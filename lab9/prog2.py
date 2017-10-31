class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []
	
	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

class Node:
	def __init__ (self,l):
		self.label=l
		self.color=None
		self.dist=None
		self.pred=None

class Graph:
	def __init__ (self,n,m):
		self.vertexTotal=n
		self.edgeTotal=m
		self.adjMatrix=[[0 for i in range(self.vertexTotal)] for i in range(self.vertexTotal)]
		self.adjList=[[] for i in range(self.vertexTotal)]
		self.vertices=[Node(i) for i in range(self.vertexTotal)]
	
	def insert(self):
		print("Enter the edges: ")
		for i in range(self.edgeTotal):
			s=input()
			s=s.split(' ')
			n1=int(s[0])
			n2=int(s[1])
			self.adjMatrix[n1][n2] = 1
			self.adjMatrix[n2][n1] = 1
		for i in range(self.vertexTotal):
			for j in range(self.vertexTotal):
				if self.adjMatrix[i][j]== 1:
					self.adjList[i].append(j)
	
	def getadjMatrix(self):
		print("The adjacency matrix is:")
		for i in range(self.vertexTotal):
			for j in range(self.vertexTotal):
				print(self.adjMatrix[i][j],end=" ")
			print()

	def getadjList(self):
		print("The adjacency list is:")
		for i in range(self.vertexTotal):
			print("vertex "+str(i)+":",end=" ")
			for j in self.adjList[i]:
				print(j,end=",")
			print()
	def BFS(self,s):
		for i in range(self.vertexTotal):
			if i != s.label:
				self.vertices[i].dist=None
				self.vertices[i].color="white"
				self.vertices[i].pred=None
		s.dist=0
		s.color="grey"
		q=Queue()
		print("visited the vertex "+ str(s.label))
		print("Distance from the source vertex is "+str(s.dist))
		q.enqueue(s)
		while not q.isEmpty():
			u=q.dequeue()
			for i in self.adjList[u.label]:
				v=self.vertices[i]
				if v.color=="white":
					v.dist=u.dist + 1
					v.color="grey"
					v.pred=u
					print("visited the vertex "+ str(v.label))
					print("Distance from the source vertex is "+str(v.dist))
					q.enqueue(v)
			u.color="black"


def main():
	n=int(input("Enter the no of vertices: "))
	m=int(input("Enter the no of edges: "))
	g=Graph(n,m)
	g.insert()
	g.getadjList()
	g.getadjMatrix()
	si=int(input("Enter the source vertex for BFS:"))
	g.BFS(g.vertices[si])

if __name__ == '__main__':
	main()
