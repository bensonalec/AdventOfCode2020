with open("daySeven.txt") as fi:
    readIn = fi.readlines()

groups = readIn

#split by contain
#x can contain num y bags, 

ruleList = {}
for gr in groups:
    gr = gr.replace(".","")
    contSplit = gr.split("contain")
    #contSplit[0] is the bag you're making a rule for
    ruleFor = contSplit[0].replace("bags","").strip()
    #contSplit[1].split[","] is the list of rules, in the form number bagDescription bag/s
    rules = contSplit[1].split(",")
    imRules = []
    for ru in rules:
        ru = ru.replace("bags","")

        ru = ru.replace("bag","")
        #remove leading and trailing whitespace
        ru = ru.strip()
        number = ru.split(" ")[0]
        bagType = " ".join(ru.split(" ")[1:])
        imRules.append((number,bagType))
    ruleList[ruleFor] = imRules

def findCountInside(bag):
    inCount = 0
    bagCountIn = 0
    for i in ruleList[bag]:        
        if i[0] == "no":
            return 1
        else:
            bagCountIn += int(i[0])
            numBags = int(i[0])
            idcMan = findCountInside(i[1])
            numBagsAndInsideThem =  idcMan * numBags
            inCount += numBagsAndInsideThem
            inCount += numBags if idcMan != 1 else 0 

    return inCount

def findBagsInside(target, bag):
    for i in ruleList[bag]:
        if i[0] == "no":
            return False
        if i[1] == target:
            return True
        else:
            samp = findBagsInside(target, i[1])
            if samp == True:
                return samp
    return False

def partOne():
    count = 0
    for ruleKey in ruleList.keys():
        if(findBagsInside("shiny gold",ruleKey) == True):
            count+=1
    print(count)

def partTwo():
    count = findCountInside("shiny gold")
    print(count)

partOne()
partTwo()