import InfixTopostfix
#import postfix
import re

def eval(expression, k, tostr):
	exp = InfixTopostfix.menu(expression)
	#exp = postfix.menu(expression)
	#print exp
	count=0
	for i in exp:
		#print(i)
		if(InfixTopostfix.isOperator(i)):
      	 	#if(postfix.isOperator(i)):
		 	count=count+1
	temp = [] # temporary variable -> contains 
	VarCount=0 # to count the variables, whether it is ready to be operated on (i.e, 2 vars )
	opstack=[] # stack for operator
	varstack=[] # stack for operand
	t=""
	exp = str(exp)
	post = re.findall('\w+|\+|-|\*|/|=', exp)
	#print post
        l=[]
        for x in post:
                if(InfixTopostfix.isOperand(x)):
                        l.append(x)

	f = open("symbol_original.txt", "a")
        for i in l:
		if not i.isdigit():
                	f.write(i)
                	f.write('\n')
        f.close()

	store_i = k
	temp_list=[]
	temps = ''
	#print post
	t = []
	for i in post:
		if InfixTopostfix.isOperator(i):
			if i!='=':
				#if postfix.isOperator(i):
				x = varstack.pop()
				y = varstack.pop()
				t1=y+i+x
				temp.append(t1)
				temps = "t"+str(k)
				#print i+"harekal"+temps
				temp_list.append(temps)
				varstack.append(temps)
				k=k+1
			elif count==1:
				x = varstack.pop()
				y = varstack.pop()
				print var , '*'*80
				tostr.append(var)
				t.append(str(x)+"="+str(y))
		else:
			varstack.append(i)
	f = open("symbol_temp.txt", "a")
	inv = 0
        for i in temp_list:
     		if inv<len(temp_list)-1:
			f.write(i)
        		f.write('\n')
		inv = inv + 1

    	f.close()

	i = store_i
	#print temp, i, 'hellohello'
	for l in temp:
		if i<store_i+count-2:
			t.append("t"+str(i)+"="+str(l))
		else:
			#print varstack
			var = varstack.pop()
			var = varstack.pop()
			#print var
			print var , '*'*80
			tostr.append(var)
			t.append(str(var)+"="+str(l))
		i=i+1

	f = open("inout.txt", "a")
	for i in t:
		print i
		f.write(i)
		f.write('\n')
	f.close()
	
	if k==0:
		return 0
	return k-1
