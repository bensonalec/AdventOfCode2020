from tqdm import tqdm
with open("dayNine.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    midPoint = inp
    output = [int(x) for x in midPoint]
    return output

def partOne(inp):
    start = 0
    end = 25
    for i in inp[end:]:
        preamble = inp[start:end]
        found = False
        for ind,x in enumerate(preamble):
            for indy,y in enumerate(preamble):
                if(x + y == i and ind != indy):
                    found=True
        if(found == False):
            return i
            break
        else:
            start += 1
            end += 1

def partTwo(inp, badNum):
    for ind,i in enumerate(inp):
        contigSum = i
        contigRange = [i]
        for indx,x in enumerate(inp[ind+1:]):
            if(contigSum < badNum):
                contigSum += x
                contigRange.append(x)
            else:
                break
        
        if(contigSum == badNum):
            maximum = max(contigRange)
            minimum = min(contigRange)
            print(maximum + minimum)
            break


partOne(preProcess(readIn))
partTwo(preProcess(readIn),partOne(preProcess(readIn)))