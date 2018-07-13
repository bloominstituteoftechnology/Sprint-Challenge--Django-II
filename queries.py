from charactercreator.models import *
from armory.models import *

character_count = Character.objects.all().count()
fighter_count = Fighter.objects.all().count()
mage_count = Mage.objects.all().count()
cleric_count = Cleric.objects.all().count()
thief_count = Thief.objects.all().count()

necromancer_count = Necromancer.objects.all().count()

items_count = Item.objects.all().count()
weapons_count = Weapon.objects.all().count()

non_weapon_items = items_count - weapons_count

total_items_held = 0
total_weapons_held = 0
all_characters = Character.objects.all()

for character in all_characters:
    total_items_held += character.inventory.count()
    total_weapons_held += character.inventory.filter(weapon=None).count()


ave_items_per_character = total_items_held / character_count
ave_weapons_per_character = total_weapons_held / character_count

print('Characters: ' + str(character_count))
print('Fighters: ' + str(fighter_count))
print('Mages: ' + str(mage_count))
print('Clerics: ' + str(cleric_count))
print('Thieves: ' + str(thief_count))
print('Necromancers: ' + str(necromancer_count))
print('')
print('Items: ' + str(items_count))
print('Weapons: ' + str(weapons_count))
print('Non-weapon Items: ' + str(non_weapon_items))
print('Average number of items per Character: ' + str(ave_items_per_character))
print('Average number of weapons per character: ' + str(ave_weapons_per_character))