# How many total Characters are there? ==> 302
# Character.objects.count(), replace Character with class name 
# How many of each specific subclass?
''' 
example: Fighter.objects.all().count()
Fighter: 68
Mage: 108
Cleric: 75
Thief: 51
Necromancer: 11
'''
# How many total Items? ==> 174
# Item.objects.all().count()

# How many of the Items are weapons? How many are not? ==> 37 weapons : 137 non-weapon
# Weapon.objects.all().count()
# Item.objects.all().count() - Weapon.objects.all().count()

# On average, how many Items does each Character have? ==> 89
# Character.objects.aggregate(Avg('inventory'))

# On average, how many Weapons does each character have?
