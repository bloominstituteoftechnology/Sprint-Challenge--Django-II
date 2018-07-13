from charactercreator.models import *
from armory.models import *

"""
It's not pretty code... but they all work and I believe
they all return the correct numbers.
"""

# 1 - How many total Characters are there?
character_count = len(Character.objects.all())

# 2 = How many of each specific subclass?
fighter_count = len(Fighter.objects.all())
mage_count = len(Mage.objects.all())
cleric_count = len(Cleric.objects.all())
thief_count = len(Thief.objects.all())
necromancer_count = len(Necromancer.objects.all())

# 3 - How many total items?
item_count = len(Item.objects.all())

weapon_count = len(Weapon.objects.all())

non_weapon_count = len(Item.objects.filter(weapon=None))

# 4 - On average, how many iitems does each character have?
items = 0
characters = Character.objects.all()
for character in characters:
    items += len(character.inventory.all())

average_items = items / len(characters)


num_of_weapons = 0
for character in characters:
    num_of_weapons += (len(character.inventory.all()) -
                       len(character.inventory.filter(weapon=None)))

average_weapons = num_of_weapons / len(characters)
