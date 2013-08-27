def perform_load1(var):
	print("load R0 , " + var)




def perform_load2(var):
	print("load R2 , " + var)





def perform_store1(var):
	print("store R0 , "+ var)





def perform_store2(var):
	print("store R0 , " + var)





def perform_oper(var):
	if(var == '+'):
		print("add R0 , R1 , R2")
	if(var == '-'):
		print("sub R0 , R1 , R2")


def perform_reset():
	print("mov r0 , #0")

def quadraples_to_assembly():
	n = input("enter the max no of registers to be used...") # input from key board
	f_quadraples = open('quadraples.txt' , 'r')

	inst = []
	
	inst_lines = f_quadraples.readlines() 


	for i in inst_lines:
		i = i.split("\n")               # append each line in quadraples.txt to list
		inst.append(i[0])		# i.e, add each instruction to a list

	
	for i in inst:
		i = (i.split(" "))		# splits each instructions in a list ---> list of lists

						# i[0] - > l_value
						# i[2] - > *
						# i[4] - > first operand
						# i[6] - > operator
						# i[8] - > second operand
					
# note : if it is just an assignment then only l value , * , r_value



	for i in inst:
		
		#if(i[4] in original):
		perform_load1(i[4])
		if(len(i) > 5):
			#if(i[6] in original):
			perform_load2(i[8])

			perform_oper(i[6])

		if(len(i) < 6):
			perform_store1(i[0])
	
		else:
			perform_store2(i[0])
		
		perform_reset()
		print("\n")
		

'''	for i in inst:
		print(len(i))
		for j in i:
			print(j, end = '') 
		print()




'''
		
if __name__ == "__main__":
	
	quadraples_to_assembly() ;

