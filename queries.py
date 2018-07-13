
############## The below imports were needed in the shell to run the quireis

# from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
# from armory.models import Item, Weapon



################# How many total Characters are there? ################
totalChrs = len(Character.objects.all())
print("Total number of characters: " + str(totalChrs))  # Ans: 302
 

################# How many of each specific subclass? #################

########### Fighters
fighterChrs = len(Fighter.objects.all())
print("Total of fighter characters: " + str(fighterChrs)) # Ans: 68

########### Mage
mageChrs = len(Mage.objects.all())
print("Total of mage characters: " + str(mageChrs)) # Ans: 108

########### Cleric
clericChrs = len(Cleric.objects.all())
print("Total of cleric characters: " + str(clericChrs)) # Ans: 75

########### Theif
thiefChrs = len(Theif.objects.all())
print("Total of theif characters: " + str(thiefChrs)) # Ans: 51

########### Necromancer
necroChrs = len(Necromancer.objects.all())
print("Total of Necromancer characters: " + str(necroChrs)) # Ans: 11


###################### How many total Items? ######################

####### Items
totalItems = len(Item.objects.all())
print("Total number of items: " + str(totalItems)) # Ans: 174

####### Weapons
totalWeapons = len(Weapon.objects.all())
print("Total number of weapons: " + str(totalWeapons)) # Ans: 37

####### Other Items
totalOtherItems = totalItems - totalWeapons
print("Total number of other items: " + str(totalOtherItems)) # Ans: 137

############## On average, how many Items does each Character have? #################
averageItems = (totalItems / totalChrs)
print("Average number of items for each character: " + str(averageItems)) # Ans: 3

############## On average, how many Weapons does each character have? ###############
averageWeapons = (totalWeapons / totalChrs)
print("Average number of weapons for each character: " + str(averageWeapons)) # Ans: 1