from charactercreator.models import Character
from armory.models import Item, Weapon

print('There are', Character.objects.count(), 'total characters')

from charactercreater.models import Mage
print('There are', Mage.objects.count(), 'total Mages')

from charactercreater.models import Necromancer
print('There are', Necromancer.objects.count(), 'total Necromancers')

from charactercreater.models import Fighter
print('There are', Fighter.objects.count(), 'total Fighters')

from charactercreater.models import Cleric
print('There are', Cleric.objects.count(), 'total Clerics')

from charactercreater.models import Thief
print('There are', Thief.objects.count(), 'total Thieves')

items = Item.objects.count()
weapons = Weapon.objects.count()
print('There are', Item.objects.count(), 'total items')
print('There are', Weapon.objects.count(), 'total items that are weapons')
print('Of all the', items, 'items', items - weapons, 'are not weapons')

