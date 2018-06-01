# How many total characters?
from charactercreator.models import Fighter, Mage, Cleric, Thief, Necromancer, Character
from armory.models import Item, Weapon

print("\nTotal Characters?") #302
total_chars = Character.objects.all()
print("\nTotal characters: %d \n" % total_chars.count())

print("\nHow many of each class?")

total_Fighters = Fighter.objects.all().count()
print("\n Fighters: %d Fighters" % total_Fighters) #68

total_Mages = Mage.objects.all().count()
print("\n Mages: %d Mages" % total_Mages) #108

total_Clerics = Cleric.objects.all().count()
print("\n Clerics: %d Clerics" % total_Clerics) #75

total_Thiefs = Thief.objects.all().count()
print("\n There are %d Thiefs" % total_Thiefs) #51

total_Necromancers = Necromancer.objects.all().count()
print("\n There are %d Necromancers" % total_Necromancers) #11


all_items = Item.objects.all()
all_weapons = Weapon.objects.all()
items_nowep = all_items.count() - all_weapons.count()


# average items/ total items
total_characters = total_chars.count()

total_items = sum([character.inventory.count() for character in total_chars])
average_items = round(total_items/total_characters, 2)

total_weapons = sum([character.inventory.filter(weapon__isnull=False).count() for character in total_chars])
average_weapons = round(total_weapons/total_characters, 2)

print("\nTotal items?") # 174
print("\n%d total Items\n" % all_items.count())
print("\nItems are weapons? are not?") # 37 weapons 137 noweapons
print("\n%d Total Items, %d are Weapons, %d are not.\n" % (all_items.count(), all_weapons.count(), items_nowep))
print("\nOn average how many Items and Weapons does each Character have?") #2.9 Items 0.6 Weapons
print("\nOn average each Character has %f Items and %f Weapons.\n" % (average_items, average_weapons))
