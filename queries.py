from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

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
print('Thieves: ', Thief.objects.count())

# Necromancers: 11
print('Necromancers: ', Necromancer.objects.count())

# How many total Items?
# Total Items: 174
totalItems = Item.objects.count()
print('Total Items: ', totalItems)

# How many of the Items are weapons? How many are not?
# Weapon Items: 37
weaponItems = Weapon.objects.count()
print('Weapon Items: ', weaponItems)

# Non-weapon Items: 137
print('Non-weapon Items: ', totalItems - weaponItems)
# print('Non-weapon Items: ', Item.objects.exclude(item_id__in=Weapon.object.all()).count())

# On average, how many Items does each Character have?
# Average Item per Character: ~3
totalItemCount = 0
for toon in Character.objects.all():
    totalItemCount += toon.inventory.count()
print('Average Item per Character: ', totalItemCount / Character.objects.count())

# On average, how many Weapons does each character have?
# Average Weapon per Character: ~1
totalWeaponCount = 0
for toon in Character.objects.all():
    totalWeaponCount += toon.inventory.exclude(item_id__in=Weapon.object.all()).count()
print('Average Weapon per Character: ', (totalItemCount - totalWeaponCount) / Character.objects.count())