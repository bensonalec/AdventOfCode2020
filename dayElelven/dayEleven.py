import copy

with open("dayEleven.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    midPoint = inp
    output = midPoint
    return output

def checkSeatsPartOne(grid,x,y):
    count = 0
    pairs = [(x-1,y),(x-1,y-1),(x-1,y+1),(x+1,y),(x+1,y-1),(x+1,y+1),(x,y+1),(x,y-1)]
    for pair in pairs:
        xVal = pair[0]
        yVal = pair[1]
        try:
            if(xVal >= 0 and yVal >= 0 and  grid[xVal][yVal] == "#"):                
                count += 1                
        except:
            pass
    return count

def checkSeatsPartTwo(grid,x,y):
    directionBlocked = 0
    validDirections = [(x-1,y),(x-1,y-1),(x-1,y+1),(x+1,y),(x+1,y-1),(x+1,y+1),(x,y+1),(x,y-1)]
    for ind, direct in enumerate(validDirections):
        currentX = x
        currentY = y
        xVal = currentX
        yVal = currentX

        while(True):
            pairs = [(currentX-1,currentY),(currentX-1,currentY-1),(currentX-1,currentY+1),(currentX+1,currentY),(currentX+1,currentY-1),(currentX+1,currentY+1),(currentX,currentY+1),(currentX,currentY-1)]
            xVal = pairs[ind][0]
            yVal = pairs[ind][1]            
            try:
                if(xVal >= 0 and yVal >= 0):
                    if(grid[xVal][yVal] == "#"):
                        directionBlocked += 1
                        break
                    elif(grid[xVal][yVal] == "L"):
                        break
                else:
                    break
            except:
                break
            currentX = xVal
            currentY = yVal
    return directionBlocked

def partOne(inp):
    inp = [x.strip() for x in inp]
    inp = [list(x) for x in inp]
    it = 0
    prevGrid = inp
    nextGrid = prevGrid
    while(prevGrid != nextGrid or it == 0):
        prevGrid = nextGrid
        nextGrid = copy.deepcopy(prevGrid)
        for indRow, row in enumerate(prevGrid):
            for seatRow,seat in enumerate(row):
                count = checkSeatsPartOne(prevGrid,indRow,seatRow)
                if(seat == "L" and count == 0):
                    nextGrid[indRow][seatRow] = "#"
                elif(seat == "#" and count >= 4):
                    nextGrid[indRow][seatRow] = "L" 
        it += 1
    totalString = "".join([str(x) for x in nextGrid])
    print(totalString.count("#"))

def partTwo(inp):
    inp = [x.strip() for x in inp]
    inp = [list(x) for x in inp]
    it = 0
    prevGrid = inp
    nextGrid = prevGrid
    while(prevGrid != nextGrid or it == 0):
        prevGrid = nextGrid
        nextGrid = copy.deepcopy(prevGrid)
        for indRow, row in enumerate(prevGrid):
            for seatRow,seat in enumerate(row):
                count = checkSeatsPartTwo(prevGrid,indRow,seatRow)
                if(seat == "L" and count == 0):
                    nextGrid[indRow][seatRow] = "#"
                elif(seat == "#" and count >= 5):
                    nextGrid[indRow][seatRow] = "L" 
        it += 1
    totalString = "".join([str(x) for x in nextGrid])
    print(totalString.count("#"))

partOne(preProcess(readIn))
partTwo(preProcess(readIn))