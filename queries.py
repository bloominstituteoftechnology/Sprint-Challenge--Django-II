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

print(f"Number of Characters:........{character_count}")
print(f"Number of Fighters:..........{fighter_count}")
print(f"Number of Mages:.............{mage_count}")
print(f"Number of Clerics:...........{cleric_count}")
print(f"Number of Theifs:............{thief_count}")
print(f"Number of Necromancers:......{necromancer_count}")
print(f"Number of Items:.............{item_count}")
print(f"Number of Weapons:...........{weapon_count}")
print(f"Number of Non-Weapon Items:..{non_weapon_count}")
print(f"Average Items/Character:.....{average_items}")
print(f"Averate Weapons/Character:...{average_weapons}")
