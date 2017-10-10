import math

class BinaryHeap:
	def __init__(self):
		self.A=[None] * 10

	def insert(self,x,t):
		self.A[t]=x
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

	def heapify(self,i):
		child1=self.A[2*i]
		child2=self.A[2*i+1]
		while child1!=None or child2!=None:
			value=max(child1,child2)
			if value==child1:
				t=self.A[i]
				self.A[i]=self.A[2*i]
				self.A[2*i]=t
				i=2*i
			else:
				t=self.A[i]
				self.A[i]=self.A[2*i+1]
				self.A[2*i+1]=t
				i=2*i+1





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

if __name__ == '__main__':
	main()