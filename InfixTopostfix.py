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
    postfixStr = []
    stackArr = []
    postfixPtr = 0
    tempStr = infixStr
    infixStr = []
    infixStr = strToTokens(tempStr)
    for x in infixStr:
	if(isOperand(x)):
            postfixStr.append(x+" ")
            postfixPtr = postfixPtr+1
# temp var mul *+
        if(isOperator(x)):
            if(x != "^"):
                while((not(isEmpty(stackArr))) and (prcd(x) <= prcd(topStack(stackArr)))):
                    postfixStr.append(topStack(stackArr))
                    pop_stack(stackArr)
                    postfixPtr = postfixPtr+1
            else:
                while((not(isEmpty(stackArr))) and (prcd(x) < prcd(topStack(stackArr)))):
                    postfixStr.append(topStack(stackArr))
                    pop_stack(stackArr)
                    postfixPtr = postfixPtr+1
            push_stack(stackArr,x)
        if(x == "("):
                push_stack(stackArr,x)                
        if(x == ")"):
            while(topStack(stackArr) != "("):
                postfixStr.append(pop_stack(stackArr))
                postfixPtr = postfixPtr+1
            pop_stack(stackArr)
            
    while(not(isEmpty(stackArr))):
        if(topStack(stackArr) == "("):
            pop_stack(stackArr)
        else:
            postfixStr.append(pop_stack(stackArr))

    returnVal = ''
    for x in postfixStr:
        returnVal += x
    
        

    if(retType == 0):
        return(returnVal)
    else:
	return(postfixStr)



def strToTokens(str):
    strArr = []
    strArr = str
    tempStr = ''	
    tokens = []
    tokens_index = 0
    count = 0
    for x in strArr:
        count = count+1
        if(isOperand(x)):
            tempStr += x
        if(isOperator(x) or x == ")" or x == "("):
            if(tempStr != ""):
                tokens.append(tempStr)
                tokens_index = tokens_index+1
            tempStr = ''
            tokens.append(x)
            tokens_index = tokens_index+1 
        if(count == len(strArr)):
            if(tempStr != ''):
                tokens.append(tempStr)
    return(tokens)



def menu(what):
	#what = raw_input('\nEnter Infix String: ')
        list=[]
        list=ip(what)
	count=0
	l = []
	k = ""
	flag = 1
	for j in list:
		if ( isOperator(j) and flag == 1):
			j = " "+j+" "
			flag = 0
		else:
			k=k+j

		if flag==0:
			l.append(k)
			l.append(j)
			flag = 1
	return list        

#menu()
