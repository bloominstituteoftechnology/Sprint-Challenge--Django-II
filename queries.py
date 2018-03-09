from django.db.models import Count, Avg
from charactercreator.models import *

1. all = Character.objects.all().count()

2. fighters = Fighter.objects.count()
    necros = Necromancer.objects.count()
    thieves = Thief.objects.count()
    clerics = Cleric.objects.count()
    mages = Mage.objects.count() - necros

3. items = Item.objects.count()

4. weapons = Weapon.objects.count()

5. allItems = Character.objects.filter(inventory__isnull=False).count()

6. allItems/all

7. Character.inventory.through.objects.filter(item_id__gt=137).count()/items
