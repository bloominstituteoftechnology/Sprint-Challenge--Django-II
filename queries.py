from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

# How many total Characters are there?
characterCount = Character.objects.all().count() # characterCount = 302
print("There are total %d Characters" %characterCount)

# How many of each specific subclass?
fighterCount = Fighter.objects.count() #fighterCount = 68
print("There are %d fighters" %fighterCount)

mageCount = Mage.objects.count() # mageCount = 108
print("There are %d Mages" %mageCount)

clericCount = Cleric.objects.count() # clericCount = 75
print("There are %d Clerics" %clericCount)

thiefCount = Thief.objects.count() # thiefCount = 51
print("There are %d thiefs" %thiefCount)

necromancerCount = Necromancer.objects.count() # necromancerCount = 11
print("There are %d necromancers" %necromancerCount)

# How many total Items?
totalItems = Item.objects.count() # totalItems = 174
print("There are total %d Items" %totalItems)

# How many of the Items are weapons? How many are not?
weaponsCount = Weapon.objects.count() # weaponsCount = 37
nonWeaponsCount = totalItems - weaponsCount # nonWeaponsCount = 137
print("There are %d weapons and %d non-weapons" %(weaponsCount, nonWeaponsCount)

# On average, how many Items does each Character have?
ItemsPerCharacter = totalItems / characterCount # ItemsPerCharacter = 0.58
print("There are %.2f Items per character" %ItemsPerCharacter)

# On average, how many Weapons does each character have?
weaponsPerCharacter = weaponsCount / characterCount # weaponsPerCharacter = 0.12
print("There are %.2f Weapons per character" %ItemsPerCharacter)