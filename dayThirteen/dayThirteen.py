with open("dayThirteen.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    midPoint = inp
    output = midPoint
    return output

import math

def partOne(inp):
    earliest = inp[0].strip()
    busIDs = inp[1].strip().split(",")
    nextTimes = []
    for bID in busIDs:
        if(bID != "x"):
            closest = math.ceil(int(earliest) / int(bID)) * int(bID)
            nextTimes.append((bID,closest))
    minTime = nextTimes[0][1]
    minID = nextTimes[0][0]
    for i in nextTimes:
        if(i[1] < minTime):
            minTime = i[1]
            minID = i[0]
            pass
    print((minTime - int(earliest)) * int(minID))

def partTwo(inp):
    busIDs = inp[1].strip().split(",")
    offsets = [(int(x),ind) for ind,x in enumerate(busIDs) if x != "x"]    

    met  = 1
    step = offsets[0][0]
    time = 0
    while met < len(offsets):
        time += step
        if (time + offsets[met][1]) % offsets[met][0] == 0:
            step = step * offsets[met][0]
            met += 1

    print(time)

partOne(preProcess(readIn))
partTwo(preProcess(readIn))