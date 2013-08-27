import sys
import random

def nnu_register(reg ,inst_no, t):
	j = 0	
	index = None
	for i in reg:
		while ( inst_no >= 0 ):
			while j<len(t[inst_no]) and t[inst_no][j][0]!=i:
				j=j+1
			if j<len(t[inst_no]) and t[inst_no][j][2] == None:
					return reg.index(i)
			inst_no = inst_no - 1


def is_address_descriptor(table , reg):
		
	present = False		
	for i in reg:
		
		if(table[i][0] != None and table[i][1] != None):
			table[i][1] = None
			present = True
			break
	return present


def address_descriptor(table , reg):
	
	for i in reg:
	
		free = -1	
		if(table[i][0] != None and table[i][1] != None):
			table[i][1] = None
			free = reg.index(i)
			break
	return free 



def get_operation(quad):
	
	if(quad[2] == '+'):
		return 'ADD'
	elif(quad[2] == '-'):
		return 'SUB'
	elif(quad[3] == '*'):
		return 'MUL'


def getRegFromV(var, lhs, reg, table):
	for var,value in table.items():
		if var!=lhs and value[0]!=None and value[1]!=None:
			return reg.index(var)
	else:
		return None
	

def getReg_rhs(var ,lhs_var, var1, inst_no , reg , table , t, out, tostr):
	if var in reg:
		op = reg.index(var)

	elif None in reg:
		op = reg.index(None)
		table[var][1] = op
		reg[op] = var
		if table[reg[op]][0] != None :
			print "LOAD "+str(var)+", R"+str(op)
			out.write("LOAD "+str(var)+", R"+str(op))

	else:
		op = getRegFromV(var, var1, reg, table)
		if op != None:
			#print "1  ", op
			v = reg[op]
			if reg[op] in tostr:
				print 'STR R'+str(op)+', '+str(reg[op])
				out.write('STR R'+str(op)+', '+str(reg[op]))
			table[v][1] = None
			reg[op] = var
			table[var][1] = op
			if table[reg[op]][0] != None :
				print "LOAD "+str(var)+", R"+str(op)
				out.write("LOAD "+str(var)+", R"+str(op))
			
		elif lhs_var in reg and lhs_var!=var and lhs_var!=var1:
			op = reg.index(lhs_var)
			#print "2  ", op
			table[lhs_var][1] = None
			table[var][1] = op
			if reg[op] in tostr:
				print 'STR R'+str(op)+', '+str(reg[op])
				out.write('STR R'+str(op)+', '+str(reg[op]))
			reg[op] = var
			# x = y + z
			if table[reg[op]][0] != None :
				print "LOAD "+str(var)+", R"+str(op)
				out.write("LOAD "+str(var)+", R"+str(op))
		else:	
			op=nnu_register(reg, inst_no, t)
			#print "3  ", op
			if (op != None ):
				table[reg[op]][1] = None
				table[var][1] = op
				if reg[op] in tostr:
					print 'STR R'+str(op)+', '+str(reg[op])
					out.write('STR R'+str(op)+', '+str(reg[op]))
					
				reg[op] = var
				if table[reg[op]][0] != None :
					print "LOAD "+str(var)+", R"+str(op)
					out.write("LOAD "+str(var)+", R"+str(op))
		
			else:
				#op = next_use_register ( reg, inst_no, t )
				op = random.randint ( 0, len(reg)-1 )
				#print "4  ", op
				table[reg[op]][1] = None
				if table[reg[op]][0] != None :
					print "STR R"+str(op)+", "+str(reg[op])
					out.write("STR R"+str(op)+", "+str(reg[op]))
					print "LOAD "+str(var)+", R"+str(op)
					out.write("LOAD "+str(var)+", R"+str(op))
				table[var][1] = op
				reg[op] = var
		
	return op


def hasNextUse(rhs, t, inst_no, reg):
	j = 0
	for key,value in t.items():
		if key == inst_no:
			while j<len(value) and value[j][0] != rhs:
				j = j+1

			if j<len(value) and (rhs in reg) and value[j][2]==None:
				return reg.index(rhs)
			else:
				return None


def getReg_lhs(var , rhs1, rhs2, inst_no , reg , table , t,out):	
	if var in reg:
		op = reg.index(var)
		#print "-1 ", op

	elif None in reg:
		op = reg.index(None)
		table[var][1] = op
		reg[op] = var
		#print "0 ", op
		#print "LOAD "+str(var)+", R"+str(op)
	
	else:
		op=hasNextUse(rhs1, t, inst_no, reg)

		if op == None:
			op=hasNextUse(rhs2, t, inst_no, reg)                 
			table[rhs2][1] = None
		else:
			table[rhs1][1] = None

		if op != None:# and table[reg[op]][0]==reg[op]:
			table[reg[op]][1] = None
                        table[var][1] = op
                        reg[op] = var
                        #print "LOAD "+str(var)+", R"+str(op)
		else:
			# Spill
			#op = next_use_register ( reg, inst_no, t )
                        op = random.randint ( 0, len(reg)-1 )
			table[reg[op]][1] = None
                        if table[reg[op]][0] != None:
                        	print "STR R"+str(op)+", "+str(reg[op])
				out.write("STR R"+str(op)+", "+str(reg[op]))
                                #print "LOAD "+str(var)+", R"+str(op)
                                table[var][1] = op
                                reg[op] = var

	return op


def getReg(I , inst_no , reg , table , t, out, tostr):
	if not str(I[1]).isdigit():
		first_rhs = getReg_rhs( I[1], I[0], I[3], inst_no , reg , table , t, out, tostr)
	else:
		first_rhs = "#"+str(I[1])

	if not str(I[3]).isdigit():
		second_rhs  = getReg_rhs( I[3], I[0], I[1], inst_no , reg , table , t , out, tostr)
	else:
		first_rhs = "#"+str(I[3])
	
	lhs = getReg_lhs( I[0], I[1], I[3] ,inst_no , reg , table , t,out )
	operator = I[2]

	if operator == '+':
		operator = 'ADD'
	elif operator == '-':
		operator = 'SUB'
	elif operator == '*':
		operator = 'MUL'
	elif operator == '/':
		operator = 'DIV'	

	print operator+" R"+str(lhs)+", R"+str(first_rhs)+", R"+str(second_rhs)
	out.write(operator+" R"+str(lhs)+", R"+str(first_rhs)+", R"+str(second_rhs))		

def get(quad , t,out, r, tostr):

	reg = []
	for i in range(0 , r):
		reg.append(None)


	f_original = open('symbol_original.txt' , 'r')
	f_temp = open('symbol_temp.txt' , 'r')

	lines_original = f_original.readlines()
	lines_temp     = f_temp.readlines()

	original_variables = []
	for i in lines_original:
		i = i.split('\n')
		original_variables.append(i[0])


	temp_variables = []
	for i in lines_temp:
		i = i.split('\n')
		temp_variables.append(i[0])

	table = dict({})

	o = []
	for i in original_variables:
		table[i] = [i , None]
		if i in tostr:
			o.append(i)


	
	for i in temp_variables:
		table[i] = [None , None]


	k = 0
	for i in quad:
		getReg(i , quad.index(i) , reg , table , t, out, tostr)
		k = k + 1

	for i in reg:
		if i in o:
			print 'STR R'+str(reg.index(i))+', '+str(i)
			out.write('STR R'+str(reg.index(i))+', '+str(i))

