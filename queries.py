from charactercreator.models import *
from armory.models import *

#Your main goal is to write Python code that uses the Django ORM to answer:

# How many total Characters are there?
Character.objects.count()
302
#How many of each specific subclass?
Fighter.objects.count()
#Fighter = 68
Mage.objects.count()
#Mage = 108
Cleric.objects.count()
#Cleric = 75
Thief.objects.count()
#Thief = 51
Necromancer.objects.count()
#Necromancer= 11
- How many total Items?
Item.objects.count()
#174
- How many of the Items are weapons? How many are not?
Weapon.objects.count()
#Weapon = 37
#Not Weapon= 137
Item.objects.filter(Weapon=none).count()
- On average, how many Items does each Character have?
Character.objects.all().annotate(count=models.Count('inventory')).aggregate(models.Avg('count'))
{'count__avg': 2.9735099337748343}
- On average, how many Weapons does each character have?
Character.objects.all().annotate(count=models.Count('inventory__weapon')).aggregate(models.Avg('count'))
{'count__avg': 0.6721854304635762}