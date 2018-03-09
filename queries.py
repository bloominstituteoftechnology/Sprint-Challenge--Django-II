 from charactercreator.models import Character, Cleric, Fighter, Mage, Thief, Necromancer>>> from armory.models import Item, Weapon

How many total Characters are there?
>>> Character.objects.all().count()
302

How many of each specific subclass?
>>> Cleric.objects.all().count()
75
>>> Fighter.objects.all().count()
68
>>> Mage.objects.all().count()
108
>>> Thief.objects.all().count()
51
>>> Necromancer.objects.all().count()
11
# there are 302 total Characters, 108 are Mages, 11 of those 108 are Necros
# Necros count within the Mage count because they inherit from Mages. 

# mages without the necromancer tag
>>> Mage.objects.filter(necromancer__isnull=True).count()
97

How many total Items?
# types of items
>>> Item.objects.all().count()
174
# total items across all characters
>>> Character.objects.filter(inventory__isnull=False).count()
898

How many of the Items are weapons? How many are not?
# types of items
>>> Weapon.objects.all().count()
37
# items without the weapons tag
>>> Item.objects.filter(weapon__isnull=True).count()
137

# total weapons across all characters
>>> Character.inventory.through.objects.filter(item_id__gt=137).count()
203

On average, how many Items does each Character have?
>>> total_all_items = Character.objects.filter(inventory__isnull=False).count()
>>> total_characters = Character.objects.all().count()
>>> total_all_items / total_characters
2.9735099337748343

On average, how many Weapons does each character have?
>>> total_weapons = Character.inventory.through.objects.filter(item_id__gt=137).count()
>>> total_weapons / total_characters
0.6721854304635762