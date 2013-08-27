import os
import eval
import usage
import InfixTopostfix
import postfix
import re
import table


def Main(out, read,Reg_no):
	f = open("symbol_temp.txt", "w")
	f.close()
        f = open("symbol_original.txt", "w")	
	f.close()
	tostr = []
	#f = open('input.txt', 'r')
	#read = f.readlines()
	k = 0
	for input_exp in read:
		#print '\n\n'+input_exp
		input_exp = str(input_exp)
		#print k
		k = eval.eval(input_exp, k, tostr)
	#input_exp = raw_input('Enter the Expression : ')
	#eval.eval(input_exp)
	
	f.close()
	d = []
	
	f1 = open('inout.txt' , 'r')
	
	lines = f1.readlines()
	f1.close()
	os.system('rm inout.txt')
	for i in lines:
		i = i.split('\n')
		d.append(i[0])

	quad = []

	j = 0
	for i in d:
		quad.append(re.findall('\w+|\+|-|\*', d[j]))
		j = j + 1

	t = usage.gen(quad)
	#print t

	f = 0
	#print t
#	print '\n\n\n'

#	for i , j in t.iteritems():
#		for k in j:
#			print k[0],'\t',
#			print 'lu'+str(k[1]),'\t',
#			if k[2] == None:
#				print 'nnu\t',
#			else:
#				print 'nu'+str(k[2])+'\t',
#			print
#		print
#	print

#	print quad	

	table.get(quad , t,out, Reg_no, tostr)
	os.system("rm symbol_temp.txt")
