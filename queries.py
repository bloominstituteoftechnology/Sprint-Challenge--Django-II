from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon
# How many total Characters are there? 302
print('Total characters: ', Character.objects.count())

# How many of each specific subclass?
#Fighter:68
print(Fighter.objects.count())
#Mages: 108
print(Mage.objects.count())
#Cleric: 75
print(Cleric.objects.count())
#thief: 51
print(Thief.objects.count())
#Necromancer: 11
print(Necromancer.objects.count())

#Item: 174
print(Item.objects.count())

#Weapon:37, Non-weapon items:X; X = 174 - 37 = 137
print(Weapon.objects.count())

#On average, how many Items does each Character have? 2.97
#On average, how many Weapons does each character have? 0.67

characters = Character.objects.all()
total_items=0
total_weapons=0
for character in characters:
    total_items += character.inventory.count()
    total_weapons += character.inventory.count() - character.inventory.filter(weapon=None).count()
print(total_items / Character.objects.count())
print(total_weapons / Character.objects.count())
