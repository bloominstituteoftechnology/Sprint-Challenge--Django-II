# How many total Characters are there?
from charactercreator.models import Character
len(Character.objects.all())
""" 302 """

# How many of each specific subclass?
from charactercreator.models import Fighter, Mage, Cleric, Thief, Necromancer
len(Fighter.objects.all())
""" 68 """
len(Mage.objects.all())
""" 108 """
len(Cleric.objects.all())
""" 75 """
len(Thief.objects.all())
""" 51 """
len(Necromancer.objects.all())
""" 11 """

"""
The Necromancer class extends the Mage class, 
which explains a total number of characters being 302,
but each class of character totaling 313.  
(An aside... but by this logic, a Cleric should extend the mage class
as well.  Or better yet, have a Melee and Magic class that is 
extended by Fighter/Thief, Elementalist/Cleric/Necormancer... I could go
on a hundred line diatribe about this, so I digress...)
"""
# How many total Items?
from armory.models import Item
len(Item.objects.all())
""" 174 """

# How many of the Items are weapons? How many are not?
from armory.models import Weapon
len(Weapon.objects.all())
""" 
37 are weapons, ergo 137 are not.  I attempted to find a way
to find the distinction via querying, but unless the information I found
was misguided, this can only be achieved by modifying the code to have
the items set a type on the model.
I went down a rabbit hole for a good half hour or so trying to do a for loop
with variations of issubclass or isinstance and keeping a count to no avail.
"""

# On average, how many Items does each Character have?
itemcount = 0
charactercount = 0
for character in Character.objects.all():
    charactercount += 1
    for item in character.inventory.all():
        itemcount += 1

"""
Character count yields 302, itemcount yields 898. 
The average is ~3 (2.9735099337748343)
"""

# On average, how many Weapons does each character have?

weaponcount = 0
charactercount = 0
for character in Character.objects.all():
    charactercount += 1
    for item in character.inventory.all():
        if item.item_id > 137:
            weaponcount += 1

"""
I imagine I did this improperly.  Similarly to the 'how many items are weapons
question', I couldn't divise a good way to distinguish whether or not the item
was a regular item or a weapon.  That being said, the weapon items start at the 
item_id of 138 and go up whereas the regular items are 137 and down.
"""

#- Do queries that filter/group on substrings (e.g. how many item names contain "quid"
Item.objects.filter(name__contains="quid")
Item.objects.filter(value__gt=0)
""" 
This oddly returns an empty QuerySet.  Or it seemed odd until I ran
for item in Item.objects.all():
    print(item.value) 
and saw nothing but zeroes.  
"""