
#How many total Characters are there? Total 302.
from charactercreater.models import Character
character = Character.objects.all()
character_count = characters.count()

#How many of each specific subclass?
from charactercreater.models import Fighter, Mage, Cleric, Thief, Necromancer 
Figher.objects.all().count()
#Total 68
Mage.objects.all().count()
#Total 108
Cleric.objects.all().count()
#Total 75
Thief.objects.all().count()
#Total 51
Necromancer.objects.all().count()
#Total 11


#How many total Items?
Item.objects.all().count()
#Total 174

#How many of the Items are weapons? How many are not?
Weapon.objects.all().count()
#Total 37
Item.objects.filter(weapon__isnull=True).count()
#Total 137

#On average, how many Items does each Character have?
items_average = totalItems/character_count
#On average, how many Weapons does each character have?
weapons_average = totalWeapons/character_count