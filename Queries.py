# 1: Characters: 302
Character.objects.count()

#2: Subclasses:

# Fighter: 68
Fighter.objects.count()

# Mage: 108
Mage.objects.count()

# Cleric: 75
Cleric.objects.count()

# Thief: 51
Thief.objects.count()

# Necromancer: 11
Necromancer.objects.count()

#3 Items: 174
Item.objects.count()

 
#4 Weapons: 37
Weapon.objects.count()

# Non-weapons: 137
Item.objects.exclude(item_id__in=Weapon.objects.all()).count()

#5 Average items per character: 2.9735
Character.objects.all().annotate(items=models.Count('inventory')).aggregate(models.Avg('items'))

#6 Average weapons per character: 1.1666 
Character.objects.values('inventory').annotate(items=models.Count('inventory', filter=models.Q(inventory__in=Weapon.objects.all()))).aggregate(models.Avg('items'))
 