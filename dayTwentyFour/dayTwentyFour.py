with open("input.txt") as fi:
    lines = fi.readlines()

from collections import defaultdict

import copy
currentCount = defaultdict(lambda: False)
for line in lines:
    init = [0,0,0]
    inpLine = copy.deepcopy(line.strip())
    directionsArray = []
    while(len(inpLine) != 0):
        toLook = inpLine[0:2]
        if(toLook in ["se","sw","nw","ne"]):
            directionsArray.append(toLook)
            inpLine = inpLine[2:]
        else:
            toLook = inpLine[0]
            directionsArray.append(toLook)
            inpLine = inpLine[1:]
    for d in directionsArray:
        if(d == "e"):
            init[0] += 1
            init[2] -= 1
        if(d == "se"):
            init[1] += 1
            init[2] -= 1
        if(d == "sw"):
            init[0] -= 1
            init[1] += 1
        if(d == "w"):
            init[0] -= 1
            init[2] += 1
        if(d == "nw"):
            init[1] -= 1
            init[2] += 1
        if(d == "ne"):
            init[0] += 1
            init[1] -= 1
    currentCount[tuple(init)] = not currentCount[tuple(init)]

values = currentCount.values()
count = 0
for i in values:
    if(i):
        count += 1

def countNeighbors(coord, currentCount):
    options = [[1,-1,0],[1,0,-1],[0,1,-1],[-1,1,0],[-1,0,1],[0,-1,1]]
    neighbors = 0
    for i in options:
        neighbors += currentCount[(coord[0]+i[0],coord[1]+i[1],coord[2]+i[2])]
    return neighbors
from tqdm import tqdm

for day in tqdm(range(100)):
    oldGrid = copy.deepcopy(currentCount)
    tileCount = {}
    for tile,value in currentCount.items():
        tileCount[tile] = countNeighbors(tile,oldGrid)

    for tile,value in oldGrid.items():
        #if our tile is black
        if(tile in tileCount.keys()):
            count = tileCount[tile]
        else:
            count = countNeighbors(tile,currentCount)
        if(value):
            #if it has > 2 black neighbors:
            if(count > 2 or count == 0):
                #flip to white
                oldGrid[tile] = False
        #if our tile is white
        else:
            #if it has exactly 2 black neighbors:
            if(count == 2):
                #flip to black
                oldGrid[tile] = True

    currentCount = oldGrid

    values = currentCount.values()
    values = [1 for x in values if x == True]
    count = sum(values)
    tqdm.write(f"{day+1},{count}")