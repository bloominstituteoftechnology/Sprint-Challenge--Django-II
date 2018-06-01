# import all the models
from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

# - How many total Characters are there? ***********************
#  there are 302 total characters
characters = Character.objects.all()
len(characters)

# - How many of each specific subclass? ************************
# 68 fighters, 108 Mage, 75 Cleric, 51 Thief, 11 Necromancer
len(Fighter.objects.all())
len(Mage.objects.all())
len(Cleric.objects.all())
len(Thief.objects.all())
len(Necromancer.objects.all())

# - How many total Items? **************************************
#  there are 174 items
items = Item.objects.all()
len(items)

# - How many of the Items are weapons? How many are not? ********
#  There are 37 weapons
weapons = Weapon.objects.all()
len(weapons)

# - On average, how many Items does each Character have?* *******
#  average of 2.9735099337748343 items
total_items = 0
for char in characters:
	# get inventory for each character
	inventory = char.inventory.all()
	# add the lenght of item in inventory to total items
	total_items += len(inventory)

average_items = total_items / len(characters)

# - On average, how many Weapons does each character have? ******
# average of 0.6721854304635762 weapons
total_weapons = 0
for weapon in weapons:
	# get the number of characters who owns this weapon
	# and add it to total_weapons
	total_weapons += weapon.character_set.count()

average_weapons = total_weapons / len(characters)
