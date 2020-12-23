import functools
inp = list("476138259")
inp = [int(x) for x in inp]
#build the million cups...
latest = max(inp)
# while(latest <= 1000000):
#     latest+=1
#     inp.append(latest)
#     pass

def executeRound(currentInp,previous,ind):
    # currentInp = list(currentInp)
    if previous != None:
        currentPosition = currentInp.index(previous)+1
        currentPosition %= len(inp)
    else:
        currentPosition = ind % len(inp)

    currentCup = currentInp[currentPosition]
    pickUp = currentInp[currentPosition+1:currentPosition+4]
    if(len(pickUp) < 3):
        pickUp.extend(currentInp[0:3-len(pickUp)])
    destination = int(currentCup) - 1
    while(destination in pickUp or destination < 1):
        destination -=1
        if(destination < 1):
            destination = max(currentInp)

    for i in pickUp:
        currentInp.remove(i)
    destinationIndex = currentInp.index(destination)
    for i in pickUp:
        if(destinationIndex+1 >= len(inp)):
            destinationIndex = -1
        currentInp.insert(destinationIndex+1,i)
        destinationIndex+=1
    previous = currentCup

    return currentInp,previous

import copy
from tqdm import tqdm
currentInp = copy.deepcopy(inp)
previous = None
for ind,i in tqdm(enumerate(range(10000000))):
    currentInp,previous = executeRound(currentInp,previous,ind)

finalString = []
OneIndex = currentInp.index(1)
for i in currentInp[OneIndex+1:]:
    finalString.append(str(i))

for i in currentInp[:OneIndex]:
    finalString.append(str(i))

print(finalString[:2])