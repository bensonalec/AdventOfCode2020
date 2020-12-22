with open("dayTwentyTwo.txt") as fi:
    readIn = fi.read()

def preProcess(inp):
    midPoint = inp.split("\n\n")
    playerOne = midPoint[0].split(":\n")[1].split("\n")
    playerTwo = midPoint[1].split(":\n")[1].split("\n")
    pOne = [int(x) for x in playerOne]
    pTwo = [int(x) for x in playerTwo]
    return pOne,pTwo

def partOne(pOne,pTwo):
    # print(pOne,pTwo)
    count = 0
    while(len(pOne) > 0 and len(pTwo) > 0):
        # print(pOne,pTwo)
        valueOne = pOne.pop(0)
        valueTwo = pTwo.pop(0)
        if(valueOne > valueTwo):
            pOne.append(valueOne)
            pOne.append(valueTwo)
        elif(valueTwo > valueOne):
            
            pTwo.append(valueTwo)
            pTwo.append(valueOne)

        count+=1
    value = 0
    for ind,i in enumerate(pOne[::-1]):
        value += ((ind+1) * i)
    for ind,i in enumerate(pTwo[::-1]):
        value += ((ind+1) * i)
    print(value)



def recursiveCombat(pOne,pTwo):
    roundStore = {}
    winner = None
    while(len(pOne) > 0 and len(pTwo) > 0):
        handHash = tuple(pOne + [-1] + pTwo)
        if(handHash in roundStore):
            return 0
            break
        else:
            roundStore[handHash] = 1
        valueOne = pOne.pop(0)
        valueTwo = pTwo.pop(0)
        
        if(len(pOne) >= valueOne and len(pTwo) >= valueTwo):
            winner = recursiveCombat(pOne[:valueOne],pTwo[:valueTwo])
            if winner == 0:
                pOne.append(valueOne)
                pOne.append(valueTwo)
            else:
                pTwo.append(valueTwo)
                pTwo.append(valueOne)
        else:
            if(valueOne > valueTwo):
                pOne.append(valueOne)
                pOne.append(valueTwo)
            elif(valueTwo > valueOne):                
                pTwo.append(valueTwo)
                pTwo.append(valueOne)


    if(len(pOne)==0):
        return 1
    else:
        return 0

pOne,pTwo = preProcess(readIn)
winner = recursiveCombat(pOne,pTwo)

value = 0
if(winner == 0):
    for ind,i in enumerate(pOne[::-1]):
        value += ((ind+1) * i)
else:
    for ind,i in enumerate(pOne[::-1]):
        value += ((ind+1) * i)

    for ind,i in enumerate(pTwo[::-1]):
        value += ((ind+1) * i)
print(value)