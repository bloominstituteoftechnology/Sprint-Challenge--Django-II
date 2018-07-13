from charactercreator.models import *
from armory.models import *

# 1. How many total Characters are there?
Character.objects.count()  # 302

# 2. How many of each specific subclass?

# Fighter
Fighter.objects.count()  # 68

# Mage
Mage.objects.count()  # 108

# Cleric
Cleric.objects.count()  # 75

# Thief
Thief.objects.count()  # 51

# Necromancer
Necromancer.objects.count()  # 11

# 3 How many total Items?
Item.objects.count()  # 175

# 4 How many of the Items are weapons? How many are not?
Weapon.objects.count() #37
Item.objects.exclude(weapon__isnull=False).count() #138

#5 On average, how many Items does each Character have?

#6 On average, how many Weapons does each character have?
