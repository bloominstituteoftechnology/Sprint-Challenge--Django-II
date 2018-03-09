**DO THIS FIRST**
>>> source env/bin/activate
>>> cd rpg
>>> ./manage.py shell (or dbshell)


- How many total Characters are there?
>>> from charactercreator.models import Character
>>> character = Character.objects.all()
>>> len(character) >>> 302


- How many of each specific subclass?
>>> from charactercreator.models import Cleric, Fighter, Mage, Necromancer, Thief
>>> cleric = Cleric.objects.all()
>>> len(cleric) >>> 75
>>> fighter = Fighter.objects.all()
>>> len(fighter) >>> 68
>>> mage = Mage.objects.all()
>>> len(mage) >>> 108
>>> necromancer = Necromancer.objects.all()
>>> len(necromancer) >>> 11
>>> thief = Thief
>>> len(thief) >>> 51


- How many total Items? (In the armory?)
>>> from armory.models import Item
>>> item = Item.objects.all()
>>> len(item) >>> 174

- How many of the Items are weapons? How many are not?
>>> from armory.models import Weapon
>>> weapon = Item.objects.all()
>>> len(weapon) >>> 37

ARE >>> 37
ARE NOT >>> 137

Since the armory_weapon table field "item_ptr_id" references the armory_item
table field "item_id" it means that 37 of the items are weapons. This should 
mean that the total is 174, and not (174 + 37)


- On average, how many Items does each Character have?
Using the info we already have above, we want to divide the total items (174)
by the amount of characters in the database (302). You get an average of
0.5761589403973509 items per character. Meaning by average, that almost half 
the characters don't have an item at all.

>>> from armory.models import Item
>>> from charactercreator.models import Character
>>> item = Item.objects.all()
>>> character = Character.objects.all()
>>> average_items = len(item) / len(character)
>>> average_items    OR    >>> print(average_items)


- On average, how many Weapons does each character have?
Using the info we already have above, we want to divide the total weapons (37)
by the amount of characters in the database (302). You get an average
of 0.12251655629139073 weapons per player. Meaning that on average, only about 12%
of characters have weapons.

>>> from armory.models import Weapon
>>> from charactercreator.models import Character
>>> weapon = Weapon.objects.all()
>>> character = Character.objects.all()
>>> average_weapons = len(weapon) / len(character)
>>> average_weapons   OR    >>> print(average_weapons)
