from os import read


with open("dayFour.txt","r") as fi:
    readIn = fi.read()

readInSeparated = readIn.split("\n\n")

def partOne(readInSeparated):
    validCount = 0
    validTotal = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    validNorthPole = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']

    for x in readInSeparated:
        fields = x.split()
        fieldNames = [y.split(":")[0] for y in fields]
        fieldNames.sort()
        if(fieldNames == validTotal or fieldNames == validNorthPole):
            validCount += 1
    print(validCount)


def checkHcl(fieldPairs):
    try:
        if(fieldPairs[0] == "#" and len(fieldPairs.split("#")[1]) == 6):
            hairColor = fieldPairs.split("#")[1]
            for i in hairColor:
                if(i not in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]):
                    return False
            pass
            return True
        else:
            return False
    except:
        return False


def partTwo(readInSeparated):
    validCount = 0
    validTotal = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    validNorthPole = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    validEcl = ["amb","blu","brn","gry","grn","hzl","oth"]
    for x in readInSeparated:
        fields = x.split()
        fieldNames = [y.split(":")[0] for y in fields]
        fieldNames.sort()

        if(fieldNames == validTotal):
            fieldPairs = [(y.split(":")[0],y.split(":")[1]) for y in fields]
            fieldPairs.sort()
            fieldPairs = [z[1] for z in fieldPairs]
            #byr
            if(not(len(fieldPairs[0]) == 4 and 1920 <= int(fieldPairs[0]) <= 2002)):
                print("invalid byr",int(fieldPairs[0]))
                continue
            #ecl
            if(not(fieldPairs[2] in validEcl)):
                print("invalid ecl", fieldPairs[2])
                continue
            #eyr
            if(not(len(fieldPairs[3]) == 4 and 2020 <= int(fieldPairs[3]) <= 2030)):
                print("invalid eyr",fieldPairs[3])
                continue
            #hcl
            if(checkHcl(fieldPairs[4]) == False):
                print("invalid hcl",fieldPairs[4])
                continue
            #hgt
            if(len(fieldPairs[5])==5 or len(fieldPairs[5]) == 4):
                if(len(fieldPairs[5]) == 5 and fieldPairs[5][3:] == "cm"):
                    # val = int(fieldPairs[0:3])
                    try:
                        if(not(150 <= int(fieldPairs[5][0:3]) <= 193)):
                            
                            print("invalid hgt",fieldPairs[5])
                            continue
                    except:
                        print("invalid hgt",fieldPairs[5])
                        continue
                elif(len(fieldPairs[5]) == 4 and fieldPairs[5][2:] == "in"):
                    # val = int(fieldPairs[0:3])
                    try:
                        if(not(59 <= int(fieldPairs[5][0:2]) <= 76)):
                            print("invalid hgt",fieldPairs[5])

                            continue
                    except:
                        print("invalid hgt",fieldPairs[5])

                        continue
            else:
                print("invalid hgt",fieldPairs[5])

                continue
            #iyr
            if(not(len(fieldPairs[6]) == 4 and 2010<= int(fieldPairs[6]) <= 2020)):
                print("invalid iyr",fieldPairs[6])
                continue
            #pid
            if(len(fieldPairs[7]) == 9):
                try:
                    int(fieldPairs[7])
                except:
                    print("invalid pid",fieldPairs[7])
                    continue
            else:
                print("invalid pid",fieldPairs[7])
                continue

            validCount += 1

        elif(fieldNames == validNorthPole):
            fieldPairs = [(y.split(":")[0],y.split(":")[1]) for y in fields]
            fieldPairs.sort()
            fieldPairs = [z[1] for z in fieldPairs]

            if(not(1920 <= int(fieldPairs[0]) <= 2002)):
                print("invalid byr",fieldPairs[0])
                continue
            #ecl
            if(not(fieldPairs[1] in validEcl)):
                print("invalid ecl", fieldPairs[1])
                continue
            #eyr
            if(not(2020 <= int(fieldPairs[2]) <= 2030)):
                print("invalid eyr", fieldPairs[2])
                continue
            #hcl
            if(checkHcl(fieldPairs[3]) == False):
                print("invalid hcl",fieldPairs[3])
                continue
            #hgt
            if(len(fieldPairs[4])==5 or len(fieldPairs[4]) == 4):
                if(len(fieldPairs[4]) == 5 and fieldPairs[4][3:] == "cm"):
                    # val = int(fieldPairs[0:3])
                    try:
                        if(not(150 <= int(fieldPairs[4][0:3]) <= 193)):
                            print("invalid hgt",fieldPairs[4])
                            continue
                    except:
                        print("invalid hgt",fieldPairs[4])

                        continue
                elif(len(fieldPairs[4]) == 4 and fieldPairs[4][2:] == "in"):
                    # val = int(fieldPairs[0:3])
                    try:
                        if(not(59 <= int(fieldPairs[4][0:2]) <= 76)):
                            print("invalid hgt",fieldPairs[4])
                            continue
                    except:
                        print("invalid hgt",fieldPairs[4])

                        continue
            else:
                print("invalid hgt",fieldPairs[4])
                continue
            #iyr
            if(not(2010<= int(fieldPairs[5]) <= 2020)):
                print("invalid iyr",fieldPairs[5])
                continue
            #pid
            if(len(fieldPairs[6]) == 9):
                try:
                    int(fieldPairs[6])
                except:
                    print("invalid pid",fieldPairs[6])
                    continue
            else:
                print("invalid pid",fieldPairs[6])
                continue

            validCount += 1
    print(validCount)

partTwo(readInSeparated)