from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon
from django.db.models import Avg


1.
Character.objects.count()
# 302


2. 
Fighter.objects.all().count()
Mage.objects.all().count()
Cleric.objects.all().count()
Thief.objects.all().count()
Necromancer.objects.all().count()

# fighter: 68
# mage: 108
# cleric: 75
# thief: 51
# mecromancer: 11


3. 
Item.objects.all().count()
# 174


4.
Item.objects.filter(weapon__isnull=False).count()
# 37
Item.objects.filter(weapon__isnull=True).count()
# 137



5.
Character.objects.aggregate(Avg('inventory'))
# {'inventory__avg': 89.17817371937639}


6. 

