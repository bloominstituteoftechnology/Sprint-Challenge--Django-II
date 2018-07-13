# How many total Characters are there?
from charactercreator.models import Character
Character.objects.count()

# How many of each specific subclass?
from charactercreator.models import Cleric
Cleric.objects.count()

from charactercreator.models import Fighter
Fighter.objects.count()

from charactercreator.models import Mage
Mage.objects.count()

from charactercreator.models import Necromancer
Necromancer.objects.count()

from charactercreator.models import Thief
Thief.objects.count()

# How many total Items?
from armory.models import Item
Item.objects.count()

# How many of the Items are weapons?
from armory.models import Weapon
Weapon.objects.count()

# How many are not?


# On average, how many Items does each Character have?


# On average, how many Weapons does each character have?

