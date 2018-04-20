
-- Query 1
-- How many total Characters are there?
SELECT COUNT(*) FROM charactercreator_character;      -- 302

-- Query 2
-- How many of each specific subclass?
SELECT COUNT(*) FROM charactercreator_fighter;        -- Weapon:      68
SELECT COUNT(*) FROM charactercreator_mage;           -- Mage:        108
SELECT COUNT(*) FROM charactercreator_cleric;         -- Clerix:      75
SELECT COUNT(*) FROM charactercreator_thief;          -- Thief:       51
SELECT COUNT(*) FROM charactercreator_necromancer;    -- Necromancer: 11


-- Query 3
-- How many total Items?
SELECT COUNT(*) FROM armory_item;                     -- 174

-- Query 4
-- How many of the Items are weapons?
SELECT COUNT(*) FROM armory_weapon;                   -- 37

-- How many of the Items are NOT weapons?
SELECT COUNT(*) FROM armory_item WHERE item_id 
  NOT IN (SELECT item_ptr_id FROM armory_weapon);     -- 137


-- Query 5
-- On average, how many Items does each Character have?


-- Query 6
-- On average, how many Weapons does each character have?
