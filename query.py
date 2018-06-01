from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

# How many total Characters are there?
print('Total characters: ', Character.objects.count())  # Answer: 302

# How many of each specific subclass?

# Mages
print('Number of Mages: ', Mage.objects.count())  # Answer: 108

# Fighters
print('Number of Fighters: ', Fighter.objects.count())  # Answer: 68

# Clerics
print('Number of Clerics: ', Cleric.objects.count())  # Answer: 75

# Thieves
print('Number of Thieves: ', Thief.objects.count())  # Answer: 51

# Necromancers
print('Number of Necromancers: ', Necromancer.objects.count())  # Answer: 11

# How many total Items?
print('Total number of Items: ', Item.objects.count())  # Answer: 174

# How many of the Items are weapons?
print('Number of Weapons: ', Item.objects.filter(
    weapon__isnull=False).count())  # Answer: 37

# How many are not?
print('Number of non-Weapon Items: ',
      Item.objects.filter(weapon__isnull=True).count())  # Answer: 137

# On average, how many Items does each Character have?
characters = list(Character.objects.all())
total = 0
for char in characters:
    total += char.inventory.count()

print('Average number of Items: ', round(
    total / Character.objects.count()))  # Answer: 3

# Mage Average number of Items
mages = list(Mage.objects.all())
mage_total = 0
for mage in mages:
    mage_total += mage.inventory.count()

print('Average number of Items a Mage has: ', round(
    mage_total / Mage.objects.count()))  # Answer: 4

# Fighter Average number of Items
fighters = list(Fighter.objects.all())
fighter_total = 0
for fighter in fighters:
    fighter_total += fighter.inventory.count()

print('Average number of Items a Figher has: ', round(
    fighter_total / Fighter.objects.count()))  # Answer: 4

# Cleric Average number of Items
clerics = list(Cleric.objects.all())
cleric_total = 0
for cleric in clerics:
    cleric_total += cleric.inventory.count()

print('Average number of Items a Cleric has: ', round(
    cleric_total / Cleric.objects.count()))  # Answer: 3

# Theif Average number of Items
thieves = list(Thief.objects.all())
thief_total = 0
for thief in thieves:
    thief_total += thief.inventory.count()

print('Average number of Items a Thief has: ', round(
    thief_total / Thief.objects.count()))  # Answer: 3

# Necromancer Average number of Items
necromancers = list(Necromancer.objects.all())
necromancer_total = 0
for necromancer in necromancers:
    necromancer_total += necromancer.inventory.count()

print('Average number of Items a Necromancer has: ', round(
    necromancer_total / Necromancer.objects.count()))  # Answer: 3

# On average, how many Weapons does each character have?
weapons_total = 0
for char in characters:
    weapons_total += char.inventory.filter(weapon__isnull=False).count()

print('Average number of Weapons: ', round(
    weapons_total / Character.objects.count()))  # Answer: 1

# Mage Average number of Weapons
mages = list(Mage.objects.all())
mage_weapon_total = 0
for mage in mages:
    mage_weapon_total += mage.inventory.filter(weapon__isnull=False).count()

print('Average number of Weapons a Mage has: ', round(
    mage_weapon_total / Mage.objects.count()))  # Answer: 1

# Fighter Average number of Weapons
fighters = list(Fighter.objects.all())
fighter_weapon_total = 0
for fighter in fighters:
    fighter_weapon_total += fighter.inventory.filter(weapon__isnull=False).count()

print('Average number of Weapons a Figher has: ', round(
    fighter_weapon_total / Fighter.objects.count()))  # Answer: 1

# Cleric Average number of Weapons
clerics = list(Cleric.objects.all())
cleric_weapon_total = 0
for cleric in clerics:
    cleric_weapon_total += cleric.inventory.filter(weapon__isnull=False).count()

print('Average number of Weapons a Cleric has: ', round(
    cleric_weapon_total / Cleric.objects.count()))  # Answer: 1

# Theif Average number of Weapons
thieves = list(Thief.objects.all())
thief_weapon_total = 0
for thief in thieves:
    thief_weapon_total += thief.inventory.filter(weapon__isnull=False).count()

print('Average number of Weapons a Thief has: ', round(
    thief_weapon_total / Thief.objects.count()))  # Answer: 1

# Necromancer Average number of Weapons
necromancers = list(Necromancer.objects.all())
necromancer_weapon_total = 0
for necromancer in necromancers:
    necromancer_weapon_total += necromancer.inventory.filter(weapon__isnull=False).count()

print('Average number of Weapons a Necromancer has: ', round(
    necromancer_weapon_total / Necromancer.objects.count()))  # Answer: 1