from charactercreator.models import *
from armory.models import *

# How many total Characters are there?
# 302
print('Total Characters: ', Character.objects.count())

# How many of each specific subclass?
# Mages: 108
print('Mages: ', Mage.objects.count())

# Fighters: 68
print('Fighters: ', Fighter.objects.count())

# Clerics: 75
print('Clerics: ', Cleric.objects.count())

# Thieves: 51
print('Thieves: ', Thieve.objects.count())

# Necromancers: 11
print('Necromancers: ', Necromancer.objects.count())

# How many total Items?
# How many of the Items are weapons? How many are not?
# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?