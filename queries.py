from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

print("\nHow many total Characters are there?")
Character.objects.all().count()
#How many total Characters are there?
#How many of each specific subclass?
#How many total Items?
#How many of the Items are weapons? How many are not?
#On average, how many Items does each Character have?
#On average, how many Weapons does each character have?
