from charactercreator.models import *
from armory.models import *
from django.db.models import Count
from django.db.models import Avg


Total = Character.objects.count()
print('How many total characters?', Total)

totalItems = Item.objects.count()
print('How many total Items?', totalItems)

Fighters = Fighter.objects.count()
print(Fighters)

Mages = Mage.objects.count()
print(Mages)

Clerics = Cleric.objects.count()
print(Clerics)

Thieves = Thief.objects.count()
print(Thieves)

Necromancers = Necromancer.objects.count()
print(Necromancers)

print('How many of each specific subclass?', Fighters + Mages + Clerics + Thieves + Necromancers)

Weapons = Weapon.objects.count()
print(Weapons)

print('How many of the Items are weapons?', Weapons, 'How many are not?', totalItems - Weapons)

print('On average, how many Items does each Character have?', Item.objects.aggregate(Avg('character')))

print('On average, how many Weapons does each Character have?', Weapon.objects.aggregate(Avg('character')))