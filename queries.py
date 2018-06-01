from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
# How many total Characters are there?
charCount = Character.objects.count()
# 302

# How many of each specific subclass?
Fighter.objects.count()
# 68
Mage.objects.count()
# 108
Cleric.objects.count()
# 75
Thief.objects.count()
# 51
Necromancer.objects.count()
# 11
# Necromancer extends Mage so the total character count is affected as all Necromancers are Mages

# How many total Items?
from armory.models import Item, Weapon
Item.objects.count()
# 174

# How many of the Items are weapons? How many are not?
Weapon.objects.count()
# 37 weapons

items = Item.objects.all()
not_weapons = [i for i in items if not hasattr(i, 'weapon')]
len(not_weapons)
# 137

# On average, how many Items does each Character have?
items = Character.objects.values('inventory').count()
print(round(items / charCount))
# 3, rounded

# On average, how many Weapons does each character have?
