from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

# How many total Characters are there?
print('total characters: ', Character.objects.count())  # a: 302

# How many of each specific subclass?

# Mages
print('mages: ', Mage.objects.count())
# a: 108

# Fighters
print('fighters: ', Fighter.objects.count())
# a: 68

# Clerics
print('clerics: ', Cleric.objects.count())
# a: 75

# Thieves
print('thieves: ', Thief.objects.count())
# a: 51

# Necromancers
print('necromancers: ', Necromancer.objects.count())
# a: 11

# How many total Items?
print('items: ', Item.objects.count())
# a: 174

# How many of the Items are weapons?
print('weapons: ', Item.objects.filter(
    weapon__isnull=False).count())
# a: 37

# How many are not?
print('nonweapon items: ',
      Item.objects.filter(weapon__isnull=True).count())
# a: 137

# On average, how many Items does each Character have?
characters = list(Character.objects.all())
total = 0
for char in characters:
    total += char.inventory.count()

print('avg items count: ', round(
    total / Character.objects.count()))
# a: 3

# mage items avg
mages = list(Mage.objects.all())
mage_total = 0
for mage in mages:
    mage_total += mage.inventory.count()

print('mage avg items count: ', round(
    mage_total / Mage.objects.count()))
# a: 4

# fighter items avg
fighters = list(Fighter.objects.all())
fighter_total = 0
for fighter in fighters:
    fighter_total += fighter.inventory.count()

print('fighter avg items count: ', round(
    fighter_total / Fighter.objects.count()))
# a: 4

# cleric items avg
clerics = list(Cleric.objects.all())
cleric_total = 0
for cleric in clerics:
    cleric_total += cleric.inventory.count()

print('cleric avg items count: ', round(
    cleric_total / Cleric.objects.count()))
# a: 3

# thief items avg
thieves = list(Thief.objects.all())
thief_total = 0
for thief in thieves:
    thief_total += thief.inventory.count()

print('thief avg items count: ', round(
    thief_total / Thief.objects.count()))
# a: 3

# necromancer items avg
necromancers = list(Necromancer.objects.all())
necromancer_total = 0
for necromancer in necromancers:
    necromancer_total += necromancer.inventory.count()

print('necromancer avg items count: ', round(
    necromancer_total / Necromancer.objects.count()))
# a: 3

# On average, how many Weapons does each character have?
weapons_total = 0
for char in characters:
    weapons_total += char.inventory.filter(weapon__isnull=False).count()

print('avg weapons count: ', round(
    weapons_total / Character.objects.count()))
#a: 1

# Mage Average number of Weapons
mages = list(Mage.objects.all())
mage_weapon_total = 0
for mage in mages:
    mage_weapon_total += mage.inventory.filter(weapon__isnull=False).count()

print('mage avg weapons count: ', round(
    mage_weapon_total / Mage.objects.count()))
#a: 1

# Fighter Average number of Weapons
fighters = list(Fighter.objects.all())
fighter_weapon_total = 0
for fighter in fighters:
    fighter_weapon_total += fighter.inventory.filter(weapon__isnull=False).count()

print('fighter avg weapons count: ', round(
    fighter_weapon_total / Fighter.objects.count()))
#a: 1

# Cleric Average number of Weapons
clerics = list(Cleric.objects.all())
cleric_weapon_total = 0
for cleric in clerics:
    cleric_weapon_total += cleric.inventory.filter(weapon__isnull=False).count()

print('cleric avg weapons count: ', round(
    cleric_weapon_total / Cleric.objects.count()))
#a: 1

# Theif Average number of Weapons
thieves = list(Thief.objects.all())
thief_weapon_total = 0
for thief in thieves:
    thief_weapon_total += thief.inventory.filter(weapon__isnull=False).count()

print('thief avg weapons count: ', round(
    thief_weapon_total / Thief.objects.count()))
#a: 1

# Necromancer Average number of Weapons
necromancers = list(Necromancer.objects.all())
necromancer_weapon_total = 0
for necromancer in necromancers:
    necromancer_weapon_total += necromancer.inventory.filter(weapon__isnull=False).count()

print('necromancer avg weapons count: ', round(
    necromancer_weapon_total / Necromancer.objects.count()))
#a: 1
