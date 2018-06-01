from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

all_chars = Character.objects.all()

all_Fighters = Fighter.objects.all().count()
all_Mages = Mage.objects.all().count()
all_Clerics = Cleric.objects.all().count()
all_Thiefs = Thief.objects.all().count()
all_Necromancers = Necromancer.objects.all().count()

all_items = Item.objects.all()
all_weapons = Weapon.objects.all()
items_not_as_weapons = all_items.count() - all_weapons.count()

total_characters = all_chars.count()

total_items = sum([character.inventory.count() for character in all_chars])
average_items = round(total_items/total_characters, 2)

total_weapons = sum([character.inventory.filter(weapon__isnull=False).count() for character in all_chars])
average_weapons = round(total_weapons/total_characters, 2)

print("\nHow many total Characters are there?")
print("\nThere are %d total characters.\n" % all_chars.count())

print("\nHow many of each specific subclass?")
print("\n There are %d Fighters." % all_Fighters)
print("\n There are %d Mages." % all_Mages)
print("\n There are %d Clerics." % all_Clerics)
print("\n There are %d Thiefs." % all_Thiefs)
print("\n There are %d Necromancers.\n" % all_Necromancers)

print("\nHow many total Items?")
print("\nThere are %d total Items.\n" % all_items.count())

print("\nHow many of the Items are weapons? How many are not?")
print("\nOut of %d Items, %d are Weapons, and %d are not.\n" % (all_items.count(), all_weapons.count(), items_not_as_weapons))

print("\nOn average, how many Items and Weapons does each Character have?")
print("\nOn average, each Character has %f Items and %f Weapons.\n" % (average_items, average_weapons))
