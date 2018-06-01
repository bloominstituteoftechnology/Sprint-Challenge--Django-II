from charactercreator.models import Character, Fighter, Mage, Cleric, Theif, Necromancer
from armory.models import Item, Weapon

# total characters of all classes
totalChars = len(Character.objects.all())
print("The total number of characters: " + str(totalChars))
 
# total of subclass characters
fighterChars = len(Fighter.objects.all())
print("The total of fighter characters: " + str(fighterChars))

mageChars = len(Mage.objects.all())
print("The total of mage characters: " + str(mageChars))

clericChars = len(Cleric.objects.all())
print("The total of cleric characters: " + str(clericChars))

theifChars = len(Theif.objects.all())
print("The total of theif characters: " + str(theifChars))

necroChars = len(Necromancer.objects.all())
print("The total of Necromancer characters: " + str(necroChars))


# total number of items
totalItems = len(Item.objects.all())
print("The total number of items is: " + str(totalItems))

totalWeapons = len(Weapon.objects.all())
print("The total number of weapons is: " + str(totalWeapons))

totalOtherItems = totalItems - totalWeapons
print("The total number of items that are not weapons is: " + str(totalOtherItems))

# average number of items per character
averageItems = (totalItems / totalChars)
print("The average number of items for each character is: " + str(averageItems))

# average number of weapons per character
averageWeapons = (totalWeapons / totalChars)
print("The average number of weapons for each character is: " + str(averageWeapons))