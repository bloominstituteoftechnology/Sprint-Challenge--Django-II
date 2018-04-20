-- 1. How many total characters are there? (Answer: 302)
select count(*) from charactercreator_character

-- 2. How many of each specific subclass? (Answers: 75, 68, 51, 108, 11)
select count(*) from charactercreator_cleric
select count(*) from charactercreator_fighter
select count(*) from charactercreator_thief
select count(*) from charactercreator_mage
select count(*) from charactercreator_necromancer

-- 3. How many total items? (Answer: 174)
select count(*) from armory_item

-- 4. How many items are weapons? How many are not? (Answers: 38, 136)
select count(*) from armory_weapon
select count(*) from armory_item where armory_item.item_id not in (select item_ptr_id from armory_weapon)

-- 5.  On average, how many Items does each Character have?

-- 6. On average, how many Weapons does each Character have?
