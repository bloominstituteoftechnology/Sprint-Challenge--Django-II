
def run():
    from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
    from armory.models import Item, Weapon
    items_count = Item.objects.count()
    weapons_count = Weapon.objects.count()
    print('total Characters: %i' % (Character.objects.count()))
    print('total Fighters: %i' % (Fighter.objects.count()))
    print('total Mages: %i' % (Mage.objects.count()))
    print('total Clerics: %i' % (Cleric.objects.count()))
    print('total Thiefs: %i' % (Character.objects.count()))
    print('total Necromancers: %i' % (Necromancer.objects.count()))
    print('total Items: %i' % (items_count))
    print('total Weapons: %i' % (weapons_count))
    print('total Items not Weapons: %i' % (items_count - weapons_count))   
    icount = 0
    wcount = 0
    for c in Character.objects.all():
        icount += c.inventory.count()
        wcount += c.inventory.exclude(weapon=None).count()
    
    print('average number of Items per Character %f' % (icount/items_count))
    print('average number of Weapons per Character %f' % (wcount/items_count))

"""
total Characters: 302
total Fighters: 68
total Mages: 108
total Clerics: 75
total Thiefs: 302
total Necromancers: 11
total Items: 174
total Weapons: 37
total Items not Weapons: 137
average number of Items per Character 5.160920
average number of Weapons per Character 1.166667
"""

