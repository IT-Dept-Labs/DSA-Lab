a=[]
n=int(input("Enter n: "))
print("Enter elements: ")
for i in range(n):
	a.append(int(input("")))
for i in range (n-1):
	min_i=i
	for j in range(i+1,n):
		if a[i]>a[j]:
			min_i=j
			t=a[i]
			a[i]=a[min_i]
			a[min_i]=t
print("Sorted Array",a)