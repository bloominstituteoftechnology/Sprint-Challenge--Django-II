from django.db.models import Count, Avg
from charactercreator.models import *
from armory.models import Item, Weapon

numberOfCharacters = Character.objects.all().count()
fighters = Fighter.objects.count()
necros = Necromancer.objects.count()
thieves = Thief.objects.count()
clerics = Cleric.objects.count()
mages = Mage.objects.count() - necros
weapons = Weapon.objects.count()
charactersWithItems = Character.objects.filter(inventory__isnull=False)

totalWeapons = 0
for a in charactersWithItems:
    totalWeapons += a.inventory.filter(item_id__gt=137).count()
    print("weapon counts", totalWeapons)

totalItems = 0
for a in charactersWithItems:
    totalItems += a.inventory.count()
    print("item counts", totalItems)

print("Total # characters", numberOfCharacters)
# 302
print("Total # fighters", fighters)
# 68
print("Total # necros", necros)
# 11
print("Total # thieves", thieves)
# 51
print("Total # clerics", clerics)
# 75
print("Total # items", totalItems)
# 3286
print("Total # weapons", totalWeapons)
# 743
print("Total # of non-weapon items", totalItems - totalWeapons)
# 2543
print("Average # of Items each character has", totalItems/numberOfCharacters)
# 10.880794701986755
print("Average # of Weapons each character has", totalWeapons/numberOfCharacters)
# 2.4602649006622515
