-- Question 1:
-- Answer = CHARACTERS: 302
SELECT COUNT(character_id)
FROM charactercreator_character;

-- Question 2a:
-- Answer = FIGHTERS: 68
SELECT COUNT(character_ptr_id)
FROM charactercreator_fighter;

-- Question 2b:
-- Answer = CLERICS: 75
SELECT COUNT(character_ptr_id)
FROM charactercreator_cleric;

-- Question 2c:
-- Answer = THIEF: 51
SELECT COUNT(character_ptr_id)
FROM charactercreator_thief;

-- Question 2d:
-- Answer = MAGE: 108
SELECT COUNT(character_ptr_id)
FROM charactercreator_mage;

-- Question 2e:
-- Answer = NECROMANCER: 11
SELECT COUNT(character_ptr_id)
FROM charactercreator_necromancer;

-- Question 3:
-- Answer = AROMORY ITEMS: 174
SELECT COUNT(item_id)
FROM armory_item;

-- Question 4a:
-- Answer = WEAPONS: 37
SELECT COUNT(item_ptr_id)
FROM armory_item;

-- Question 4b:
-- Answer = NON WEAPONS: 137
SELECT FROM(item_id)
FROM armory_weapon;

-- Question 5:
-- Answer = AVERAGE ITEM PER CHARACTER: 2.9735
SELECT AVG(items.item_count)
FROM (SELECT COUNT(item_id)as item_count
    FROM charactercreator_character_inventory
    GROUP BY character_id) items;

-- Question 6:
-- Answer = AVERAGE WEAPONS PER CHARACTER: 1.3097
SELECT AVG(weapons.weapon_count)
FROM (SELECT COUNT(item_id) as weapon_count
    FROM charactercreator_character_inventory
    WHERE item_id IN (SELECT item_ptr_id
    FROM armory_weapon)
    GROUP BY character_id) weapons;