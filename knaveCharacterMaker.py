import random

def getName(x): #gets a name from a txt file
	nameArray = []
	with open(x, "r") as ins:
		for line in ins:
			nameArray.append(line)
	
	randomName = random.randint(0,len(nameArray) - 1)
	return nameArray[randomName][:-1] # deletes enter character must have blank line at end of txt files

def rollDice(x):
    return random.randint(1,x)

def getScore():
    return min(rollDice(6),min(rollDice(6), rollDice(6)))

print("Strength: " + str(10 + getScore()))
print("Dexterity: " + str(10 + getScore()))
print("Constitution: " + str(10 + getScore()))
print("Intelligence: " + str(10 + getScore()))
print("Wisdom: " + str(10 + getScore()))
print("Charisma: " + str(10 + getScore()))

print("HP Roll: " + str(rollDice(8)))

print("Physique: " + getName("physique.txt"))
print("Face: " + getName("face.txt"))
print("Skin: " + getName("skin.txt"))
print("Hair: " + getName("hair.txt"))
print("Clothing: " + getName("clothing.txt"))
print("Virtue: " + getName("virtue.txt"))
print("Vice: " + getName("vice.txt"))
print("Speech: " + getName("speech.txt"))
print("Background: " + getName("background.txt"))
print("Misfortunes: " + getName("misfortunes.txt"))
print("Alignment: " + getName("alignment.txt"))
print("Armor: " + getName("armor.txt"))
print("Helmets and Shields: " + getName("helmetsAndShields.txt"))
print("Dungeoneering Gear: " + getName("dungeoneeringGear.txt"))
print("General Gear 1: " + getName("generalGear1.txt"))
print("General Gear 2: " + getName("generalGear2.txt"))

