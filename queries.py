from charactercreator.models import *
from armory.models import *

# How many total Characters are there?
# 302
print('Total Characters: ', Character.objects.count())

# How many of each specific subclass?
# Mages: 108
print('Mages: ', Mages.objects.count())

# Fighters: 68
print('Fighters: ', Fighters.objects.count())

# Clerics: 75
print('Clerics: ', Clerics.objects.count())

# Thieves: 51
print('Thieves: ', Thieves.objects.count())

# Necromancers: 11
print('Necromancers: ', Necromancers.objects.count())

# How many total Items?
# How many of the Items are weapons? How many are not?
# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?