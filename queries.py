# Django ORM
# set environment shell, load test data, and enter python shell
# pipenv shell
# python manage.py loaddata testdata.json
# python shell

# === commands from within python shell ===

print('\n')
print('===== Django-II Sprint Challenge Answers using Django ORM =====')
print('\n')

# import models from necessary apps
from charactercreator.models import *
from armory.models import *

# ========== Q1 ==========

print('Q1: How many total Characters are there?')
characters = Character.objects.all()
char_len = len(characters)
print('There are %i total Characters.' % (char_len))
print ('\n')
# answer: 302

# ========== Q2 ==========

print('Q2: How many of each specific subclass?')
fighters = Fighter.objects.all()
mages = Mage.objects.all()
clerics = Cleric.objects.all()
thieves = Thief.objects.all()
necromancers = Necromancer.objects.all()

fighter_len = len(fighters)
mage_len = len(mages)
cleric_len = len(clerics)
thief_len = len(thieves)
necro_len = len(necromancers)

print('There are %i Fighters.' % (fighter_len))
print('There are %i Mages.' % (mage_len))
print('There are %i Clerics.' % (cleric_len))
print('There are %i Thieves.' % (thief_len))
print('There are %i Necromancers.' % (necro_len))
print ('\n')
# asnwers for each below:
# fighters = 68
# mages = 108
# clerics = 75
# thieves = 51
# necromancers = 11


# ========== Q3 ==========

print('Q3: How many total items?')
items = Item.objects.all()
item_len = len(items)
print('There are %i total Items.' % (item_len))
print('\n')
# answer = 174

# ========== Q4 ==========

print('Q4: How many of the items are weapons?')
weapons = Weapon.objects.all()
weapon_len = len(weapons)
print('There are %i total Weapons.' % (weapon_len))
print('\n')
# answer 37

# ========== Q4 ==========

print('Q5: How many are not?')
item_len_excluding_weapons = len(items) - len(weapons)
print('There are %i Items which are not Weapons.' % (item_len_excluding_weapons))
print('\n')
# answer = 137

# ========== Q5 ==========

print('Q6: On average, how many items does each character have?')
count = 0
for char in characters:
    count += char.inventory.count()
avg_char_items = round(count/len(characters))
print('There are %i Items on average each Character carries.' % (avg_char_items))
print('\n')
# answer = 3, rounded to integer from 2.9

print('Q7: On average, how many weapons does each character have?')
count = 0
for char in characters:
    count += char.inventory.filter(item_id__range=(138, 174)).count()
avg_weapons_all_chars = round(count/len(characters))
# answer = 1, rounded to integer from 0.6
# !! NOTE: the answer for average weapons each weapon-yeilding character has
#          is diferent than the average of weapons among all characters
if (avg_weapons_all_chars == 1):
    print('There is %i Weapon on average each Character carries.' % (avg_weapons_all_chars))
    print('\n')
else:
    print('There are %i Weapons on average each Character carries.' % (avg_weapons_all_chars))
    print('\n')


# ========== ========== SQL ========== ==========

print('\n')
print('===== Django-II Sprint Challenge Answers using SQL =====')
print('\n')