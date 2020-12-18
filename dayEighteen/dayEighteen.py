with open("sample.txt") as fi:
    readIn = fi.read()

def preProcess(inp):
    midPoint = inp.split("\n")
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

import copy
def prioritizeAddition(line):
    finalLine = copy.deepcopy(line)
    for ind,c in enumerate(line):
        if(c == "+"):
            newInd = 0

            finalLine.insert(ind-1,"(")
            finalLine.insert(ind+3,")")
    return finalLine

def solveParentheses(eq):
    if("(" not in eq):
        eq = prioritizeAddition(eq)
        print(eq)
        return solveEquation(eq)
    # else:
    #     valueStack = []
    #     operatorStack = ["+"]
    #     total = 0
    #     it = 0
    #     line = eq
    #     while(len(line) != 0):
    #         ch = line[0]
    #         # print(ch)

    #         if(ch == "+"):
    #             operatorStack.append("+")
    #             line.pop(0)

    #             pass
    #         elif(ch == "*"):
    #             operatorStack.append("*")

    #             line.pop(0)
    #             pass
    #         elif(ch == "("):
    #             # print("B",line,operatorStack)
    #             value, finalIndex, rest = solveParentheses(line[1:])
    #             # print(value)
    #             line = rest
    #             # print("A",line,operatorStack)
    #             op = operatorStack.pop()
    #             if(op == "+"):
    #                 total += value
    #             if(op == "*"):
    #                 total  *= value
    #             if(len(line) == 0):
    #                 break
    #             # line.pop(0)

    #         elif(ch == ")"):
    #             # print("Returned")
    #             return total,it,line[1:]
    #             pass
    #         else:
    #             op = operatorStack.pop()
    #             if(op == "+"):
    #                 total += int(ch)
    #             if(op == "*"):
    #                 total  *= int(ch)
    #             line.pop(0)
    #         it += 1
    # return total, None,None

    pass

def solveParentheses(eq):
    #for a parenthesis, find the nearest one after, pass it into the same function
    line = eq
    ind = 0
    while(")" in line):
        #find the nearest "(" before it
        ind += 1
        pass
    return solveEquation(eq)




def partTwo(inp):
    total = 0
    for line in inp:
        print(solveParentheses(list(line.strip().replace(" ",""))))
        # total += x[0]
        # print(x[0])
    print(total)
    pass

partOne(preProcess(readIn))
partTwo(preProcess(readIn))