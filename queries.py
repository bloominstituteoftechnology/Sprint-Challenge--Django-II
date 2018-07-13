from charactercreator.models import Character
# How many total Characters are there?
    characters = Character.objects.all()
    character_count = characters.count()
    # Answer: 302

from charactercreator.models import Fighter, Mage, Cleric, Thief, Necromancer
# How many of each specific subclass?
    # Fighter
    Fighter.objects.all().count()
        # Answer: 68
    # Mage
    Mage.objects.all().count()
        # Answer: 108
    # Cleric
    Cleric.objects.all().count()
        # Answer: 75
    # Thief
    Thief.objects.all().count()
        # Answer: 51
    # Necromancer
    Necromancer.objects.all().count()
        # Answer: 11

from armory.models import Item, Weapon
# How many total Items?
    Item.objects.all().count()
    # Answer: 174
# How many of the Items are weapons?
    Weapon.objects.all().count()
    # Answer: 37
    # How many are not?
    Item.objects.filter(weapon__isnull=True).count()
    # Answer: 137

# On average, how many Items does each Character have?
    totalItems = 0
    totalWeapons = 0
    for character in characters:
        totalItems += character.inventory.count()
        totalWeapons += character.inventory.filter(weapon__isnull=False).count()

    item_average = totalItems/character_count
    # Answer: 2.9735099337748343
    
# On average, how many Weapons does each character have?
    weps_average = totalWeapons/character_count
    # Answer: 0.6721854304635762

""" From solution lecture discussion """    
# from django.db.models import Count, Avg, Sum
# counting = characters.annotate(count=Count('inventory')).aggregate(Sum('count'))
# 898
# counting = characters.annotate(count=Count('inventory')).aggregate(Avg('count'))

# counting = characters.annotate(count=Count('inventory__weapon')).aggregate(Avg('count'))
