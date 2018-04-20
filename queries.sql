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
select 

-- On average, how many Weapons does each character have?
