def fact(n):
	s=1
	if n<0:
		print('Invalid Input')
		exit()
	if  n==1 or n==0:
		return s
	else:
		for i in range(1,n+1):
			s=s*i
		return s
def fact1(n):
    if n<0:
        return -1
    elif n==1 or n==0:
        return 1
    else:
        return n*fact1(n-1)


n=int(input("Enter a number: "))
print("Factorial of",n,"=",fact(n))
print("Factorial of",n," by recursion =",fact1(n))
 