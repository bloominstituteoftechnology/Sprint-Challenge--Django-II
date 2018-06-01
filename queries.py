- How many total Characters are there? 302
"""
>>> from charactercreator.models import Character
>>> Character.objects
<django.db.models.manager.Manager object at 0x10df58198>
>>> all_entries = Character.objects.all()
>>> all_entries
<QuerySet [<Character: Character object (1)>, <Character: Character object (2)>, <Character: Character object (3)>, <Character: Character object (4)>, <Character: Character object (5)>, <Character: Character object (6)>, <Character: Character object (7)>, <Character: Character object (8)>, <Character: Character object (9)>, <Character: Character object (10)>, <Character: Character object (11)>, <Character: Character object (12)>, <Character: Character object (13)>, <Character: Character object (14)>, <Character: Character object (15)>, <Character: Character object (16)>, <Character: Character object (17)>, <Character: Character object (18)>, <Character: Character object (19)>, <Character: Character object (20)>, '...(remaining elements truncated)...']>
>>> all_entries.count()
302
"""

- How many of each specific subclass?
Fighter = 68
Mage = 108
Cleric = 75
Thief = 51
Necromancer = 11
"""
>>> from charactercreator.models import Fighter, Mage, Cleric, Thief, Necromancer  # noqa
>>> all_fighters = Fighter.objects.all()
>>> all_mages = Mage.objects.all()
>>> all_clerics = Cleric.objects.all()
>>> all_thieves = Thief.objects.all()
>>> all_necromancers = Necromancer.objects.all()
>>> all_fighters.count()
68
>>> all_mages.count()
108
>>> all_clerics.count()
75
>>> all_thieves.count()
51
>>> all_necromancers.count()
11
"""

- How many total Items? 174
"""
>>> from armory.models import Item, Weapon
>>> Item.objects.all().count()
174
"""

- How many of the Items are weapons? 37. How many are not? 174 (num of Item) - 37 (num of Weapon) = 137  # noqa
"""
>>> Weapon.objects.all().count()
37
"""

- On average, how many Items does each Character have? 898 / 302 (num of characters) = 2.9735  # noqa
"""
>>> sum([character.inventory.filter().count() for character in Character.objects.all()])  # noqa
898
"""

- On average, how many Weapons does each character have? 203 / 302 (num of characters) = 0.6721  # noqa
"""
>>> sum([character.inventory.filter(weapon__isnull=False).count() for character in Character.objects.all()])  # noqa
203
"""
