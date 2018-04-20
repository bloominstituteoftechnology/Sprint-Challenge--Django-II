"""Total number of Characters"""
Character.objects.all().count()

"""Character count for each character type"""
Fighter.objects.all().count() 
Mage.objects.all().count() 
Cleric.objects.all().count() 
Thief.objects.all().count() 
Necromancer.objects.all().count() 


"""Count of total inventory"""
Item.objects.all().count()

"""Count of total Weapons"""
Weapon.objects.all()count()

"""Count of total Non-Weapons"""
Items.objects.all().count() - Weapon.objects.all().count()

"""On average, how many Items does each Character have?"""


