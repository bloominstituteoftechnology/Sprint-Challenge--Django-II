# 01. Total number of characters: 302
from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
Character.objects.all().count()


# 02. Total number of subclasses:

#  a. Fighter:      68
Fighter.objects.all().count()

#  b. Mage:         108
Mage.objects.all().count()

#  c. Cleric:       75
Cleric.objects.all().count()

#  d. Thief:        51
Thief.objects.all().count()

#  e. Necromancer:  11
Necromancer.objects.all().count()


# 03. Number of Total Items: 174
from armory.models import Item, Weapon
Item.objects.all().count()


# 04a: Number of Weapon Items: 37
Weapon.objects.all().count()
# 04b. Number of Non-Weapon Items: 137
###### Subtracted


# 05. Average number of Items each Character has: 
#     I attempted:
inventory.objects.all().count()
Character.objects.filter(inventory_isnull=False).count()
Character.objects.filter(inventory_isnull=False)
all_items = Character.objects.filter(inventory_isnull=False).count()
all_items = Character.objects.filter(inventory_isnull=True).count()
Item.objects.all().count()
Item.objects.all().name()
Item.objects.all().average()
Item.objects.get(id)
Item.objects.in_bulk()
# I honestly don't know how to do parts 5 & 6. I'm going to push and stop and wait for the solution lecture.


# 05. Average number of Weapons each Character has:
