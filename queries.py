# python manage.py shell
from charactercreator.models import *
from armory.models import *

# How many total Characters are there?
char_count = Character.objects.count()
char_count # Returns 302

# How many of each specific subclass?
# CONSOLIDATE TO SINGLE QUERY
fighter_count = Fighter.objects.count()
fighter_count # returns 68

thief_count = Thief.objects.count()
thief_count # returns 51

necromancer_count = Necromancer.objects.count()
necromancer_count # returns 11

mage_count = Mage.objects.count()
mage_count # returns 108

cleric_count = Cleric.objects.count()
cleric_count # returns 75

# How many total Items?
item_count = Item.objects.count() 
item_count # returns 174

# How many of the Items are weapons? How many are not?
weapon_count = Weapon.objects.count()
weapon_count # returns 37
non_weapons = item_count - weapon_count
non_weapons # returns 137

# On average, how many Items does each Character have?
sum = 0
characters = Character.objects.all()
for character in characters:
  sum += character.inventory.count()
avg_items = sum/char_count
avg_items # returns 2.97

# On average, how many Weapons does each character have?
# cross check character inventory IDs against the weapon model 
all_weapons = Weapon.objects.all()
weapons_list = []
for weapon in all_weapons:
  weapons_list.append(weapon.item_id)
