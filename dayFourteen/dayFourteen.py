with open("dayFourteen.txt") as fi:
    readIn = fi.readlines()

import functools
import copy

def preProcess(inp):
    midPoint = inp
    ind = 0
    rules = []
    while(ind < len(midPoint)-1):
        line = midPoint[ind].strip()
        # print(ind,line)
        if("mask" in line):
            mask = line.split(" = ")[1]
            addr = []
            for it,ln in enumerate(midPoint[ind+1:]):
                if("mask" in ln):
                    break
                spl = ln.strip().split(" = ")
                address = "{0:08b}".format(int(spl[0].split("[")[1].replace("]","")))
                value = "{0:08b}".format(int(spl[1]))
                # print(address,value)
                addr.append((address,value))
                ind += 1
            rules.append((mask,addr))
        ind += 1
    # print(rules)
    return rules

def partOne(inp):
    memStore = {}
    for ru in inp:
        mask = ru[0]
        stores = ru[1]
        for store in stores:
            addr = store[0]
            binRep = store[1]
            missingZeroes = 36 - len(binRep)
            missingZeroes = missingZeroes * "0"
            
            binRep = missingZeroes + binRep
            newBin = []
            for ind,i in enumerate(mask):
                if(i != "X"):
                    if(binRep[ind] != i):
                        newBin.append(i)
                    else:
                        newBin.append(i)  
                else:
                    newBin.append(binRep[ind])
            memStore[int(addr,2)] = int("".join(newBin),2)
    su = 0
    for i in memStore.keys():
        su += memStore[i]
    print(su)

@functools.lru_cache
def buildTTab(total,div):
    cycles = total // div
    finalList = []
    toWrite = "0"
    totalList = []
    for ind,i in enumerate(range(div)):
        ind %= div
        if(ind == div-1):
            finalList+= div * [toWrite]
            cycles -= 1
            if(toWrite == "0"):
                toWrite = "1"
            else:
                toWrite = "0"
    totalList.append(finalList)
    if(div == 1):
        return totalList
    else:
        totalList += buildTTab(total,div//2)
        return totalList

def partTwo(inp):
    memStore = {}
    for ru in inp:
        mask = ru[0]
        stores = ru[1]
        for store in stores:
            binRep = store[0]
            value = store[1]
            missingZeroes = 36 - len(binRep)
            missingZeroes = missingZeroes * "0"
            
            binRep = missingZeroes + binRep
            newBin = []
            toStore = []
            floatingIndexes = []
            for ind,i in enumerate(mask):
                if(i == "X"):
                    newBin.append("X")
                    floatingIndexes.append(ind)
                elif(i == "0"):
                    newBin.append(binRep[ind])
                elif(i == "1"):
                    newBin.append(i)
            numFloating = len(floatingIndexes)
            possibles = buildTTab(2 ** numFloating,(2 ** numFloating) // 2)
            for ind,i in enumerate(range(2 ** numFloating)):
                newOne = copy.deepcopy(newBin)
                for jInd,j in enumerate(floatingIndexes):
                    newOne[j] = possibles[jInd][ind]
                toStore.append(newOne)
            for x in toStore:
                memStore[int("".join(x),2)] = int(value,2)
    su = 0
    for i in memStore.keys():
        su += memStore[i]
    print(su)

partOne(preProcess(readIn))
partTwo(preProcess(readIn))