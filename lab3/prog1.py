def evaluate(li):
	stack=[]
	for i in li:
		if i.isdigit():
			stack.append(i)
		else:
			op2=stack.pop()
			op1=stack.pop()
			stack.append(operate(op1,i,op2))
	print(stack[0])

def operate(o1,op,o2):
	if op=='+':
		return int(o1)+int(o2)
	elif op=='-':
		return int(o1)-int(o2)
	elif op=='*':
		return int(o1)*int(o2)
	else:
		return int(o1)//int(o2)


s=input("Enter a valid postfix expression: ")
evaluate(s)
