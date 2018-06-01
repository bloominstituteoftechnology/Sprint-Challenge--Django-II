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