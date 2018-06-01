from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer  # noqa
from armory.models import Item, Weapon

# How many total Characters are there? 302
all_characters = Character.objects.all().count()

# How many of each specific subclass?
# Fighter = 68
# Mage = 108 - 11 (necromancer) = 97
# Cleric = 75
# Thief = 51
# Necromancer = 11
all_fighters = Fighter.objects.all().count()
all_mages = Mage.objects.all().count()
all_clerics = Cleric.objects.all().count()
all_thieves = Thief.objects.all().count()
all_necromancers = Necromancer.objects.all().count()

# How many total Items? 174
Item.objects.all().count()

# How many of the Items are weapons? 37
Weapon.objects.all().count()

# How many are not? 137
all_items = Item.objects.all().count()
all_weapons = Weapon.objects.all().count()
all_items - all_weapons

# On average, how many Items does each Character have? 2.9735099337748343  # noqa
total_items = sum([character.inventory.filter().count() for character in Character.objects.all()])  # noqa
total_items / all_characters

# On average, how many Weapons does each character have? 0.6721854304635762  # noqa
total_weapons = sum([character.inventory.filter(weapon__isnull=False).count() for character in Character.objects.all()])  # noqa
total_weapons / all_characters
