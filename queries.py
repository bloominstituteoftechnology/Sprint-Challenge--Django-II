# How many total Characters are there?
from charactercreator.models import Character
characters_count = Character.objects.all().count()
print('How many total Characters are there?', characters_count)

# How many of each specific subclass?
characters_subclasses = Character.__subclasses__()
print('How many of each specific subclass?')
for subclass in characters_subclasses:
  print(subclass.__name__, ':', subclass.objects.all().count())

# How many total Items?
from armory.models import Item
items_count = Item.objects.all().count()
print('How many total Items?', items_count)

# How many of the Items are weapons? How many are not?
weapons_count = Item.__subclasses__()[0].objects.all().count()
print('How many of the Items are weapons?', weapons_count, ',How many are not?', items_count - weapons_count)

# On average, how many Items does each Character have?
characters = Character.objects.all()
average_items = 0
for character in characters:
  average_items += character.inventory.count()
average_items = average_items / characters.count()
print('On average, how many Items does each Character have?', average_items)

# On average, how many Weapons does each character have?
average_weapons = 0
for character in characters:
  for item in character.inventory.all():
    if item.__class__.__name__ == 'weapon':
      average_weapons += 1