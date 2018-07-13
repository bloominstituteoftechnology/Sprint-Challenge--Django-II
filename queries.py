Characters:
    Character.objects.count()
    # Answer: 302
Fighter:
    Fighter.objects.count()
    # Answer: 68
Mage:
    Mage.objects.count()
    # Answer: 108
Cleric:
    Cleric.objects.count()
    # Answer: 75
Thief:
    Thief.objects.count()
    # Answer: 51
Necromancer:
    Necromancer.objects.count()
    # Answer: 11
Items:
    Item.objects.count()
    # Answer: 174
Weapons:
    Weapon.objects.count()
    # Answer: 37
Not Weapons:
    Item.objects.exclude(weapon__isnull=False).count()
    # Answer: 137
Average Items per Character:
    characters = (Character.objects.all())
    average = 0
    for character in characters:
        average += character.inventory.count()

    print(average / Character.objects.count())
    # Answer: 2.9735099337748343
Average Weapons per Character:
    characters = Character.objects.all()
     weapons = 0
    for character in characters:
        weapons = character.inventory.exclude(weapon__isnull=False).count()

    print(weapons / Character.objects.count())
    # Answer: 0.013245033112582781