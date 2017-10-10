import math

class BinaryHeap:
	def __init__(self):
		self.A=[None]

	def insert(self,x,t):
		self.A.append(x)
		p=t
		while True:
			q=p//2
			if q==0:
				break
			if self.A[p]>self.A[q]:
				tem=self.A[p]
				self.A[p]=self.A[q]
				self.A[q]=tem
				#swap(self.A[p],self.A[q])
				p=q
				q=p//2
			else:
				break	


	def maximum(self):
		return self.A[1]

	def extractMax(self):
		var=self.A[1]
		self.A[1]=self.A[len(self.A)-1]
		ret=self.A.pop()
		heapify(self.A,1)
		return ret

	def buildHeap(self,V):
		#heapify(V,1)
		V.append(self.extractMax())

def heapify(A,i):
	child1=A[2*i]
	child2=A[2*i+1]
	while i<len(A)//2:
		value=max(child1,child2)
		if value>A[i]:
			if value==child1:
				t=A[i]
				A[i]=A[2*i]
				A[2*i]=t
				i=2*i
			else:
				t=A[i]
				A[i]=A[2*i+1]
				A[2*i+1]=t
				i=2*i+1
			c=len(A)
			if 2*i>=len(A):
				break
			else:
				child1=A[2*i]
				child2=A[2*i+1]




"""def swap(a,b):
	t=a
	a=b
	b=t"""




def main():
	heap=BinaryHeap()
	s=int(input("Enter the size:"))
	t=1
	for i in range(s):
		ele=int(input("Enter the element: "))
		heap.insert(ele,t)
		t+=1
	print(heap.A)

	B=[20,35,45,78,15,21]

	heap.buildHeap(B)
	#print(B[2])
	"""heapify(B,1)
	print(B)"""
	print(heap.maximum())

	heap.extractMax()

	print(heap.A)

if __name__ == '__main__':
	main()