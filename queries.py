from django.db import models
from django.db.models import Avg

from charactercreator.models import *
from armory.models import *

characters = Character.objects.all()
print('Total number of characters: ', characters.count()) # A: 302

fighters = Fighter.objects.all()
print('Total number of Fighters: ', fighters.count()) # A: 68

mages = Mage.objects.all()
print('Total number of Mages: ', mages.count()) # A: 108

clerics = Cleric.objects.all()
print('Total number of Clerics: ', clerics.count()) # A: 75

thiefs = Thief.objects.all()
print('Total number of Thiefs: ', thiefs.count()) # A: 51

necromancers = Necromancer.objects.all()
print('Total number of Necromancers: ', necromancers.count()) # A: 11


items = Item.objects.all()
print('Total number of items: ', items.count()) # A: 174

weapons = Weapon.objects.all()
print('Total number of weapons: ', weapons.count()) # A: 37

not_weapons = items.exclude(weapon__gte=0)
print('Total number of items that are NOT weapons: ', not_weapons.count()) # A: 137

avg_items = items.count() / characters.count()
# model solution:
characters.annotate(count=models.Count('inventory')).aggregate(models.Avg('count'))
print('Average number of items each Character has: ', avg_items) # A: 0.576

avg_weapons = weapons.count() / characters.count()
#model solution:
characters.annotate(count=models.Count('inventory__weapon')).aggregate(models.Avg('count'))
print('Average number of weapons each Character has: ', avg_weapons) # A: 0.123



# How many total characters are there? A: 302

# How many of each specific subclass?
  # Fighters = 68
  # Mages = 108
  # Clerics = 75
  # Thiefs = 51
  # Necromancers = 11

# How many total items? A: 174

# How many of the items are weapons? A: 37

# How many of the items are NOT weapons? A: 137

# On average, how many Items does each Character have? A: 0.576

# On average, how many Weapons does each Character have? A: 0.123