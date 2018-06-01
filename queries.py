from charactercreator.models import Character
from charactercreator.models import Fighter
from charactercreator.models import Mage
from charactercreator.models import Cleric
from charactercreator.models import Thief
from charactercreator.models import Necromancer
from armory.models import Item
from armory.models import Weapon

# How many total characters are there?
print('total # of characters is', Character.objects.all().count())

# How many of each specific subclass?
fighters = Fighter.objects.all().count()
print('total # of fighters is', Fighter.objects.all().count())
mages = Mage.objects.all().count()
print('total # of mages is', Mage.objects.all().count())
clerics = Cleric.objects.all().count()
print('total # of clerics is', Cleric.objects.all().count())
thieves: Thief.objects.all().count()
print('total # of thiefs is', Thief.objects.all().count())
necromancers = Necromancer.objects.all().count()
print('total # of necromancers is', Necromancer.objects.all().count())

# How many total items
print('total # of items are', Item.objects.all().count())

# How many items are weapon? not weapons?
print('total # of weapons are', Weapon.objects.all().count())
print('total # of non-weapon items are', Item.objects.all().count() - Weapon.objects.all().count())