from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

## How many total Characters are there?
characters = Character.objects.all()
char_result = len(characters)
print("There are", char_result, "characters in total")

""" There are 302 total characters """

## How many of each specific subclass?
print("There are", len(Fighter.objects.all()), "fighters in total")
print("There are", len(Mage.objects.all()), "mages in total")
print("There are", len(Cleric.objects.all()), "clerics in total")
print("There are", len(Thief.objects.all()), "thieves in total")
print("There are", len(Necromancer.objects.all()), "necromancers in total")

"""
68 fighters
108 mages
75 clerics
51 thieves
11 necromancers
*** note that the total here is 313, because necromancers are mages, which have also been counted ***
"""

## How many total Items?
items = Item.objects.all()
item_result = len(items)
print("There are", item_result, "items in total")

""" There are 174 total items """

## How many of the Items are weapons? How many are not?
weapons = Weapon.objects.all()
weapon_result = len(weapons)
print("There are", weapon_result, "weapons in the items")
print(item_result - weapon_result, "of the items are not weapons")

""" There are 37 weapons in the items """
""" 137 of the items are not weapons """

## On average, how many Items does each Character have?
item_total = 0
for char in characters:
    item_total += len(char.inventory.all())
print ("On average each character has", item_total / char_result, "items")

""" Each character has on average 2.97 items...unsure if the average meant the rounded average so I just did it like this """

## On average, how many Weapons does each character have?
weapon_total = 0
for char in characters:
    weapon_total += len(char.inventory.filter(weapon__isnull=False))
print ("On average each character has", weapon_total / char_result, "weapons")

""" Each character has on average 0.67 weapons, perhaps because all characters do not carry a weapon """