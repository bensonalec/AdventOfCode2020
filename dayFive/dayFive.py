import math

with open("dayFive.txt","r") as fi:
    readIn = fi.readlines()

def processRow(indicators, rng):

    if(rng[0] != rng[1]):
        ind = indicators[0]
        if(ind == "F" or ind == "L"):
            midPoint = rng[0] + math.floor((rng[1] - rng[0]) / 2)
            return processRow(indicators[1:],(rng[0],midPoint))
        elif (ind == "B" or ind == "R"):
            midPoint = rng[0] + math.ceil((rng[1] - rng[0]) / 2)
            return processRow(indicators[1:],(midPoint,rng[1]))
    else:
        return rng[0]

foundList = ["O" for x in range(0,1023)]

maxSeatID = 0
for line in readIn:
    #first, let's get the row
    rowCode = line[0:7]
    rowValue = processRow(rowCode,(0,127))
    columnCode = line[7:]

    columnValue = processRow(columnCode,(0,7))
    seatID = (rowValue * 8) +  columnValue
    foundList[seatID] = "X"
    if seatID > maxSeatID:
        maxSeatID = seatID
    # print(rowCode)

print(maxSeatID)

for ind,x in enumerate(foundList):
    if(foundList[ind - 1] == "X" and foundList[ind + 1] == "X" and foundList[ind] == "O"):
        print(ind)
