# How many total Characters are there?
>>> from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
>>> len(Character.objects.all())
302 Total



# How many of each specific subclass?
>>> len(Cleric.objects.all())
75

>>> len(Fighter.objects.all())
68

>>> len(Thief.objects.all())
51

>>> len(Necromancer.objects.all())
11

>>> Mage.objects.filter(necromancer__isnull=True).count()
97

# there are 302 total Characters, 108 are Mages, 11 of those 108 are Necros
# Necros count within the Mage count because they inherit from Mages. 


# How many total Items?
>>> len(Item.objects.all())
174



# How many of the Items are weapons? How many are not?
>>> len(Weapon.objects.all())
37 Weapons

# 174 - 37

137 Non Weapons



# On average, how many Items does each Character have?
>>> total_all_items = Character.objects.filter(inventory__isnull=False).count()
>>> total_characters = Character.objects.all().count()
>>> total_all_items / total_characters
2.9735099337748343



# On average, how many Weapons does each character have?
>>> total_weapons = Character.inventory.through.objects.filter(item_id__gt=137).count()
>>> total_weapons / total_characters
0.6721854304635762
