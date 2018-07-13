# $ pipenv shell > $ python manage.py shell
# import models
from charactercreator.models import *
from armory.models import *

# How many total Characters are there? 302
len(Character.objects.all()) | | Character.objects.count()

# How many of each specific subclass?
# Fighter: 65
len(Fighter.objects.all()) | | Fighter.objects.count()

# Mage:108
len(Mage.objects.all()) | | Mage.objects.count()

# Cleric: 75
len(Cleric.objects.all()) | | Cleric.objects.count()

# Theif: 51
len(Theif.objects.all()) | | Thief.objects.count()

# Necromancer: 11
len(Necromancer.objects.all()) | | Necromancer.objects.count()

# How many total Items? 175
len(Item.objects.all()) | | Item.objects.count()

# How many Items are Weapons? 37
len(Weapon.objects.all()) | | Weapon.objects.count()

# How many Items are NOT Weapons? 138
# hacky, working on better solution
Item.objects.count() - Weapon.objects.count()

# On average, how many Items does each Character have?

# On average, how many Weapons does each Character have?
