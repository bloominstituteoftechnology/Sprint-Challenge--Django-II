- How many total Characters are there?
    sqlite> select * from charactercreator_character;
    >>> Character.objects.get()
    302

- How many of each specific subclass?
5

- How many total Items?
    Item.objects.get()
    174
- How many of the Items are weapons? How many are not?
    select * from armory_weapon;
    item_ptr_id 138 -174 are weapons
    item_ptr_id 001 -137 are not weapons

- On average, how many Items does each Character have?

- On average, how many Weapons does each character have?