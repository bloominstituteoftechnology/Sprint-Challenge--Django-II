import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")

from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

# How many total Characters are there?
charCount = Character.objects.count()
print("The total count of characters in the database is ", charCount)

# How many of each specific subclass?
fighterCount = Character.objects.filter(fighter__isnull=True).count()
print("The total count of Characters with a subclass of Fighter is ", fighterCount)

mageCount = Character.objects.filter(mage__isnull=True).count()
print("The total count of Characters with a subclass of Mage is ", mageCount)

clericCount = Character.objects.filter(cleric__isnull=True).count()
print("The total count of Characters with a subclass of Cleric is ", clericCount)

thiefCount = Character.objects.filter(thief__isnull=True).count()
print("The total count of Characters with a subclass of Thief is ", thiefCount)

# How many total Items?
itemCount = Item.objects.count()
print("The total count of Items in the database is ", itemCount)

# How many of the Items are weapons? How many are not?
weaponCount = Weapon.objects.count()
print("The total count of Items that is a type of weapon in the database is ", weaponCount)

notweaponCount = itemCount - Weapon.objects.count()
print("The total count of Items that is not a type of weapon in the database is ", notweaponCount)

# On average, how many Items does each Character have?
avgItemPerChar = itemCount / charCount
print("The average count of Items to a Character is ", avgItemPerChar)

# On average, how many Weapons does each character have?
avgWeaponPerChar = weaponCount / charCount
print("The average count of Weapons to a Character is ", avgWeaponPerChar)

