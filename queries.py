# Commands to create an object
# from charactercreator.models import <class>
# from armory.models import <class>
from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer

# Commands to figure out counts
# <class>.objects.count()
Character.objects.count() # 302
Fighter.objects.count() # 68
Mage.objects.count() # 108
Cleric.objects.count() # 75
Thief.objects.count() # 51
Necromancer.objects.count() # 11


# Python code to figure out averages
item_average = Item.objects.count() / Character.objects.count() # 0.5775577557755776
weapon_average = Weapon.objects.count() / Character.objects.count() # 0.12211221122112212