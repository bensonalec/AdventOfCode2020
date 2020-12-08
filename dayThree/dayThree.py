with open("dayThree.txt","r") as fi:
    readIn = fi.readlines()

def checkMap(readIn, horizChange, vertChange):
    vertical = 0
    horizontal = 0
    index = 0
    treecount = 0
    
    for ind,nextLine in enumerate(readIn):
        
        # print(nextLine[horizontal])
        if(ind % vertChange == 0 or vertChange == 1):
            if(nextLine[horizontal] == "#"):
                treecount += 1
                vertical += vertChange
            else:
                vertical += 1
            
            horizontal += horizChange
            horizontal %= (len(nextLine)-1)
        
    return treecount

print(checkMap(readIn, 1,1) * checkMap(readIn, 3,1) * checkMap(readIn, 5,1) * checkMap(readIn, 7,1) * checkMap(readIn, 1,2))
# print(checkMap(readIn, 3,1))
# print(checkMap(readIn, 5,1))
# print(checkMap(readIn, 7,1))
# print(checkMap(readIn, 1,2))
