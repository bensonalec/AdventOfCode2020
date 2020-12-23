import itertools
from tqdm import tqdm
import functools

with open("dayNineteen.txt") as fi:
    lines = fi.read()
    lines = lines.replace('"',"")
    pass

linesSpl = lines.split("\n\n")
lines = linesSpl[0].split("\n")
toCheck = linesSpl[1]

#read each rule in 
rules = {}
for line in lines:
    lineSpl = line.strip().split(":")
    ruleName = lineSpl[0]
    if(len(lineSpl) == 1):
        components = []
    else:
        components = []
        for x in lineSpl[1].strip().split("|"):
            components.append(x.strip().split(" "))        
        rules[ruleName] = components

def findTerminalRule(character):
    returnList = []    
    for key,val in rules.items():
        for i in val:
            for j in i:
                if character in j:
                    returnList.append(key)
    return returnList

def findMatchingRule(characterList):
    returnList = []
    for key,nonTerm in rules.items():
        ruleList = nonTerm
        possibleValues = itertools.product(characterList[0],characterList[1])
        for pos in possibleValues:
            if(list(pos) in ruleList and key not in returnList):
                returnList.append(key)
    return returnList

count = 0
for inpString in tqdm(toCheck.split("\n")[:-1]):
    size = len(inpString)
    lowerRows = [list(list() for j in range(i+1)) for i in range(size)]
    lowerRows = lowerRows[::-1]

    for indi, i in enumerate(lowerRows):
        for indj, j in enumerate(i):
            if(indi != 0):
                topI = 0
                topJ = indj
                rightI = indi-1
                rightJ = indj+1
                while topI < indi and rightJ < size:
                    res = findMatchingRule([lowerRows[topI][topJ], lowerRows[rightI][rightJ]])
                    if(res != []):
                        lowerRows[indi][indj].extend(res)
                    topI = topI+1
                    topJ = topJ
                    rightI = rightI-1
                    rightJ = rightJ+1
            else:
                lowerRows[indi][indj] = findTerminalRule(inpString[indj])

    finalAnswer = lowerRows[-1][0]
    if(finalAnswer == ['0']):
        count+=1
    tqdm.write(f"{count}")