import sys
import queue


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.color=None
        self.dist=-255
        self.pred+None


class Graph:
    def __init__(self,v):
        self.adjList=[None]*v

    def insertEdge(self,a,b):
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

    def BFS(self,s):
        s.dist=0
        s.color='grey'


Q=queue()
Q.enqueue('h')
print(Q)



