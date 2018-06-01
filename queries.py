from charactercreator.models import Character
from armory.models import Item
## How many total Characters are there?
characters = Character.objects.all()
char_result = len(characters)
print("There are", char_result, "characters in total")

""" There are 302 total characters """

## How many of each specific subclass?


## How many total Items?
items = Item.objects.all()
item_result = len(items)
print("There are", item_result, "items in total")

""" There are 174 total items """

## How many of the Items are weapons? How many are not?


## On average, how many Items does each Character have?


## On average, how many Weapons does each character have?
