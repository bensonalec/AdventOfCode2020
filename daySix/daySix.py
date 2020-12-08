with open("daySix.txt") as fi:
    readIn = fi.read()

groups = readIn.split("\n\n")

def partOne(groups):
    total = 0
    for gr in groups:
        noNL = gr.replace("\n","")
        total += len(set(noNL))
    print(total)

def partTwo(groups):
    total = 0
    for gr in groups:
        
        # noNL = gr.replace("\n","")
        #find letters that are present on every line
        lines = gr.split("\n")
        
        total += len(set.intersection(*map(set,lines)))
    print(total)

partOne(groups)
partTwo(groups)