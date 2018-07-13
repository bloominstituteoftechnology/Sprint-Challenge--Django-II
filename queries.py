How many total Characters are there? 302 list(Character.objects.all())

How many of each specific subclass?
from charactercreator.models import Cleric 74
list(Cleric.objects.all())
from charactercreator.models import Fighter 68
list(Fighter.objects.all())
from charactercreator.models import Mage 233
list(Mage.objects.all())
from charactercreator.models import Thief 50
list(Thief.objects.all())
from charactercreator.models import Necromancer 10
list(Necromancer.objects.all())

How many total Items?
from armory.models import Item
list(Item.objects.all()) 174
How many of the Items are weapons? How many are not?
from armory.models import Weapon 36
list(Weapon.objects.all())
On average, how many Items does each Character have?
On average, how many Weapons does each character have?