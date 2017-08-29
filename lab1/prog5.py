str1=input("Enter str1: ")
str2=input("Enter str2: ")
str3=input("Enter str3: ")
for i in str1:
	while str1[i]!=' ':
		j=0
		str4[j]=str1[i]
		j+=1
	for k in str4:
		if str4[k]==str2[k]:
			str1[i]=str4[k]



#str1=str1.replace(str2,str3)
print ('Result:',str1)