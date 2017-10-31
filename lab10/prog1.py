import sys


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.start=0
        self.end=0
        self.color='white'


class Graph:
    def __init__(self,v):
        self.adjList = [None] *v
        self.time=0

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
        u.start=self.time
        u.color='grey'
        # for i in range(len(self.adjList)):
        #     if self.adjList[i] != None:
        tr = self.adjList[u.val]
        while tr != None:
            print(tr.val, end=' ')
            tr = tr.next

        else:
            print(self.adjList[u.val])


def main():
    v=int(input('Enter the number of the vertices:'))
    g=Graph(v)
    x=int(input('Enter the number of edges: '))
    print('Enter the edges: ')
    for i in range(x):
        a,b=map(int,sys.stdin.readline().split())
        g.insertEdge(a,b)
    g.DFS(g.adjList[0])

if __name__ == '__main__':
    main()

