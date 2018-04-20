from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

# How many total characters are there? (Answer: 302)
Character.objects.all().count()

# How many of each specific subclass?
Fighter.objects.all().count() # (Answer: 68)

Cleric.objects.all().count() # (Answer: 75)

Thief.objects.all().count() # (Answer: 51)

Necromancer.objects.all().count() # (Answer: 11)

Mage.objects.filter(necromancer__isnull=True).count() # (Answer: 108)

# How many total items? (Answer: 174)
Item.objects.all().count()

# How many items are weapons? How many are not? (Answers: 37 are, 137 are not)
Weapon.objects.all().count()

Item.objects.filter(weapon_isnull=True).count()

# On average, how many Items does each Character have? (Answer: 2.9735099337748343)
all_items = Character.objects.filter(inventory_isnull=False).count()
all_characters = Character.objects.all().count()
all_items / all_characters

# On average, how many Weapons does each Character have? (Answer: 0.6721854304635762)
all_weapons = Character.inventory.through.objects.filter(item_id_gt=137).count()
all_weapons / all_characters