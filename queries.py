# 1. How many total Characters are there?
>>> from charactercreator.models import Fighter, Mage, Cleric, Thief, Necromancer, Character
>>> all_entries = Character.objects.all()
>>> all_entries.count()
#Answer is 302

# 2. How many of each specific subclass?
# Mage -- Necromancer is a subclass of Mage, and will need to be filtered out
>>> mage = Mage.objects.filter(necromancer__isnull=True)
>>> mage.count()
#97

#Clerics
>>> cleric = Cleric.objects.all()
>>> cleric.count()
##75

# Thieves
>>> thieves = Thief.objects.all()
>>> thieves.count()
#51

# Necromancers
>>> necromancer = Necromancer.objects.all()
>>> necromancer.count()
#11
# 3. How many total Items?
>>> from armory.models import Item, Weapon
>>> all_items = Item.objects.all()
>>> all_items.count()
#174

# 4. ow many of the Items are weapons? How many are not?
# Weapons
>>> Item.objects.filter(weapon__isnull=False).count()
#37
# Not weapons
>>> Item.objects.filter(weapon__isnull=True).count()
# 137

# 5. On average, how many Items does each Character have?
>>> Character.inventory.through.objects.filter(item_id__lt=137).count()
# 689
>>> Character.inventory.through.objects.filter(item_id__lt=137).count() / Character.objects.all().count()
# 2.281456953642384

# 6. On average, how many Weapons does each character have?

>>> Character.inventory.through.objects.filter(item_id__gt=137).count()
# 203

>>> Character.inventory.through.objects.filter(item_id__gt=137).count() / Character.objects.all().count()
#0.6721854304635762
