with open("sample.txt") as fi:
    readIn = fi.read()

def preProcess(inp):
    midPoint = inp
    output = midPoint.split(",")
    return output

def partOne(inp):
    numberStack = [int(x) for x in inp]
    it = 0

    while len(numberStack) < 2020:
        # print(numberStack)
        toLook = int(numberStack[-1])

        if(numberStack.count(toLook) == 1):
            numberStack.append(0)
        else:
            #find the most recent, and second most recent uses of the number in the stack, take the difference of their uses
            uses = []
            found = 0
            for ind,i in enumerate(numberStack[::-1]):
                if(i == toLook and len(uses) <= 2):
                    uses.append(ind+1)
            numberStack.append(abs(uses[0] - uses[1]))
        it += 1

    # print(len(numberStack))
    print(numberStack[-1])

from tqdm import tqdm
import collections

def returnList():
    return []

def partTwo(inp):
    numberStack = collections.defaultdict(returnList)
    for ind,x in enumerate(inp):
        numberStack[int(x)].append(int(ind))
    numberList = [int(x) for x in inp]

    for x in range(len(inp)-1,30000000):
        toLook = int(numberList[-1])
        if(len(numberStack[toLook]) == 1):
            numberList.append(0)
            numberStack[0].append(x+1)
        else:
            uses = [numberStack[toLook][-1],numberStack[toLook][-2]]
            numberStack[abs((uses[0]) - (uses[1]))].append(x+1)
            numberList.append(abs((uses[0]) - (uses[1])))
    print(numberList[-2])
    pass

partOne(preProcess(readIn))
print("\n")
partTwo(preProcess(readIn))