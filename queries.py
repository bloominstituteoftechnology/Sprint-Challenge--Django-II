from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

# How many total Characters are there?
Character.objects.count() # Characters - 302

# How many of each specific subclass?
Fighter.objects.count() # Fighters - 68
Mage.objects.count() # Mages - 108
Cleric.objects.count() # Clerics - 75
Thief.objects.count() # Theif - 51
Necromancer.objects.count() # Necromancers - 11

# How many total Items?
Item.objects.count() # - 174

# How many of the Items are weapons?
Weapon.objects.count() # Weapons - 37

# How many are not?
# Item.objects.count() - Weapon.objects.count() = 137

# On average, how many Items does each Character have?
# Cannot get Character.inventory.count() to return anything

# On average, how many Weapons does each character have?
# Weapon.objects.count() / Character.objects.count() = 0.12?