# Toatal Charcters
from  charactercreator.models import *
>>> Character.objects.count()
302

# Subclasses
>>> Fighter.objects.count()
68
>>> Mage.objects.count()
108
>>> Cleric.objects.count()
75
>>> Thief.objects.count()
51
>>> Necromancer.objects.count()
11

# Total items
>>> from armory.models import *
>>> Item.objects.count()
174
# Total Weapons 
>>> Weapon.objects.count()
37

# How many of the items are weapons ?
>>> Item.objects.count()-Weapon.objects.count()
137

# On average, how many Items does each Character have?
>>> Character.objects.count() / Item.objects.count()
1.735

# On average, how many Items does each Character have?
characters = Character.objects.count()
result = 0
for ele in characters:
    result += ele.inventory.count()

result / characters
3

