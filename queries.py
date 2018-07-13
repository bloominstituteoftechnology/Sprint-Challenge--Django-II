from charactercreator.models import Character
from charactercreator.models import Fighter
from charactercreator.models import Mage
from charactercreator.models import Cleric
from charactercreator.models import Thief
from charactercreator.models import Necromancer

Character.objects
all_characters = Character.objects.all()
all_characters

# query to count the characters
count_char = Character.objects.count()
count_char
302

# count each subclass charctaer by class and return sum
f = Fighter.objects.all().count()
f
68
m = Mage.objects.all().count()
c = Cleric.objects.all().count()
t = Thief.objects.all().count()
n = Necromancer.objects.all().count()
f + m + c + t + n

#how many total items
from armory.models import Item
item_count = Item.objects.count()
item_count
174

# how many are weapons and how many are not
from armory.models import Weapon
weapon_count = Weapon.objects.count()
weapon_count
37

174 - 37 = 137 # item that are not weapons

# avg items
item_avg = count_char / item_count

# avg weapons
weapon_avg = count_char / weapon_count
