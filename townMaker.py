import random

def getName(x): #gets a name from a txt file
	nameArray = []
	with open(x, "r") as ins:
		for line in ins:
			nameArray.append(line)
	
	randomName = random.randint(0,len(nameArray) - 1)
	return nameArray[randomName][:-1] # deletes enter character

def getTownName(): #gets a prefix and suffix to make a town name
	return getName("townPrefix.txt") + getName("townSuffix.txt")

def getPopulation():
	range = random.randint(0,300)
	return 20 + range

		
print("Name: " + getTownName())
print("Worships: " + getName("dieties.txt"))
print("Primarily Populated with: " + getName("races.txt"))
print("Town Leader is a: " + getName("classes.txt"))
print("Population: " + str(getPopulation()))
