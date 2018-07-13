import math
from django.db import models
from charactercreator.models import Character
from armory.models import Item
from armory.models import Weapon

characters = Character.objects.all()
items = Item.objects.all()
weapons = Weapon.objects.all()

# How many total characters are there?

# There are 302 characters.

total_characters = len(characters)

# How many of each specific subclass?

# There are four subclasses.

total_subclasses = len(Character.__subclasses__())

# How many total items? 

# The number of items is 174

total_items = len(items)

# How many items are weapons? How many are not?

# Weapons: 37
# Non-weapons: 137

weapon_count = len(weapons)
nonweapon_count = total_items - weapon_count

# On average, how many items does each character have?
# Average number of items: 3

character_item_count = 0

for character in range(total_characters):
    character_item_count += len(Item.objects.filter(character=character))

average_item_count = math.ceil(character_item_count / total_characters)

# On average, how many weapons does each character have?
# Average number of weapons: 1

character_weapon_count = 0

for character in range(total_characters):
    character_weapon_count += len(Weapon.objects.filter(character=character))

average_weapon_count = math.ceil(character_weapon_count / total_characters)
