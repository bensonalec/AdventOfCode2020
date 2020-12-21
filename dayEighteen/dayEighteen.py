with open("dayEighteen.txt") as fi:
    readIn = fi.read()

def preProcess(inp):
    midPoint = inp.split("\n")[:-1]
    output = midPoint
    return output

def solveEquation(eq):
    #first, evaluate anything in parentheses
    # print(eq)
    valueStack = []
    operatorStack = ["+"]
    total = 0
    it = 0
    line = eq
    while(len(line) != 0):
        ch = line[0]
        # print(ch)

        if(ch == "+"):
            operatorStack.append("+")
            line.pop(0)

            pass
        elif(ch == "*"):
            operatorStack.append("*")

            line.pop(0)
            pass
        elif(ch == "("):
            # print("B",line,operatorStack)
            value, finalIndex, rest = solveEquation(line[1:])
            # print(value)
            line = rest
            # print("A",line,operatorStack)
            op = operatorStack.pop()
            if(op == "+"):
                total += value
            if(op == "*"):
                total  *= value
            if(len(line) == 0):
                break
            # line.pop(0)

        elif(ch == ")"):
            # print("Returned")
            return total,it,line[1:]
            pass
        else:
            op = operatorStack.pop()
            if(op == "+"):
                total += int(ch)
            if(op == "*"):
                total  *= int(ch)
            line.pop(0)
        it += 1
    # print("Returned")
    return total, None,None

def partOne(inp):
    total = 0
    for line in inp:
        x,y,z = solveEquation(list(line.strip().replace(" ","")))
        total += x
    print(total)
        # print(x)


def prec(operator):
    if(operator == "+"):
        return 1
    else:
        return 0

def shunt(eq):
    tokenStack = list(eq)
    outputQueue = []
    operatorStack = []
    # while there are tokens to be read:
    while(len(tokenStack) != 0):
        #     read a token.
        token = tokenStack.pop(0)
        isInt = False
        try:
            #if the token is a number, then:
            #push it to the output queue.
            outputQueue.append(int(token))
            isInt = True
        except:
            pass
        #else if the token is an operator then:
        if(token in ["+","*"]):
            #while ((there is an operator at the top of the operator stack)
            #and ((the operator at the top of the operator stack has greater precedence)
            #or (the operator at the top of the operator stack has equal precedence and the token is left associative))
            #and (the operator at the top of the operator stack is not a left parenthesis)):
            while((len(operatorStack) > 0) and (operatorStack[-1] != "(") and (prec(operatorStack[-1]) > prec(token) or prec(operatorStack[-1] == prec(token)))):
                #pop operators from the operator stack onto the output queue.
                outputQueue.append(operatorStack.pop())
            #push it onto the operator stack.
            operatorStack.append(token)
        #else if the token is a left parenthesis (i.e. "("), then:
        if(token == "("):
            #push it onto the operator stack.
            operatorStack.append(token)
        #else if the token is a right parenthesis (i.e. ")"), then:
        if(token == ")"):
            #while the operator at the top of the operator stack is not a left parenthesis:
            while(operatorStack[-1] != "("):
                #pop the operator from the operator stack onto the output queue.
                outputQueue.append(operatorStack.pop())
            #if there is a left parenthesis at the top of the operator stack, then:
            if(operatorStack[-1] == "("):
                #pop the operator from the operator stack and discard it
                operatorStack.pop()
    #while there are still operator tokens on the stack:
    for i in operatorStack[::-1]:
        #pop the operator from the operator stack onto the output queue.
        outputQueue.append(i)
    return outputQueue


def evaluateRPN(eq):
    tmpStack = []
    for token in eq:
        try:
            tmpStack.append(int(token))
        except:
            a = tmpStack.pop()
            b = tmpStack.pop()
            if(token == "+"):
                tmpStack.append(a+b)
                pass
            elif(token == "*"):
                tmpStack.append(a*b)
    return tmpStack[0]


def partTwo(inp):
    total = 0
    for line in inp:
        x = evaluateRPN(shunt(list(line.strip().replace(" ",""))))
        total += x
    print(total)
    pass

partOne(preProcess(readIn))
partTwo(preProcess(readIn))