from charactercreator.models import Character, Cleric, Fighter, Mage, Necromancer, Thief
from armory.models import Weapon, Item

# How many total Characters are there?
# How many of each specific subclass?
# How many total Items?
# How many of the Items are weapons? How many are not?
# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?

# Characters
Character.objects.count() # 302

# Subclasses
Fighter.objects.count() # 68
Mage.objects.count() # 108
Cleric.objects.count() # 75
Thief.objects.count() # 51
Necromancer.objects.count() # 11

# Items
Item.objects.count() # 174

# Are / Are Not Weapons
print("\nOut of %d items, %d are weapons, and %d are not.\n" % (Item.objects.count(), Weapon.objects.count(), Item.objects.count() - Weapon.objects.count())) # 37 / 137

# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?
characters = Character.objects.count()
inventory = [chars.inventory.count() for chars in Character.objects.all()]
items = sum(inventory) / characters
average_weapons = round(Weapon.objects.count()/Character.objects.count(), 2)
print("\nOn average, each Character has %f items and %f weapons\n" % (items, average_weapons)) # 2.97 / 0.12
