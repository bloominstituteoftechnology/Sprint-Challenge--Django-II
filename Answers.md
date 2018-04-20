* How many total Characters are there?
  302 , 297 unique one
  djangoshell
  len(Character.objects.all())
  dbshell
  * select count(\*) from charactercreator_character;
  * select count(distinct name) from charactercreator_character;
* How many of each specific subclass?
  fighter - 68, mage-108,cleric -75, thief-51, Necromance - 11
* How many total Items?
  174, 172 Unique

  Python Shell
  items = Item.objects.all()
  len(items)

  db shell
  select count(\*) from armory_item;
  for getting uniques
  select count(Distinct name) from armory_item;

* How many of the Items are weapons? How many are not?
  37 are weapons, 174/172-37 are not
* On average, how many Items does each Character have?
  totalitems = 0
  for character in characters:
  ...totalitems +=character.inventory.count()

  totalitems
  898
  898/302
  Ans 2.9735099337748343

dbshell

select count(\*) from charactercreator_character_inventory;
---> 898
898/302

* On average, how many Weapons does each character have?
  for c in characters:
  ... c_items = c.inventory.all()
  ... for i in c_items:
  ... if i.item_id in weaponsdict:
  ... totalweapons += 1
  ...
  > > > totalweapons
  > > > 203
  > > > 203/302
  > > > 0.6721854304635762

dbshell

select count(\*) from charactercreator_character_inventory join armory_weapon on charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id;
