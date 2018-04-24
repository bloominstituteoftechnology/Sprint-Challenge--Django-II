# import aggregations from django.db.models
# from django.db.models import Count, Sum, Avg

# import all the models from charactercreator.models
# from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
# How many total Characters are there?
Character.objects.count() == 302
# How many of each specific subclass?
# Total fighter characters:
Fighter.objects.count() == 68

# Total mage characters:
Mage.objects.filter(necromancer__isnull=True).count() == 97

# Total cleric characters:
Cleric.objects.count() == 75

# Total thief characters:
Thief.objects.count() == 51

# Total necromancer characters:
Necromancer.objects.count() == 11


# import all the models from armory.models
# from armory.models import Item, Weapon
# How many total Items?
Item.objects.count() == 174

total_items = Character.objects.aggregate(total_items=Count('inventory'))[
    'total_items'] == 898

# How many of the Items are weapons? How many are not?
# weapons
Weapon.objects.count() == 37

total_weapons = Weapon.objects.aggregate(total_weapon=Count('character'))[
    'total_weapon'] == 203
# non-weapons
Item.objects.filter(weapon__isnull=True) == 137

Character.objects.aggregate(total_items=Count('inventory'))[
    'total_items'] - Weapon.objects.aggregate(total_weapon=Count('character'))[
    'total_weapon'] = 695

# On average, how many Items does each Character have?
Character.objects.all().annotate(count=Count('inventory')).aggregate(Avg('count'))
{'count__avg': 2.9735099337748343}

Character.objects.filter(
    inventory__isnull=False).count() / Character.objects.count()

Character.objects.aggregate(total_items=Count('inventory'))[
    'total_items'] / Character.objects.count() == 2.9735099337748343

# On average, how many Weapons does each character have?
Character.objects.all().annotate(count=Count(
    'inventory__weapon')).aggregate(Avg('count'))

Weapon.objects.aggregate(total_weapons=Count('character'))[
    'total_weapons'] / Character.objects.count() == 0.6721854304635762
