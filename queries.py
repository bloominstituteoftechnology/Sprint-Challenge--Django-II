I first opened up the django shell and did:
    from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer

1. There are 302 total Characters
query is:
Character.objects.all().count()

** There is probably a better way to aggregate this but I wasn't sure. I used the same query for each character type just replace 'Fighter' with the other type
2. Fighter.objects.all().count()
    68 Fighters
    108 Mages
    75 Clerics
    51 Theives
    11 Necromancers

I did from armory.models import Item, Weapon
3. Item.objects.all().count()
    174 items

4. Weapon.objects.all().count()
    37 weapons

5. I first did from django.db.models import Avg
    Character.objects.all().aggregate(Avg('inventory'))
{'inventory__avg': 89.17817371937639}
