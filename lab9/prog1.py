import sys
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


class Graph:
    def __init__(self,v):
        self.adjMatrix=[[0 for i in range(v)] for j in range(v)]
        self.adjList=[None]*v

    def insertEdge(self,a,b):
        self.adjMatrix[a][b]=1
        self.adjMatrix[b][a]=1


        n1=Node(b)
        n2=Node(a)
        if self.adjList[a] is None:
            self.adjList[a] = n1
        else:
            n1.next = self.adjList[a]
            self.adjList[a] = n1


        if self.adjList[b]==None:
             self.adjList[b]=n2
        else:
            n2.next=self.adjList[b]
            self.adjList[b]=n2




def main():
    v=int(input("Enter the number of vertices: "))
    g=Graph(v)
    print("Enter the edges\nEnter . . to quit")
    while True:
        a,b = map(str,sys.stdin.readline().split())
        if a=='.':
            break
        a=int(a)
        b=int(b)
        if a<v and b<v:
            g.insertEdge(a,b)
        else:
            print("Invalid endpoints. Please try Again")
    print('Adjacency Matrix is')
    for i in range(v):
        print(g.adjMatrix[i])

    print('Adjacency List:')
    for i in range(len(g.adjList)):
        print('Vertex',i,':',end='')
        if g.adjList[i]!=None:
            tr=g.adjList[i]
            while tr!=None:
                print(tr.val,end=' ')
                tr=tr.next
            print()
        else:
            print(g.adjList[i])


if __name__ == '__main__':
			main()