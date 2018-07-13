'''
1. Get All Characters 

    from charactercreator.models import *
    charactors = Character.objects.all()
    len(charactors) = 302

2. Get Sub Classes

    fighter = Fighter.objects.all()
    len(fighter) = 68

    mages = Mage.objects.all()
    len(mages) = 108

    cleric = Cleric.objects.all()
    len(cleric) = 75

    thief = Thief.objects.all()
    len(thief) = 51

    necromancer = Necromancer.object.all()
    len(necromancer) = 11

3. Get Items 

    from armory.models import *
    items = Item.objects.all()
    len(items) = 174

4.  Get Weapons

    weapons = Weapons.objects.all()
    len(weapons) = 37
    are not weapons = 137

5.  average of items for each characters

        item_count = 0

        for char in character:
            count += char.inventory.count()

        print(count) = 898

        item_avg = count/len(characters) ~ 3 (2.97)

6.  average of weapons for each characters

        weapon_count = 0

        for char in character:
            count += char.inventory.filter(item_id__range=(138,174).count()

        print(count) = 203

        weapons_avg = count/len(characters) ~ 1 (.67)

'''
