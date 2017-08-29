def isPrime(n):
	if n==1:
		return
	for i in range(1,int(n/2-1)):
		if n%i==0:
			return False
	else:
		return True
n=int(input("Enter a number: "))
print('Check Prime:',isPrime(n))