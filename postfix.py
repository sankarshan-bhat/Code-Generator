def push_stack(stackArr,ele):
    stackArr.append(ele)

def pop_stack(stackArr):
    return stackArr.pop()

def isOperand(who):
    if(not(isOperator(who)) and (who != "(") and (who != ")")):
        return 1
    return 0

def isOperator(who):
    if(who == "+" or who == "-" or who == "*" or who == "/" or who == "^" or who == "="):
        return 1
    return 0

def topStack(stackArr):
    return(stackArr[len(stackArr)-1])

def isEmpty(stackArr):
    if(len(stackArr) == 0):
        return 1
    return 0

def prcd(who):
    if(who == "^"):
	return(5)
    if((who == "*") or (who == "/")):
	return(4)
    if((who == "+") or (who == "-")):
	return(3)
    if(who == "("):
	return(2)
    if(who == ")"):
	return(1)

def ip(infixStr,postfixStr = [],retType = 0):
    postfixStr = []#final postfix expression
    stackArr = [] #stack
    #postfixPtr = 0
    #tempStr = infixStr#temporary string 
    #infixStr = []
    infixStr = list(infixStr)
    for x in infixStr:
	if(isOperand(x)):
            postfixStr.append(x+' ')
            #postfixPtr = postfixPtr+1
# temp var mul *+
        if(isOperator(x)):
        	while((not(isEmpty(stackArr))) and (prcd(x) <= prcd(topStack(stackArr)))):
                    postfixStr.append(topStack(stackArr))
                    pop_stack(stackArr)
                    #postfixPtr = postfixPtr+
       		push_stack(stackArr,x)

        elif(x == "("):
                push_stack(stackArr,x)                
        elif(x == ")"):
            while(topStack(stackArr) != "("):
                postfixStr.append(pop_stack(stackArr))
                #postfixPtr = postfixPtr+1
            pop_stack(stackArr)
            
    while(not(isEmpty(stackArr))):
        if(topStack(stackArr) == "("):
            pop_stack(stackArr)#may be raise exception
        else:
            postfixStr.append(pop_stack(stackArr))

    return(postfixStr)

def menu(infixExpr):
	#infixExpr = raw_input('\nEnter Infix String: ')
        postfixExpr=ip(infixExpr)
	print
	print(postfixExpr)
	print
	l=[]
    	for x in postfixExpr:
        	if(isOperand(x)):
        		l.append(x) 

    	f = open("symbol_original.txt", "w")
    	for i in l:
       		newline = i#.rstrip('\r\n')
        	f.write(newline)
        	f.write('\n')
	f.close()
	return postfixExpr			
          
#menu()
