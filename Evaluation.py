
import postfix
import re

def eval(expression):
	exp = postfix.conversion(expression)
	count=0
	for i in exp:
      	 	if(postfix.isOperator(i)):
		 	count=count+1
	temp = [] # lis of temporary variable 
	VarCount=0 # to count the variables, whether it is ready to be operated on (i.e, 2 vars )
	varstack=[] 
	k=0
	t=""
	post=[]
	temp_list=[]
	k=0
	for i in exp:
		if postfix.isOperator(i):
			x = varstack.pop()
			y = varstack.pop()
			t=y+i+x
			temp.append(t)
			temps = "t"+str(k)
			temp_list.append(temps)
			varstack.append(temps)
			k=k+1
			
		else:
			varstack.append(i)

	f = open("symbol_temp.txt", "w")
	print '\n'
	for i in temp_list:
    		newline=i.rstrip('\r\n')
     		f.write(newline)
        	f.write('\n')
    	f.close()
	i = 0
	t = []
	for l in temp:
		if i<count-1:
			t.append("t"+str(i)+"="+str(l))
		else:
			t.append(str(l))
		i=i+1
	
	f = open("inout.txt", "w")
	print '\n'
	for i in t:
		print i
		f.write(i)
		f.write('\n')
	print '\n'
	f.close()
