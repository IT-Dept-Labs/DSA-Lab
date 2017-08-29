def fib(n):
	if n<0:
		print("Invalid input")
	else:
		a=[]
		a.append(0)
		a.append(1)
		a.append(1)
		
		for i in range(0,n):
			if i==0:
				print(a[0],end=' ')
			elif i==1:
				print(a[1],end=' ')
			elif i==2:
				print(a[2],end=' ')
			else:
				a.append(a[i-1]+a[i-2])
				print(a[i],end=' ')
				
def fib1(n):
	if n==0:
		return 0
	elif n==1:
		fib1(0)
		return 1
	else:
		return fib1(n-1)+fib1(n-2)


n=int(input("Enter a positive number: "))
fib(n)
print('\n')
for i in range(0,n):
	print(fib1(i),end=' ')

