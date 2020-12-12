with open("dayTwelve.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    midPoint = inp
    output = midPoint
    return output

def partOne(inp):
    position = [0,0,90]
    for x in inp:
        position[2] = position[2] % 360
        x = x.strip()
        action = x[0]
        magnitude = x[1:]
        if(action == "N"):
            position[0] += int(magnitude)
        elif(action == "S"):
            position[0] -= int(magnitude)
        elif(action == "E"):
            position[1] += int(magnitude)
        elif(action == "W"):
            position[1] -= int(magnitude)
        elif(action == "L"):
            position[2] -= int(magnitude)
        elif(action == "R"):
            position[2] += int(magnitude)
        elif(action == "F"):
            if(position[2] == 0):
                position[0] += int(magnitude)
            if(position[2] == 90):
                position[1] += int(magnitude)
            if(position[2] == 180):
                position[0] -= int(magnitude)
            if(position[2] == 270):
                position[1] -= int(magnitude)
    print(abs(position[0]) + abs(position[1]))

def partTwo(inp):
    position = [0,0]
    waypoint = [10,1]
    for x in inp:
        x = x.strip()
        action = x[0]
        magnitude = x[1:]
        magnitude = int(magnitude)
        if(action == "N"):    
            waypoint[1] += int(magnitude)
        elif(action == "S"):
            waypoint[1] -= int(magnitude)
        elif(action == "E"):
            waypoint[0] += int(magnitude)
        elif(action == "W"):
            waypoint[0] -= int(magnitude)
        elif(action == "L"):
            if(magnitude == 270):
                im = waypoint[1]
                waypoint[1] = waypoint[0] *-1
                waypoint[0] = im
            elif(magnitude == 180):
                waypoint[1] = waypoint[1] * -1
                waypoint[0] = waypoint[0] * -1
            elif(magnitude == 90):
                im = waypoint[1]
                waypoint[1] = waypoint[0] 
                waypoint[0] = im* -1
        elif(action == "R"):
            if(magnitude == 90):
                im = waypoint[1]
                waypoint[1] = waypoint[0] *-1
                waypoint[0] = im
            elif(magnitude == 180):
                waypoint[1] = waypoint[1] * -1
                waypoint[0] = waypoint[0] * -1
            elif(magnitude == 270):
                im = waypoint[1]
                waypoint[1] = waypoint[0] 
                waypoint[0] = im* -1
        elif(action == "F"):
            position[0] += int(magnitude) * waypoint[0]
            position[1] += int(magnitude) * waypoint[1]        
    print(abs(position[0]) + abs(position[1]))

partOne(preProcess(readIn))
partTwo(preProcess(readIn))