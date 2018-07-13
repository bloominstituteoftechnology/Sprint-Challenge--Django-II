from characterscreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

# How many characters are there?
list(Character.objects.all())
# Returns 302

#How many of each Specific subclass?
list(Fighter.objects.all())
# Returns 68 Fighters
list(Mage.objects.all())
# Returns 233 Mages
list(Cleric.objects.all())
# Returns 74 Clerics
list(Thief.objects.all())
# Returns 50 Thieves
list(Necromancer.objects.all())
# Returns 10 Nacromancers

#How many total Items?
list(Item.objects.all())
# Returns 174 items

#How many total Items are Weapons?
list(Weapon.objects.all())
# Returns 36 Items are weapons
