from charactercreator.models import Character
from charactercreator.models import Fighter
from charactercreator.models import Mage
from charactercreator.models import Cleric
from charactercreator.models import Thief
from charactercreator.models import Necromancer
from armory.models import Item
from armory.models import Weapon

# How many total characters are there?
print('total # of characters is', Character.objects.all().count())

# fighters = 0
# mage = 0
# cleric = 0
# thief = 0
# necromancer = 0

# for e in Character.objects.all():
#     print(e)
#     if e.fighter: fighters += 1
#     elif e.mage: 
#         if e.mage.necromancer: necromancer += 1
#         else: mage +=1
#     elif e.cleric: cleric += 1
#     else: thief += 1

# print('# of fighters is', fighters)

# How many of each specific subclass?
print('total # of fighters is', Fighter.objects.all().count())
print('total # of mages is', Mage.objects.all().count())
print('total # of clerics is', Cleric.objects.all().count())
print('total # of thiefs is', Thief.objects.all().count())
print('total # of necromancers is', Necromancer.objects.all().count())

# How many total items
print('total # of items are', Item.objects.all().count())

# How many items are weapon? not weapons?
print('total # of weapons are', Weapon.objects.all().count())
print('total # of non-weapon items are', Item.objects.all().count() - Weapon.objects.all().count())

totalItems = 0
totalWeapons = 0
for e in Character.objects.all():
    totalItems += e.inventory.count()
    for i in e.inventory.values():
        if (i['item_id'] > 137): totalWeapons += 1

print('average # of items each character has is', totalItems / Character.objects.all().count())
print('average # of weapons each character has is', totalWeapons / Character.objects.all().count())