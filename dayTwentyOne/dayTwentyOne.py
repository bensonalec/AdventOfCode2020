from collections import defaultdict

with open("dayTwentyOne.txt") as fi:
    lines = fi.read()
#parse the list in 
lineList = []
for line in lines.split("\n")[:-1]:
    lineSpl = line.split(" (contains ")
    foods = lineSpl[0].split(" ")
    allergens = lineSpl[1][:-1].split(", ")
    lineList.append((foods,allergens))

allergyCountDic = defaultdict((lambda : 0))
#first, count how many times allergen appears in a line
for line in lineList:
    for allergen in line[1]:
        allergyCountDic[allergen]+=1

allergyAndIngredientCountDic = defaultdict((lambda : defaultdict(int)))
for line in lineList:
    for allergen in line[1]:
        for ingredient in line[0]:
            allergyAndIngredientCountDic[allergen][ingredient] += 1

#now, find the difference between these two lists (an ingredient must have the same count as it's allergen to be a valid option for that)

allergyAndIngredientCountDic = dict(sorted(allergyAndIngredientCountDic.items(), key = lambda item: len(item[1])))
finalList = defaultdict(lambda : "")
for k,v in allergyAndIngredientCountDic.items():
    countShouldBe = allergyCountDic[k]
    trueList = []
    for iK,iV in v.items():
        if(iV==countShouldBe):
            trueList.append(iK)
    allergyAndIngredientCountDic[k] = trueList
import copy
allergyAndIngredientCountDic = dict(sorted(allergyAndIngredientCountDic.items(), key = lambda item: len(item[1])))
for k,v in allergyAndIngredientCountDic.items():
    trueList = allergyAndIngredientCountDic[k]
    for i in finalList.values():
        try:
            trueList.remove(i)
        except:
            pass
    for i in trueList:
        if(i not in finalList.values()):
            finalList[k] = i

print(finalList)
foundIngredients = finalList.values()
allIngredients = []
for i in lineList:
    for j in i[0]:
        if(j not in allIngredients):
            allIngredients.append(j)
    
#find the difference between the foundIngredients and allIngredients
notAllergens = (list(list(set(allIngredients)-set(foundIngredients)) + list(set(foundIngredients)-set(allIngredients))))

finalCount = 0

for i in lineList:
    ingredients = i[0]
    for j in ingredients:
        if(j in notAllergens):
            finalCount += 1


finalList = dict(sorted(finalList.items(), key = lambda item: item[0]))

print(",".join(finalList.values()))