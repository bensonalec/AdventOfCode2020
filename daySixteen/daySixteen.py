with open("sample.txt") as fi:
    readIn = fi.read()

def preProcess(inp):
    midPoint = inp.split("\n\n")
    rules = midPoint[0].split("\n")
    newRules = []
    ruleNames = []
    for ru in rules:
        spl = ru.split(": ")
        name = spl[0]
        subRules = spl[1].split(" or ")
        ruleList = []
        for su in subRules:
            suSpl = su.split("-")
            ruleList.append((int(suSpl[0]),int(suSpl[1])))
        newRules.append(ruleList)
        ruleNames.append(name)
    yours = midPoint[1].split("\n")[1]
    yours = [int(x) for x in yours.split(",")]
    nearby = midPoint[2].split(":\n")[1].split("\n")
    neList = []
    for ne in nearby:
        temp = []
        for x in ne.split(","):
            if(x != ""):
                temp.append(int(x))
        neList.append(temp)
    return newRules,yours,neList,ruleNames

def partOne(newRules,your,neList,ruleNames):
    invalidValues = []
    for tick in neList:
        for value in tick:
            valid = 0
            for ru in newRules:
                ruleSetOne = ru[0]
                ruleSetTwo = ru[1]
                for rs in ru:
                    if(rs[0] <= value <= rs[1]):
                        valid+=1
            if(valid == 0):
                invalidValues.append(value)
    print(sum(invalidValues))

def removeInvalidTickets(newRules,your,neList):
    validTickets = []
    for tick in neList:
        if(tick != []):
            valid = True
            for value in tick:
                validCount = 0
                for ru in newRules:
                    ruleSetOne = ru[0]
                    ruleSetTwo = ru[1]
                    for rs in ru:
                        if(rs[0] <= value <= rs[1]):
                            validCount+=1
                if(validCount == 0):
                    valid = False
            if(valid == True):
                validTickets.append(tick)
    return validTickets

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

def partTwo(newRules,your,neList,ruleNames):
    neList = removeInvalidTickets(newRules,your,neList)
    rulesDic = {}
    for ru in ruleNames:
        rulesDic[ru] = []
    for index in range(len(ruleNames)):
        for tick in neList:
            row = tick[index]
            for ryind,ru in enumerate(newRules):
                valid = False
                for rs in ru:
                    if(rs[0] <= row <= rs[1]):
                        valid = True
                if(valid == False and index not in rulesDic[ruleNames[ryind]]):
                    rulesDic[ruleNames[ryind]].append(index)
    sorte = dict(sorted(rulesDic.items(), key=lambda item: len(item[1]),reverse=True))
    found = []
    order = []
    for key,value in sorte.items():
        for val in Diff(value,list(range(0,20))):
            if(val not in found):
                found.append(val)
                order.append((val,key))
                break
    final = sorted(order, key=lambda item: item[0])
    finalValue = 1
    for i in final:
        if("departure" in i[1]):
            finalValue *= int(your[i[0]])
    print(finalValue)

partOne(*preProcess(readIn))
partTwo(*preProcess(readIn))