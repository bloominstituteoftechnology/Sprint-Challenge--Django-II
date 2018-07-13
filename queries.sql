-- How many total Characters are there?
select count(*) "Total Characters" from charactercreator_character;

-- How many of each specific subclass?
select count(*) "Clerics" from charactercreator_cleric;
select count(*) "Fighters" from charactercreator_fighter;
select count(*) "Mage" from charactercreator_mage;
select count(*) "Necromancer" from charactercreator_necromancer;
select count(*) "Thief" from charactercreator_thief;

-- How many total Items?
select count(*) "Total Items" from armory_item;

-- How many of the Items are weapons?
select count(*) "Weapons" from armory_weapon;

-- How many are not?
select count(*) "Not Weapons"
from armory_item
where item_id not in (select item_ptr_id from armory_weapon);

-- On average, how many Items does each Character have?
select AVG("Average Items") from
  (select character_id, COUNT(item_id) "Average Items"
   from charactercreator_character_inventory GROUP BY character_id);

-- On average, how many Weapons does each character have?
select AVG("Average Weapons") from
  (select character_id, COUNT(item_id) "Average Weapons"
   from charactercreator_character_inventory
   where item_id in (select item_ptr_id from armory_weapon)
   GROUP BY character_id);