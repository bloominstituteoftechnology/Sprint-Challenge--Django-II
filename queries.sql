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



-- 6. On average, how many Weapons does each character have?