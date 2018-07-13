from charactercreator.models import *
from armory.models import *


1. How many total Characters are there? 
 Character.objects.count()
 Answer: 302


2. How many of each specific subclass?

#Class Fighter
Fighter.objects.count()
Answer:68

#Class Mage
Mage.objects.count()
Answer:108

#Class Cleric
Cleric.objects.count()
Answer:75

#Class Thief
Thief.objects.count()
Answer:51

#Class Necromancer
Necromancer.objects.count()
Answer:11


3. How many total Items? 
Item.objects.count()
Answer: 174

4. How many of the Items are weapons? How many are not?
Weapon.objects.count()
Answers:37

Item.objects.filter(weapon=None).count()
Answer:137

5. On average, how many Items does each Character have?
Character.objects.all().annotate(count = models.Count('inventory')).aggregate(models.Avg('count'))
Answer: {'count__avg': 2.9735099337748343}

6. On average, how many Weapons does each character have?
Character.objects.all().annotate(count = models.Count('inventory__weapon')).aggregate(models.Avg('count'))
Answer: {'count__avg': 0.6721854304635762}

