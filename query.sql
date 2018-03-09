
How many total Characters are there?
>>>select count(*) from charactercreator_character;

How many of each specific subclass?
>>>select count(*) from charactercreator_cleric;
75
>>>select count(*) from charactercreator_fighter;
68
>>>select count(*) from charactercreator_mage;
108
>>>select count(*) from charactercreator_theif;
51
>>>select count(*) from charactercreator_necromancer;
11
# there are 302 total Characters, 108 are Mages, 11 of those 108 are Necros
# Necros count within the Mage count because they inherit from Mages. 
>>> Mage.objects.filter(necromancer__isnull=True).count()
97

How many total Items?
# total items across all characters
select * from  charactercreator_character_inventory;
898

How many of the Items are weapons? How many are not?
# total across all characters
>>>select * from charactercreator_character_inventory where item_id >= 138;
203

On average, how many Items does each Character have?


On average, how many Weapons does each character have?