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
		self.heapify(1)
		return var


	def heapify(self,i):
		while i<len(self.A)//2:
			child1=self.A[2*i]
			child2=self.A[2*i+1]
			value=max(child1,child2)
			if value>self.A[i]:
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
				c=len(self.A)
				if 2*i>=len(self.A):
					break
				else:
					child1=self.A[2*i]
					child2=self.A[2*i+1]

def main():
	h=BinaryHeap()
	t=1
	arr=[25,2,23,13,34,12]
	for i in arr:
		h.insert(i,t)
		t+=1
	for i in range(len(arr)-1,-1,-1):
		arr[i]=h.extractMax()
	print("Result: ",end='')
	print(arr)

if __name__ == '__main__':
	main()