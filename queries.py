# queries.py
''' To Test my knowledge of Django ORM using Djano-RPG database
'''
# imports
from django.db import models

# Only import what is mention
from armory.models import Item, Weapon

# to bring all of the character model types
from charactercreator.models import *
# for more explict use:
# from charactercreator.models import Cleric, Fighter, Mage, Necromancer, Thief

# How many total Characters are there?
characterCount = Character.objects.count() # 302

# How many of each specific subclass?

cleric = Cleric.objects.count() #75
fighter = Fighter.objects.count() #68
mage = Mage.objects.count() #108
necromancer = Necromancer.objects.count() #11
thief = Thief.objects.count()  #51

# How many total Items?
itemsCount = Item.objects.count() # 174

# How many of the Items are weapons? 37
weaponsCount = Weapons.objects.count()

# How many are not?
notWeaponsCount = items - weaponsCount

# On average, how many Items does each Character have?
averageItemPerCharacter = itemsCount / characterCount

# On average, how many Weapons does each character have?
averageWeaponPerCharacter = weapons / characterCount
