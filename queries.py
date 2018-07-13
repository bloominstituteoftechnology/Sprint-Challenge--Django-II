from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

# or
# from charactercreator.models import *
# from armor.models.import *

# How many total Characters are there?
### 302
total_characters = Character.objects.count()
print("Total number of characters: ", total_characters)


# How many of each specific subclass?
### 68 Fighters
fighters = Fighter.objects.count()
print("Total number of fighters: ", fighters)

### Not sure if you want Necromancers counted as Mages or not
### 97 Mages that are not Necromancers (assuming Necros should not be counted as Mages)
mages = Mage.objects.count() - Necromancer.objects.count()
print("Total number of mages: ", mages)
### 108 Mages if Necromancers should be counted as Mages:
mages = Mage.objects.count()
print("Total number of mages: ", mages)

### 75 Clerics
clerics = Cleric.objects.count()
print("Total number of clerics: ", clerics)

### 51 Thieves
thieves = Thief.objects.count()
print("Total number of thieves: ", thieves)

### 11 Necromancers
necromancers = Necromancer.objects.count()
print("Total number of necromancers: ", necromancers)


# How many total Items?
### 174 items
total_items = Item.objects.count()
print("Total number of items: ", total_items)

# How many of the Items are weapons? How many are not?
### 37 weapons
total_weapons = Weapon.objects.count()
print("Total number of weapons: ", total_weapons)

### 137 items that are not weapons
total_non_weapons = Item.objects.count() - Weapon.objects.count()
print("Total that are not weapons: ", total_non_weapons)


# On average, how many Items does each Character have?
### 2.9735
totalItems = 0
for character in Character.objects.all():
  totalItems += character.inventory.count()
avg_items = totalItems / Character.objects.count()
print("Average number of items per character", avg_items)

# On average, how many Weapons does each character have?
### 6.7218
nonWeapons = 0
for character in Character.objects.all():
  nonWeapons += character.inventory.exclude(item_id__in=Weapon.objects.all()).count()
avg_Weapons = (totalItems - nonWeapons) / Character.objects.all().count()
print("Average number of weapons: ", avg_Weapons)