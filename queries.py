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

#How many total Items?
#How many of the Items are weapons? How many are not?
#On average, how many Items does each Character have?
#On average, how many Weapons does each character have?
