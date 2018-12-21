# -*- coding: utf-8 -*- 
L = ['A','B','C','D']

print("小偷是:",end=" ")
for s in L:
	i = s  
	a=(i != 'A')
	b=(i == 'D')
	c=(i == 'B')
	d=(i != 'D')
	if (a + b + c + d == 1):
		L1 = [a,b,c,d]
		print(i)
		for i in range(len(L1)):
			if L1[i]:
				print("说真话的是：",end="")
				print(L[i])
