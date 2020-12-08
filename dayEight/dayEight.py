with open("dayEight.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    midPoint = inp
    output = midPoint
    return output

def partOne(inp):
    accumulator = 0
    visited = [0] * len(inp)

    lineNum = 0
    while(visited[lineNum] == 0):
        #set visited[lineNum] to 1
        visited[lineNum] = 1


        #execute the line
        line = inp[lineNum]
        #split into operation and value
        lineSpl = line.split(" ")
        operator = lineSpl[0]
        value = int(lineSpl[1])
        if(operator == "nop"):
            lineNum = lineNum + 1
        elif(operator == "acc"):
            accumulator += value
            lineNum += 1
        elif(operator == "jmp"):
            lineNum = lineNum + value

    print(accumulator)
    pass

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
        lineSpl = line.split(" ")
        operator = lineSpl[0]
        if(lineNum == corruptLine):
            if(operator == "nop"):
                operator = "jmp"
            elif(operator == "jmp"):
                operator = "nop"

        value = int(lineSpl[1])

        if(operator == "nop"):
            lineNum = lineNum + 1
        elif(operator == "acc"):
            accumulator += value
            lineNum += 1
        elif(operator == "jmp"):
            lineNum = lineNum + value
    if(lineNum >= len(inp)):
        print(accumulator)


def partTwo(inp):

    #need to find all possible permutations where a nop will become a jmp or a jmp will become a nop
    for ind,line in enumerate(inp):
        #find every instruction where a nop or jmp occurs
        lineSpl = line.split(" ")
        operator = lineSpl[0]
        value = int(lineSpl[1])


        if(operator == "nop" or operator == "jmp"):
            execute(inp,ind)
        #pass the lineNumber of this into some function that checks for a loop
        #if there's a loop, then try the next value
        pass

    #this code will detect a loop

    pass

partOne(preProcess(readIn))
partTwo(preProcess(readIn))