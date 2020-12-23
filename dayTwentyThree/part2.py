import functools
inp = list("476138259")
inp = [int(x) for x in inp]
#build the million cups...
latest = max(inp)
# print(latest)
while(latest < 1000000):
    latest+=1
    inp.append(latest)

currentDic = {}
for ind,i in enumerate(inp):
    if(ind+1 >= len(inp)):
        currentDic[i] = inp[0]
    else:
        currentDic[i] = inp[ind+1]

def executeRound(currentInp,previous,ind):
    currentCup = previous
    pickUp = []
    toPick = currentCup
    for i in range(3):
        pickUp.append(currentInp[toPick])
        toPick = currentInp[toPick]
    destination = currentCup -1
    while destination in pickUp or destination < 1:
        destination -= 1
        if(destination < 1):
            destination = max(currentInp.keys())
    currentInp[currentCup] = currentInp[pickUp[2]]
    for i in pickUp:
        del currentInp[i]
    gapStore = currentInp[destination]
    currentInp[destination] = pickUp[0]
    currentInp[pickUp[0]] = pickUp[1]
    currentInp[pickUp[1]] = pickUp[2]
    currentInp[pickUp[2]] = gapStore
    previous = currentInp[currentCup]
    return currentInp,previous

import copy
from tqdm import tqdm
currentInp = copy.deepcopy(inp)
previous = currentInp[0]
for ind,i in tqdm(enumerate(range(10000000))):
    currentDic,previous = executeRound(currentDic,previous,ind)

current = currentDic[1]
finalString = []
while(current != 1):
    finalString.append(int(current))
    current = currentDic[current]
import math
print(math.prod(finalString[:2]))