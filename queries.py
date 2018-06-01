from charactercreator.models import Character
## How many total Characters are there?
characters = Character.objects.all()
result = len(characters)
print("There are", result, "characters in total")

""" There are 302 total characters """

## How many of each specific subclass?


## How many total Items?


## How many of the Items are weapons? How many are not?


## On average, how many Items does each Character have?


## On average, how many Weapons does each character have?
