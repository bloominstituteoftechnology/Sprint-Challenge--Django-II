from charactercreator.model import Character, Mage, Cleric, Fighter, Thief, Necromancer
from armory.models import Item, Weapon
from django.db.models import Count, Avg

# 1. How many total Characters are there?

Character.objects.count() # 302


# 2. How many of each specific subclass?

Mage.objects.count()        # 108 including necromancers, 97 without
Cleric.objects.count()      # 75
Fighter.objects.count()     # 68
Thief.objects.count()       # 51
Necromancer.objects.count() # 11 

# 3. How many total Items?

items = Item.objects.count() # 174

# 4. How many of the Items are weapons? How many are not?

weapons Weapon.objects.count() # 37

items - weapons # 137 items are not weapons

# 5. On average, how many Items does each Character have?

inv_items = [char.inventory.count() for char in Character.objects.all()] # number of items each character has in inventory
(sum(inv_items) / get_characters()) # 2.973 items per character

  # OR

Character.objects.all().annotate(avg_items = Count('inventory')).aggregate(Avg('avg_items')) # 2.9735099337748343

# 6. On average, how many Weapons does each character have?

Character.objects.all().annotate(avg_weapons = Count('inventory__weapon')).aggregate(Avg('avg_weapons')) # 0.6721854304635762
