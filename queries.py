from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon
from django.db.models import Count, Avg

# How many total Characters are there?
Character.objects.all().count()
# 302 Characters

# How many of each specific subclass?
Fighter.objects.all().count()
# 68 Fighters
Mage.objects.all().count()
# 108 Mages
Cleric.objects.all().count()
# 75 Clerics
Thief.objects.all().count()
# 51 Theives
Necromancer.objects.all().count()
# 11 Necromancers

# How many total Items?
Item.objects.all().count()
# 174 Items

# How many of the Items are weapons? How many are not?
Weapon.objects.all().count()
# 37 Weapons
Item.objects.filter(weapon__isnull=True).count()
# 137 Items are NOT weapons

# On average, how many Items does each Character have?
Character.objects.all().annotate(count = Count('inventory')).aggregate(Avg('count'))
# count__avg': 2.9735099337748343

# On average, how many Weapons does each character have?
Character.objects.all().annotate(count = Count('inventory__weapon')).aggregate(Avg('count'))
# 'count__avg': 0.6721854304635762