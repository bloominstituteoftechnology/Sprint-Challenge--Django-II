from django.db.models import Count, Sum, Avg
from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

# How many total Characters are there? 
Character.objects.count() # 302

# How many of each specific subclass?
Fighter.objects.count() # 68
len(Mage.objects.filter(necromancer__isnull=True)) # 97
Cleric.objects.count() # 75
Thief.objects.count() # 51
Necromancer.objects.count() # 11

# How many total Items?
Item.objects.count() # 174

# How many of the Items are weapons? 
Weapon.objects.count() # 37

# How many are not?
len(Item.objects.filter(weapon__isnull=True)) # 137

# On average, how many Items does each Character have?
Character.objects.all().annotate(count=Count('inventory')).aggregate(Avg('count')) # 2.9735099337748343

# On average, how many Weapons does each character have?
Character.objects.all().annotate(count=Count('inventory__weapon')).aggregate(Avg('count')) #0.6721854304635762