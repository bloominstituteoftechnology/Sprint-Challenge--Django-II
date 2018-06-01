### Write Python code that uses the Django ORM to answer:

# How many total Characters are there?
from charactercreator.models import Character
len(Character.objects.all())

# How many of each specific subclass?
len(Character.objects.filter(fighter=True))
len(Character.objects.filter(mage=True))
len(Character.objects.filter(cleric=True))
len(Character.objects.filter(thief=True))
# need query count for necromancer

# How many total Items?
from charactercreator.models import Item
len(Item.objects.all())

# How many of the Items are weapons? How many are not?


# On average, how many Items does each Character have?


# On average, how many Weapons does each character have?
