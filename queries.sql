-- How many total Characters are there?
select Count(*) from charactercreator_character;

-- How many of each specific subclass?
-- Total fighters:
select count(*) from charactercreator_fighter;

-- Total mages:
select count(*) from charactercreator_mage where character_ptr_id not in (select mage_ptr_id from charactercreator_necromancer);

-- Total clerics:
select count(*) from charactercreator_cleric ;

-- Total thiefs:
select count(*) from charactercreator_thief;

-- Total necromancers:
select count(*) from charactercreator_mage as mage, charactercreator_necromancer as necro where mage.character_ptr_id=necro.mage_ptr_id;

-- How many total Items?
select count(*) from armory_item;

-- How many of the Items are weapons? How many are not?
-- all weapons:
select count(*) from armory_weapon;

-- all non-weapons:
select count(*) from armory_item where item_id not in (select item_ptr_id from armory_weapon);

-- On average, how many Items does each Character have?
total_items = select count(*) from charactercreator_character_inventory;
total_characters = select count(*) from charactercreator_character;
avg = total_items / total_characters

-- On average, how many Weapons does each character have?
total_weapons = select count(*) from charactercreator_character_inventory where item_id in (select item_ptr_id from armory_weapon);

total_characters = select count(*) from charactercreator_character;

avg = total_weapons / total_characters

-- Do queries that filter/group on substrings (e.g. how many item names contain "quid")

select count(*) from armory_item where name like '%quid%';