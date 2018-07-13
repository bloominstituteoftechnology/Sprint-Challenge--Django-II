# Characters: 302
Character.objects.count()

# Fighters: 68
Fighter.objects.count()

# Mages: 108
Mage.objects.count()

# Clerics: 75
Cleric.objects.count()

# Thiefs: 51
Thief.objects.count()

# Necromancers: 11
Necromancer.objects.count()

# Items: 175
Item.objects.count()

# Weapons: 37
Weapon.objects.count()

# Non-weapons: 138
Item.objects.exclude(item_id__in=Weapon.objects.all()).count()

# Average items per character: 0.5794701986754967
Item.objects.count() / Character.objects.count()


# Average weapons per character: 0.12251655629139073
Weapon.objects.count() / Character.objects.count()


