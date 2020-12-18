with open("daySeventeen.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    midPoint = [x.strip() for x in inp]
    output = midPoint
    return output

import copy

def partOne(inp):
    threeD = [[list(x) for x in inp]]
    # print(threeD)
    height = 1
    #list of the numbers for 0,0,0
    neighbors = [[0,0,1],[0,0,-1],[0,1,1],[0,1,-1],[0,1,0],[0,-1,1],[0,-1,-1],[0,-1,0],[1,0,1],[1,0,-1],[1,0,0],[-1,0,0],[1,1,1],[1,1,-1],[1,1,0],[1,-1,1],[1,-1,-1],[1,-1,0],[-1,0,1],[-1,0,-1],[-1,1,1],[-1,1,-1],[-1,1,0],[-1,-1,1],[-1,-1,-1],[-1,-1,0]]
    #three dimensional, our input is only one slice of that

    for cycle in range(0,6):
        newGrid = copy.deepcopy(threeD)
        newMinus = []
        newPlus = []
        for i in range(len(newGrid[0]) + 2):
            blankY = ["."] * (len(threeD[0]) + 2)
            newMinus.append(copy.deepcopy(blankY))
            newPlus.append(copy.deepcopy(blankY))
        newGrid.insert(0,newMinus)
        # print(newPlus)
        newGrid.append(newPlus)
        # newGrid[0][0][0] = "x"
        for indz,z in enumerate(threeD):
            blankY = ["."] * (len(threeD[0]) + 2)
            # print(blankY)
            newGrid[indz+1].append(copy.deepcopy(blankY))
            newGrid[indz+1].insert(0,copy.deepcopy(blankY))
            for indy,y in enumerate(z):
                newY = copy.deepcopy(y)
                newY.append(".")
                newY.insert(0,".")
                newGrid[indz+1][indy+1]= copy.deepcopy(newY)
                for indx,x in enumerate(y):
                    pass
        #now, work through newGrid to determine the matching neighbors for each cell
        # newGrid[2][0][0] = "x"

        interrim = copy.deepcopy(newGrid)

        for indz, z in enumerate(newGrid):
            for indy, y in enumerate(z):
                for indx, x in enumerate(y):
                    # print(x)
                    activeNeighbors = 0
                    #count the active neighbors
                    for i in neighbors:
                        checkX = indx + i[0]
                        checkY = indy + i[1]
                        checkZ = indz + i[2]
                        # print(checkX,checkY,checkZ)
                        #check that it's not negative
                        if((checkX > -1 and checkY > -1 and checkZ > -1)):
                            # print(checkX,checkY,checkZ,newGrid[checkZ][checkY][checkX])
                            try:
                                if(newGrid[checkZ][checkY][checkX] == "#"):
                                # print(checkZ,checkY,checkX)
                                # print(checkX,checkY,checkZ,newGrid[checkZ][checkY][checkX])
                                    activeNeighbors += 1
                            except:
                                pass
                    currentCell = newGrid[indz][indy][indx]
                    #rules:
                        #if a cube is active
                            #2 or 3 of it's neighbors are active, it remains active
                            #else becomes inactive
                        #else
                            #3 neighbors are active it becomes active
                            #else it remains inactive
                    # print(x,activeNeighbors)
                    # print(activeNeighbors)
                    if(currentCell == "#"):
                        if not (activeNeighbors == 2 or activeNeighbors == 3):
                            interrim[indz][indy][indx] = "."
                    else:
                        if(activeNeighbors == 3):

                            # print(indz,indy,indx,activeNeighbors)
                            interrim[indz][indy][indx] = "#"

                    # print()
                    # [[print(f) for f in x] for x in interrim]

                    pass
                    # exit()
        threeD = copy.deepcopy(interrim)

    onCount = 0
    for z in threeD:
        for y in z:
            for x in y:
                if(x == "#"):
                    onCount += 1

    print(onCount)
    

    #given the initial input, determine for each square the next level (basically, each cycle should add another z layer)
    pass

def partTwo(inp):
    threeD = [[[list(x) for x in inp]]]
    # print(threeD)
    height = 1
    #list of the numbers for 0,0,0
    neighbors = [[0,0,0,1],[0,0,0,-1],[0,0,1,1],[0,0,1,-1],[0,0,1,0],[0,0,-1,1],[0,0,-1,-1],[0,0,-1,0],[0,1,0,1],[0,1,0,-1],[0,1,0,0],[0,-1,0,0],[0,1,1,1],[0,1,1,-1],[0,1,1,0],[0,1,-1,1],[0,1,-1,-1],[0,1,-1,0],[0,-1,0,1],[0,-1,0,-1],[0,-1,1,1],[0,-1,1,-1],[0,-1,1,0],[0,-1,-1,1],[0,-1,-1,-1],[0,-1,-1,0],[1,0,0,1],[1,0,0,-1],[1,0,1,1],[1,0,1,-1],[1,0,1,0],[1,0,-1,1],[1,0,-1,-1],[1,0,-1,0],[1,1,0,1],[1,1,0,-1],[1,1,0,0],[1,-1,0,0],[1,1,1,1],[1,1,1,-1],[1,1,1,0],[1,1,-1,1],[1,1,-1,-1],[1,1,-1,0],[1,-1,0,1],[1,-1,0,-1],[1,-1,1,1],[1,-1,1,-1],[1,-1,1,0],[1,-1,-1,1],[1,-1,-1,-1],[1,-1,-1,0],[-1,0,0,1],[-1,0,0,-1],[-1,0,1,1],[-1,0,1,-1],[-1,0,1,0],[-1,0,-1,1],[-1,0,-1,-1],[-1,0,-1,0],[-1,1,0,1],[-1,1,0,-1],[-1,1,0,0],[-1,-1,0,0],[-1,1,1,1],[-1,1,1,-1],[-1,1,1,0],[-1,1,-1,1],[-1,1,-1,-1],[-1,1,-1,0],[-1,-1,0,1],[-1,-1,0,-1],[-1,-1,1,1],[-1,-1,1,-1],[-1,-1,1,0],[-1,-1,-1,1],[-1,-1,-1,-1],[-1,-1,-1,0],[-1,0,0,0],[1,0,0,0]]
    #three dimensional, our input is only one slice of that

    print(f"Cycle {0}")
    [[print(f) for f in x] for x in threeD]

    for cycle in range(0,6):
        newGrid = copy.deepcopy(threeD)
        #here generate the blank 4 D planes
        for i in range(len(newGrid[0][0]) + 2):
            blankY = ["."] * (len(threeD[0][0]) + 2)
            newMinus[w].append(copy.deepcopy(blankY))
            newPlus[w].append(copy.deepcopy(blankY))


        for indw,w in enumerate(threeD):
            newMinus = []
            newPlus = []
            for i in range(len(newGrid[0][0]) + 2):
                blankY = ["."] * (len(threeD[0][0]) + 2)
                newMinus.append(copy.deepcopy(blankY))
                newPlus.append(copy.deepcopy(blankY))
            newGrid[indw].insert(0,newMinus)
            newGrid[indw].append(newPlus)

            for indz,z in enumerate(w):
                blankY = ["."] * (len(threeD[0]) + 2)
                # print(blankY)
                newGrid[indz+1].append(copy.deepcopy(blankY))
                newGrid[indz+1].insert(0,copy.deepcopy(blankY))
                for indy,y in enumerate(z):
                    newY = copy.deepcopy(y)
                    newY.append(".")
                    newY.insert(0,".")
                    newGrid[indz+1][indy+1]= copy.deepcopy(newY)
                    for indx,x in enumerate(y):
                        pass
        #now, work through newGrid to determine the matching neighbors for each cell
        # newGrid[2][0][0] = "x"

        interrim = copy.deepcopy(newGrid)
        print(f"Cycle {cycle}")
        [[print(f) for f in x] for x in interrim]

        for indz, z in enumerate(newGrid):
            for indy, y in enumerate(z):
                for indx, x in enumerate(y):
                    # print(x)
                    activeNeighbors = 0
                    #count the active neighbors
                    for i in neighbors:
                        checkX = indx + i[0]
                        checkY = indy + i[1]
                        checkZ = indz + i[2]
                        # print(checkX,checkY,checkZ)
                        #check that it's not negative
                        if((checkX > -1 and checkY > -1 and checkZ > -1)):
                            # print(checkX,checkY,checkZ,newGrid[checkZ][checkY][checkX])
                            try:
                                if(newGrid[checkZ][checkY][checkX] == "#"):
                                # print(checkZ,checkY,checkX)
                                # print(checkX,checkY,checkZ,newGrid[checkZ][checkY][checkX])
                                    activeNeighbors += 1
                            except:
                                pass
                    currentCell = newGrid[indz][indy][indx]
                    #rules:
                        #if a cube is active
                            #2 or 3 of it's neighbors are active, it remains active
                            #else becomes inactive
                        #else
                            #3 neighbors are active it becomes active
                            #else it remains inactive
                    # print(x,activeNeighbors)
                    # print(activeNeighbors)
                    if(currentCell == "#"):
                        if not (activeNeighbors == 2 or activeNeighbors == 3):
                            interrim[indz][indy][indx] = "."
                    else:
                        if(activeNeighbors == 3):

                            print(indz,indy,indx,activeNeighbors)
                            interrim[indz][indy][indx] = "#"

                    # print()
                    # [[print(f) for f in x] for x in interrim]

                    pass
                    # exit()
        threeD = copy.deepcopy(interrim)
        print(f"Cycle {cycle+1}")
        [[print(f) for f in x] for x in interrim]
        # print(threeD)

    onCount = 0
    for z in threeD:
        for y in z:
            for x in y:
                if(x == "#"):
                    onCount += 1

    print(onCount)
    

    #given the initial input, determine for each square the next level (basically, each cycle should add another z layer)
    pass

    pass

partOne(preProcess(readIn))
partTwo(preProcess(readIn))