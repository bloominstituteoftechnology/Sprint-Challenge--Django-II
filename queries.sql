-- 1. How many total Characters are there?
-- ANSWER: 302
-- # sql:
-- # select count(*) from charactercreator_character


-- 2. How many of each specific subclass?



-- 3. How many total Items?
-- ANSWER: 174
-- code:
-- select count(*) from armory_item


-- 4. How many of the Items are weapons? How many are not?
-- ANSWER: 38 Weapons, 136 non-Weapon Items
-- code:
-- select count(*) from armory_weapon
-- select count(*) from armory_item where armory_item.item_id not in (select item_ptr_id from armory_weapon)



-- 5. On average, how many Items does each Character have?
--A: 2.97 (2)
-- sqlite> select count(*) from charactercreator_character_inventory;
-- count(*)  
-- ----------
-- 898       
-- sqlite> select count(*) from charactercreator_character;
-- count(*)  
-- ----------
-- 302 
--MANUAL DIVISION : 2.97

--B:
-- sqlite> select ((select count(*) from charactercreator_character_inventory)/(select count(*) from charactercreator_character));
-- ((select count(*) from charactercreator_character_inventory)/(select count(*) from charactercreator_character))
-- ---------------------------------------------------------------------------------------------------------------
-- 2                                                                                                              
 




-- 6. On average, how many Weapons does each character have?

-- POSSIBLE? THOUGH DIFFERENT FROM QUERIES.PY ANSWER
-- sqlite> select count(*) from charactercreator_character_inventory as inventory where inventory.item_id not in (select item_ptr_id as item_id from armory_weapon)
--    ...> ;
-- 692 (this is total amount of weapons across all characters)
-- MANUAL DIVISION: ANSWER: 2.29


-- **Do queries that filter/group on substrings (e.g. how many item names contain "quid")



-- charactercreator_character_inventory
-- id          character_id  item_id 