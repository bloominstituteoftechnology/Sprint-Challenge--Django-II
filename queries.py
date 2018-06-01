#Imports:
from armory.models import Weapon, Item
from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer

# How many total Characters are there?
print('There are %i total Characters.' % len(Character.objects.all())) # 302

# How many of each specific subclass?
print('There are %i Fighters.' % len(Fighter.objects.all())) # 68
print('There are %i Mages.' % len(Mage.objects.all())) # 108
print('There are %i Clerics.' % len(Cleric.objects.all())) # 75
print('There are %i Thieves.' % len(Thief.objects.all())) # 51
print('There are %i Necromancers.' % len(Necromancer.objects.all())) # 11

# How many total Items?
print('There are %i Unique Items.' % len(Item.objects.all())) #174

# How many of the Items are weapons? How many are not?
notWeapons = len(Item.objects.all()) - len(Weapon.objects.all())
print('%i of those items are Weapons, %i are not.' % (len(Weapon.objects.all()), notWeapons)) # 37, 137

# On average, how many Items does each Character have?
sum = 0
for char in Character.objects.all():
  sum += len(char.inventory.all()) # 898
average = sum / len(Character.objects.all()) # 898 / 302 = 2.9735099337748343
print('On average, each character has %s items' % average)

# On average, how many Weapons does each character have?
weaponSum = 0
# object ids go from 138 to 174
for char in Character.objects.all():
  weaponSum += len(char.inventory.filter(pk__in=range(138,175))) # 203
weaponAvg = weaponSum / len(Character.objects.all()) # 203 / 302 = 0.6721854304635762
print('On average, each character has %s weapons' % weaponAvg)
