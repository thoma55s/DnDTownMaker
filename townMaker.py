import random
import sys

if "dawn" in sys.argv:
	print("dawn")
	animals = "animals.txt"
	races = "dawnRaces.txt"
	townPrefix = "dawnTownPrefix.txt"
	townSuffix = "dawnTownSuffix.txt"
	leader = "leaders.txt"
	monsterIssues = "dawnMonsterIssues.txt"
	dieties = "dawnDieties.txt"
else:
	animals = "monsters.txt"
	races = "dndRaces.txt"
	townPrefix = "dndTownPrefix.txt"
	townSuffix = "dndTownSuffix.txt"
	leader = "classes.txt"
	monsterIssues = "dndMonsterIssues.txt"
	dieties = "dndDieties.txt"
	
def getName(*fileNames): #gets a name from a txt file
	nameArray = []
	for fileName in fileNames:
		nameArray.extend(getFile(fileName))
	randomName = random.randint(0,len(nameArray) - 1)
	return nameArray[randomName][:-1] # deletes enter character must have blank line at end of txt files

def getFile(fileName):
	nameArray = []
	with open(fileName, "r") as ins:
		for line in ins:
			nameArray.append(line)
	return nameArray

def getTownName(): #gets a prefix and suffix to make a town name
	return getName("prefix.txt", townPrefix) + getName("suffix.txt", townSuffix)

def getPopulation():
	range = random.randint(0,300)
	return 20 + range



		
print("Name: " + getTownName())
print("Worships: " + getName(dieties))
print("Primarily Populated with: " + getName(races))
print("Town Leader is a: " + getName(leader))
print("Government: " + getName("governments.txt"))
print("Population: " + str(getPopulation()))
print("Quests")
for x in range(0,3):
	print(getName(monsterIssues)  + " " + getName(animals) + "s")
