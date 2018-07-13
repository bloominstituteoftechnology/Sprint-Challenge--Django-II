-- #1 Answer: 302
SELECT COUNT(character_id)
FROM charactercreator_character;

-- #2a FIGHTERS: 68
SELECT COUNT(character_ptr_id)
FROM charactercreator_fighter;

-- #2b CLERICS: 75
SELECT COUNT(character_ptr_id)
FROM charactercreator_cleric;

-- #2c THIEF.tables: 51
SELECT COUNT(character_ptr_id)
FROM charactercreator_thief;

-- #2d MAGE: 108
SELECT COUNT(character_ptr_id)
FROM charactercreator_mage;


-- #2e NECROMANCER 11
SELECT COUNT(mage_ptr_id)
FROM charactercreator_necromancer;


-- #3 Armory items: 174

SELECT COUNT(item_id)
FROM armory_item;

-- #4a Weapons: 37
SELECT COUNT(item_ptr_id)
FROM armory_weapon;

--#4b Non weapons: 137
SELECT COUNT(item_id)
FROM armory_item
WHERE item_id NOT IN (SELECT item_ptr_id
FROM armory_weapon);


-- #5 Average Items per Character: 2.9735
SELECT AVG(items.item_count)
FROM (SELECT COUNT(item_id) as item_count
    FROM charactercreator_character_inventory
    GROUP BY character_id) items;

-- #6 Average Weapons per Character: 1.3097
SELECT AVG(weapons.weapon_count)
FROM (SELECT COUNT(item_id) as weapon_count
    FROM charactercreator_character_inventory
    WHERE item_id IN (SELECT item_ptr_id
    FROM armory_weapon)
    GROUP BY character_id) weapons;



