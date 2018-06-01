# - How many total Characters are there?
from charactercreator.models import Character
print(Character.objects.count())
# Returns: 302

# - How many of each specific subclass?
from charactercreator.models import Fighter, Mage, Cleric, Thief, Necromancer
print(Fighter.objects.count())
# Returns: 68
print(Mage.objects.count())
# Returns: 108
print(Cleric.objects.count())
# Returns: 75
print(Thief.objects.count())
# Returns: 51
print(Necromancer.objects.count())
# Returns: 11

# - How many total Items?
from armory.models import Item
print(Item.objects.count())
# Returns: 174

# - How many of the Items are weapons? How many are not?
from armory.models import Weapon
print(Weapon.objects.count())
# Returns: 37 - Items are Weapons
print(Item.objects.count() - Weapon.objects.count())
# Returns: 137 - Items are not Weapons

# - On average, how many Items does each Character have?
totalChars = Character.objects.count()
# Returns: 302
totalItems = sum([char.inventory.count() for char in Character.objects.all()])
# Returns: 898
print('On average, each Character has %f items' % (totalItems/totalChars))
# 898 / 302 ~ 2.97

# - On average, how many Weapons does each character have?
chars_count = Character.objects.count()
# Returns: 302
weapon_count = sum([character.inventory.filter(weapon__isnull=False).count() for character in Character.objects.all()])
# Returns: 203
print('On average, each character has %f weapons' % (weapon_count/chars_count))
# 203 / 302 ~ 0.67