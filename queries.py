
from charactercreator.models import Character
''# How many total Characters are there?
'Total Number of character in our api ='
len(Character.objects.all())
# How many of each specific subclass?
from django.db import models
#save for later..I know there is a way to query a list of characters subclasses, I just can't figure out the syntax for that
#charactercreator(models.Model.all())
#There are 5 Subclasesses of character that we see in models.py
from armory.models import Item
from armory.models import Weapon

'Total Number of Items ='
len(Item.objects.all())

len(Weapon.objects.all())
'Are Weapons'
#couldn't get the filter syntax to work so I just put in a simple equation

'This many Items are not ='
(len(Item.objects.all()) - len(Weapon.objects.all()))

'On Average, Each Character has '
(len(Item.objects.all()) / len(Character.objects.all()))
'Items'

'On Average, Each Character has '
(len(Weapon.objects.all()) / len(Character.objects.all()))
'Weapons'