import itertools
from typing import List

with open("dayTen.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    midPoint = inp
    output = [int(x) for x in midPoint]
    return output

def partOne(inp):
    inp.sort()
    oneList= 0
    threeList = 0
    for ind,i in enumerate(inp[:-1]):
        if(inp[ind+1] - i == 1):
            oneList+=1
        elif(inp[ind+1] - i == 3):
            threeList += 1
    threeList+=1
    oneList += 1
    print(oneList*threeList)

class node:
    contents = None
    
    def __init__(self,value):
        self.contents = value
        self.nextNode = []

def buildGraph(inp):
    nodes = {}
    for i in inp:
        nodes[i] = node(i)
    for i in inp:
        threeNext = [x + i for x  in range(1,4)]
        for x in threeNext:
            if x in nodes.keys():
                nodes[i].nextNode.append(nodes[x])

    return nodes

def checkGraph(nodes):
    nodesKeys = list(nodes.keys())

    nodesKeys.sort(reverse=True)

    reachEnd = {}
    #see how many times it can get to the end (by default only 1) (store this)
    reachEnd[nodesKeys[0]] = 1
    #then, for each node before that:
    for i in nodesKeys[1:]:
        canVisit = nodes[i].nextNode
        canEnd = 0
        for j in canVisit:
            canEnd += reachEnd[j.contents]
        reachEnd[i] = canEnd

    print(reachEnd[1] + reachEnd[2] + reachEnd[3])
    
        #see how many times the nodes it can reach can reach the end, add each of these ways up (store this)
def partTwo(inp):
    inp.sort()
    nodes = buildGraph(inp)
    checkGraph(nodes)


partOne(preProcess(readIn))
partTwo(preProcess(readIn))