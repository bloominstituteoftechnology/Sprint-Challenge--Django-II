from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

#How many total Characters are there?
Character.objects.all().count() #302

# How many of each specific subclass?
Fighter.objects.all().count() #68
Mage.objects.all().count() - Necromancer.objects.all().count() #97
Cleric.objects.all().count() #75
Thief.objects.all().count() #51
Necromancer.objects.all().count() #11

# How many total Items?
Item.objects.all().count() #174

# How many of the Items are weapons? 
Weapon.objects.all().count() #37
# How many are not?
Item.objects.all().count() - Weapon.objects.all().count() #137

# On average, how many Items does each Character have?
Characters = Character.objects.all()
total_Items = sum([character.inventory.count() for character in Characters])
total_Characters = Character.objects.all().count()
total_Items/total_Characters #2.9735099337748343

# On average, how many Weapons does each character have?
Characters = Character.objects.all()
total_Weapons = sum([character.inventory.filter(weapon__isnull=False).count() for character in Characters])
total_Characters = Character.objects.all().count()
total_Weapons/total_Characters #0.6721854304635762
