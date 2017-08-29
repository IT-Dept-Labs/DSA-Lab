a=[]
n=int(input("Enter size of array: "))
print("Enter elements: ")
for i in range(n):
	a.append(int(input("")))
n=len(a)
for i in range(n-1):
	for j in range(i,n):
		if a[i]>a[j]:
			t=a[i]
			a[i]=a[j]
			a[j]=t
print("sorted Array:",a)
