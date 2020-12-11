import functools

with open("dayEleven.txt") as fi:
    #. floor
    #L is empty
    ## is occupied
    readIn = fi.readlines()

def preProcess(inp):
    midPoint = inp
    output = midPoint
    return output
def checkSeatsPartOne(grid,x,y):
    
    #check if these are occupied
    
    count = 0
    directionBlocked = 0
    #dimensions are 100 by 95
    #basically, keep moving in those directions until either out of bounds, or see one
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
    
    #check if these are occupied
    
    count = 0
    directionBlocked = 0
    #dimensions are 100 by 95
    #basically, keep moving in those directions until either out of bounds, or see one
    validDirections = [(x-1,y),(x-1,y-1),(x-1,y+1),(x+1,y),(x+1,y-1),(x+1,y+1),(x,y+1),(x,y-1)]
    
    #for each direction, go out until either out of bounds, or a visible seat
    for ind, direct in enumerate(validDirections):
        currentX = x
        currentY = y
        xVal = currentX
        yVal = currentX

        while(True):
            # print("SDSD")
            pairs = [(currentX-1,currentY),(currentX-1,currentY-1),(currentX-1,currentY+1),(currentX+1,currentY),(currentX+1,currentY-1),(currentX+1,currentY+1),(currentX,currentY+1),(currentX,currentY-1)]
            xVal = pairs[ind][0]
            yVal = pairs[ind][1]
            
            # print(pairs[ind])
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


    # while(len(validDirections) > 0):
        
    #     pairs = [(x-1,y),(x-1,y-1),(x-1,y+1),(x+1,y),(x+1,y-1),(x+1,y+1),(x,y+1),(x,y-1)]
    #     for pair in pairs:
    #         xVal = pair[0]
    #         yVal = pair[1]
    #         # print(pair)
    #         # if(xVal >= 0 and yVal >= 0):
    #         #     print(grid[xVal][yVal])
    #         try:
    #             if(xVal >= 0 and yVal >= 0 and  grid[xVal][yVal] == "#"):
                    
    #                 count += 1
                    
    #         except:
    #             pass
    #     #given x,y check x - 1, x + 1, y - 1, y + 1
    #     # print("COUNT",count)
    #     return count
    # if(grid[x][y] == "L"):

    #     print(directionBlocked)

    return directionBlocked

    pass
import copy

def partOne(inp):
    inp = [x.strip() for x in inp]
    inp = [list(x) for x in inp]
    #if a seat is empty and there are no occupied seats adjacent, it is occupied next run
    #if a seat is occupied and four or more seats adjacent are occupied, it becomes empty
    grid = inp
    it = 0
    prevGrid = inp
    nextGrid = prevGrid
    # print(inp)
    while(prevGrid != nextGrid or it == 0):
        prevGrid = nextGrid
        # print("RUN")
        # old = prevGrid
        nextGrid = copy.deepcopy(prevGrid)

        for indRow, row in enumerate(prevGrid):
            for seatRow,seat in enumerate(row):
                #check the status of the surrounding eight chairs
                
                count = checkSeatsPartOne(prevGrid,indRow,seatRow)
                # print(count)
                # print(seat)
                if(seat == "L" and count == 0):
                    nextGrid[indRow][seatRow] = "#"
                    # print("trigg")
                elif(seat == "#" and count >= 4):
                    nextGrid[indRow][seatRow] = "L" 
                    # print("trigg")
        # print(prevGrid)
        # print(nextGrid)
        # print(nextGrid)
        it += 1
    totalString = "".join([str(x) for x in nextGrid])
    print(totalString.count("#"))
    # print(it)
def partTwo(inp):
    inp = [x.strip() for x in inp]
    inp = [list(x) for x in inp]
    #if a seat is empty and there are no occupied seats adjacent, it is occupied next run
    #if a seat is occupied and four or more seats adjacent are occupied, it becomes empty
    grid = inp
    it = 0
    prevGrid = inp
    nextGrid = prevGrid
    # print(inp)
    while(prevGrid != nextGrid or it == 0):
        prevGrid = nextGrid
        # print("RUN")
        # old = prevGrid
        nextGrid = copy.deepcopy(prevGrid)

        for indRow, row in enumerate(prevGrid):
            for seatRow,seat in enumerate(row):
                #check the status of the surrounding eight chairs
                
                count = checkSeatsPartTwo(prevGrid,indRow,seatRow)
                # print(count)
                # print(seat)
                if(seat == "L" and count == 0):
                    nextGrid[indRow][seatRow] = "#"
                    # print("trigg")
                elif(seat == "#" and count >= 5):
                    nextGrid[indRow][seatRow] = "L" 
                    # print("trigg")
        # print(prevGrid)
        # print(nextGrid)
        # break
        # print(nextGrid)
        it += 1
    totalString = "".join([str(x) for x in nextGrid])
    print(totalString.count("#"))
    # print(it)
    
    pass

partOne(preProcess(readIn))
partTwo(preProcess(readIn))