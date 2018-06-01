"""
How many total Characters are there?
How many of each specific subclass?
How many total Items?
How many of the Items are weapons? How many are not?
On average, how many Items does each Character have?
On average, how many Weapons does each character have?
"""

# How many total Characters are there?

from charactercreator.models import Character
characters = Character.objects.all()
len(characters)

# ANSWER: 302

# How many of each specific subclass?

from charactercreator.models import Fighter, Cleric, Thief, Mage, Necromancer

# FIGHTER

fighters = Fighter.objects.all()
len(fighters)

# ANSWER: 68

# CLERIC

clerics = Cleric.objects.all()
len(clerics)

# ANSWER: 75

# MAGE

mages = Mage.objects.all()
len(mages)

# ANSWER: 108

# THEIF

thieves = Thief.objects.all()
len(thieves)

# ANSWER: 51

# NECROMANCER

necromancers = Necromancer.objects.all()
len(necromancers)

# ANSWER: 11

# These answers add up to 318, which is more than the total number of characters (302) because the 11 necormancers are actually a subclass of mage.  So all necromancers are both necromancers and mages.

# How many total Items?

from armory.models import Item, Weapon
items = Item.objects.all()
len(items)

# ANSWER 174

# How many of the Items are weapons? How many are not?

len(Weapon.objects.all())

# ANSWER: 37 weapons

len(Item.objects.filter(weapon=None))

# ANSWER: 137 items which are not weapons

# On average, how many Items does each Character have?

inventories = characters.values('inventory')
inventory_totals = []
for inventory in inventories:
    inventory_totals.append(inventory['inventory'])
sum(inventory_totals)/len(inventory_totals)

# ANSWER: 89.17817371937639

# On average, how many Weapons does each character have?

weapons_carried = []
for character in characters:
    weapons_carried.append(len(character.inventory.filter(item_id__gt=137)))
sum(weapons_carried)/len(weapons_carried)

# ANSWER: 0.6721854304635762
