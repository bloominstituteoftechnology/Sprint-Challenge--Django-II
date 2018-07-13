# - How many total Characters are there?
total_characters = Character.objects.count()

# - How many of each specific subclass?
fighter_subclass_total = Fighter.objects.count()

mage_subclass_total = Mage.objects.count()

cleric_subclass_total = Cleric.objects.count()

thief_subclass_total = Thief.objectss.count()

necromancer_subclass_total = Necromancer.objects.count()

# - How many total Items?
items_total = Item.objects.count()

# - How many of the Items are weapons? How many are not?
items_are_weapons = Weapon.objects.count()

items_arenot_weapons = Item.objects.exclude(
    item_id__in=Weapon.objects.all()).count()

# - On average, how many Items does each Character have?
average_item_per_character = Characters.objects.count() / Item.objects.count()

# - On average, how many Weapons does each character have?
average_weapon_per_character = Characters.objects.count() / items_are_weapons()

print("Number of total characters: " + total_characters)

print("There are 5 specific classes the total for each are: \n" +
      "Fighter: " + fighter_subclass_total + "\n" +
      "Mage: " + mage_subclass_total + "\n" +
      "Cleric: " + cleric_subclass_total + "\n" +
      "Thief: " + thief_subclass_total + "\n" +
      "Necromance: " + necromancer_subclass_total)

print("Total items: " + items_total)

print("Items that are weapons: " + items_are_weapons)

print("Items that are not weapons: " + items_arenot_weapons)

print("Average item per character: " + average_item_per_character)

print("Average weapon per character: " + average_weapon_per_character)
