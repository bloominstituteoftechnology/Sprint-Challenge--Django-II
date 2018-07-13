from charactercreator.models import *
from armory.models import * 

#How many total Characters are there? 302
Character.objects.count()

#How many of each specific subclass? 68 , 108, 75, 51, 11 

Fighter.objects.count()
Mage.objects.count()
Cleric.objects.count()
Thief.objects.count()
Necromancer.object.count()

#How many total items? 174

items.objects.count() 

#or could you do 
Character.inventory.count()

#How many of the Items are weapons? How many are not? 37, 
Weapons.objects.count()

Items.objects.exclude(Item ='Weapon').count()

#On average, how many Items does each Character have?

Character.objects.all().aggregate(Avg('Items'))

#On average, how many Items does each Character have?
