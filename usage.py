import re

def computeLastUse(quad, i, j):
	flag = 1
	k = i
	
	if (j>0):
		flag = 0
		k = i
	elif j==0:
		while k>0 and flag==1:
			if (quad[i][j] == quad[k][0]):
				flag = 0
			k = k-1
	if flag==1:
		k=0

	return k

def computeNextUse(quad, i, j):
	flag = 1
	k = i+1
	while k<len(quad) and flag==1:
		l = 1
		while  l<len(quad[k]):
			if quad[k][l]==quad[i][j]:
				flag = 0
			l = l+1
		k = k+1

	if flag == 1:	
		ret = None
	else:
		ret = k
	
	return ret

def gen(quad):
	
	len(quad)
	t ={i: [] for i in range(0,len(quad)) }

	i=len(quad)-1

	while(i>=0):
		j = 0
		while (j<len(quad[i])):
			if ( j!=2 ):
				#print quad[i][j]
				if not str(quad[i][j]).isdigit():
					lu = computeLastUse(quad, i, j)
					nu = computeNextUse(quad, i, j)
					t[i].append([quad[i][j],lu, nu])
			j = j+1
		i = i-1
	
	
	return t
