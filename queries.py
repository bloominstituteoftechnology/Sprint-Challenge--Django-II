from charactercreator.models import Character
from armory.models import Item
## How many total Characters are there?
characters = Character.objects.all()
result = len(characters)
print("There are", result, "characters in total")

""" There are 302 total characters """

## How many of each specific subclass?


## How many total Items?
items = Item.objects.all()
result = len(items)
print("There are", result, "items in total")

""" There are x total items """

## How many of the Items are weapons? How many are not?


## On average, how many Items does each Character have?


## On average, how many Weapons does each character have?
