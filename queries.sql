-- How many total Characters are there?
SELECT count(*) FROM charactercreator_character; --302


-- How many of each specific subclass?
SELECT count(*) FROM charactercreator_fighter; --68
SELECT (SELECT count(*) FROM charactercreator_mage) - (SELECT count(*) FROM charactercreator_necromancer); --97
SELECT count(*) FROM charactercreator_cleric; --75
SELECT count(*) FROM charactercreator_thief; --51
SELECT count(*) FROM charactercreator_necromancer; --11

-- How many total Items?
SELECT count(*) FROM armory_item; --174

-- How many of the Items are weapons? 
SELECT count(*) FROM armory_weapon; --37
-- How many are not?
SELECT (SELECT count(*) FROM armory_item) - (SELECT count(*) FROM armory_weapon); --137

-- On average, how many Items does each Character have?
SELECT (SELECT count(*) FROM charactercreator_character_inventory) / (SELECT count(*) * 1.0 FROM charactercreator_character); --2.97350993377483

--On average, how many Weapons does each character have?
SELECT (SELECT count(*) FROM charactercreator_character_inventory AS inventory JOIN armory_weapon AS weapon WHERE inventory.item_id = weapon.item_ptr_id) / (SELECT count(*) * 1.0 FROM charactercreator_character); --0.672185430463576