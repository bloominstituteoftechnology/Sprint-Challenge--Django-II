from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

print("\nHow many total Characters are there?")
Character.objects.all().count()

all_Fighters = Fighter.objects.all().count()
all_Mages = Mage.objects.all().count()
all_Clerics = Cleric.objects.all().count()
all_Thiefs = Thief.objects.all().count()
all_Necromancers = Necromancer.objects.all().count()

print("\nHow many of each specific subclass?")
print("\n There are %d Fighters" % all_Fighters)
print("\n There are %d Mages" % all_Mages)
print("\n There are %d Clerics" % all_Clerics)
print("\n There are %d Thiefs" % all_Thiefs)
print("\n There are %d Necromancers" % all_Necromancers)

all_items = Item.objects.all().count()
print("\nHow many total Items?")
all_items
items_as_weapons = all_items - Weapon.objects.all().count()
print("\nHow many of the Items are weapons? How many are not?")
Weapon.objects.all().count()
items_as_weapons


Characters = Character.objects.all()
total_Items = sum([character.inventory.count() for character in Characters])
total_Characters = Character.objects.all().count()
total_Items/total_Characters
print("\nOn average, how many Items does each Character have?")
round(total_Items/total_Characters, 2)

total_Weapons = sum([character.inventory.filter(weapon__isnull=False).count() for character in Characters])
total_Characters = Character.objects.all().count()
average_weapons = total_Weapons/total_Characters
print("\nOn average, how many Weapons does each character have?")
round(total_Weapons/total_Characters, 2)
