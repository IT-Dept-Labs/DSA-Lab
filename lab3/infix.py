def convert(s):
	post=[]
	c=0
	v=None
	for i in s:
		if i.isdigit():
			post.append(i)
			c+=1
			if not s[c+1].isdigit():
				post.append(v) 
		else:
			v=i
		
	print(post)
convert('2+3-5+4*7+8')