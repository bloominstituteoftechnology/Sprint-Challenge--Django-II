-- How many total Characters are there?
SELECT COUNT(*) FROM charactercreator_character;
-- A: 302

-- How many of each specific subclass?
SELECT COUNT(*) FROM charactercreator_cleric;
-- A: 75

SELECT COUNT(*) FROM charactercreator_fighter;
-- A: 68

SELECT COUNT(*) FROM charactercreator_mage;
-- A: 108

SELECT COUNT(*) FROM charactercreator_thief;
-- A: 51

SELECT COUNT(*) FROM charactercreator_necromancer;
-- A: 11

-- How many total Items?
SELECT COUNT(*) FROM armory_item;
-- A: 174

-- How many of the Items are weapons? How many are not?
SELECT COUNT(*) FROM armory_weapon;
-- A: 37 are weapons, 137 are not weapons

-- On average, how many Items does each Character have?
-- On average, how many Weapons does each character have?