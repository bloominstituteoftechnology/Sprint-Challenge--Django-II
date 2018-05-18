-- - How many total Characters are there? 302

SELECT      COUNT(character_id)
FROM        charactercreator_character;

-- - How many of each specific subclass?
-- fighter
SELECT      COUNT(character_ptr_id)
FROM        charactercreator_fighter;
-- mage
SELECT      COUNT(character_ptr_id)
FROM        charactercreator_mage, charactercreator_necromancer
WHERE       mage_ptr_id IS NULL; 

-- cleric: 75
SELECT      COUNT(character_ptr_id)
FROM        charactercreator_cleric;
-- thief: 51
SELECT      COUNT(character_ptr_id)
FROM        charactercreator_thief;
-- necromancer: 11
SELECT      COUNT(mage_ptr_id)
FROM        charactercreator_necromancer;

-- How many total Items? 174
SELECT      COUNT(item_id)
FROM        armory_item;

-- How many of the Items are weapons? 37
SELECT      COUNT(item_ptr_id)
FROM        armory_weapon;