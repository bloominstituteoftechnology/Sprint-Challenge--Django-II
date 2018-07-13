from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

# How many total Characters are there?
print('total characters: ', Character.objects.count())  # Answer: 302

# How many of each specific subclass?

# Mages
print('mages: ', Mage.objects.count())  # Answer: 108

# Fighters
print('fighters: ', Fighter.objects.count())  # Answer: 68

# Clerics
print('clerics: ', Cleric.objects.count())  # Answer: 75

# Thieves
print('thieves: ', Thief.objects.count())  # Answer: 51

# Necromancers
print('necromancers: ', Necromancer.objects.count())  # Answer: 11

# How many total Items?
print('items: ', Item.objects.count())  # Answer: 174

# How many of the Items are weapons?
print('weapons: ', Item.objects.filter(
    weapon__isnull=False).count())  # Answer: 37

# How many are not?
print('nonweapon items: ',
      Item.objects.filter(weapon__isnull=True).count())  # Answer: 137

# On average, how many Items does each Character have?
# On average, how many Weapons does each character have?
