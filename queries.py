from armory.models import Item, Weapon
from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer

# How many total Characters are there?
c = Character.objects.all()
len(c) # answer is 302


# How many of each specific subclass?
Fighter.objects.count()
Mage.objects.count()
Cleric.objects.count()
Thief.objects.count()
Necromancer.objects.count()


# How many total Items?
eyetums = Item.objects.all() # gets total number of items
len(eyetums) # shows 174 items

# How many of the Items are weapons? How many are not?
waypuns = Weapon.objects.all() # gets total number of weapons
len(waypuns) # shows 37 items
knotWaypuns = len(eyetums) - len(waypuns) # the answer is 137


# On average, how many Items does each Character have?
inventory_sum = 0
for character in Character.objects.all():
  inventory_sum += character.inventory.count()

inventory_sum/len(c)


# On average, how many Weapons does each character have?
weapon_sum = 0
for character in Character.objects.all():
  weapon_sum += character.inventory.count()

weapon_sum/len(c)