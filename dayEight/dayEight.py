with open("dayEight.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    commandList = []
    for lineNum, line in enumerate(inp):
        #split into operation and value
        lineSpl = line.split(" ")
        operator = lineSpl[0]
        value = int(lineSpl[1])
        commandList.append((operator,value))
    return commandList

def execute(inp, corruptLine):
    accumulator = 0
    visited = [0] * len(inp)
    lineNum = 0
    while(lineNum < len(inp) and visited[lineNum] == 0):
        #set visited[lineNum] to 1
        visited[lineNum] = 1
        #execute the line
        line = inp[lineNum]
        #split into operation and value
        operator = line[0]
        value = int(line[1])
        if(lineNum == corruptLine):
            if(operator == "nop"):
                operator = "jmp"
            elif(operator == "jmp"):
                operator = "nop"

        if(operator == "nop"):
            lineNum = lineNum + 1
        elif(operator == "acc"):
            accumulator += value
            lineNum += 1
        elif(operator == "jmp"):
            lineNum = lineNum + value
    
    if(lineNum >= len(inp)):
        return True,accumulator
    else:
        return False,accumulator

def partOne(commandList):
    print(execute(commandList,-1)[1])

def partTwo(inp):
    #need to find all possible permutations where a nop will become a jmp or a jmp will become a nop
    for ind,line in enumerate(inp):
        #find every instruction where a nop or jmp occurs
        operator = line[0]
        if(operator == "nop" or operator == "jmp"):
            #pass the lineNumber of this into some function that checks for a loop
            val, acc = execute(inp,ind)
            if(val == True):
                print(acc)
                break


partOne(preProcess(readIn))
partTwo(preProcess(readIn))