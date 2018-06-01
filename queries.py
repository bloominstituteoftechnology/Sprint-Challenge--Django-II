print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print('SPRINT CHALLENGE - DJANGO II: THE AWAKENING\n')
print('In an enchanted and blookdsoaked land far away...\n')
# Get total number of characters
from charactercreator.models import Character
chars_count = Character.objects.count()
print('Total characters: %d' % chars_count) # should be 302


# Get total number of Fighters
from charactercreator.models import Fighter
fighter_count = Fighter.objects.count()
print('    Fighter: %d' % fighter_count) # Should be 68


# Get total number of Necromancers
from charactercreator.models import Necromancer
necromancer_count = Necromancer.objects.count()
print('    Necromancers: %d' % necromancer_count) # Should be 11


# Get total number of Mages
from charactercreator.models import Mage
mage_count = Mage.objects.count() - necromancer_count
print('    Mages: %d' % mage_count) # Should be 97


# Get total number of Clerics
from charactercreator.models import Cleric
cleric_count = Cleric.objects.count()
print('    Clerics: %d' % cleric_count) # Should be 75


# Get total number of Thiefs
from charactercreator.models import Thief
thief_count = Thief.objects.count()
print('    Thieves: %d' % thief_count) # Should be 51

print('')

# Get total number of Items
from armory.models import Item, Weapon
item_count = Item.objects.count()
weapon_count = Weapon.objects.count()
print('Total items %d' % item_count)
print('    Weapons: %d' % weapon_count)
print('    Non-weapons: %d' % (item_count - weapon_count))

print('')

# Average number items a character has
chars_all = Character.objects.all()
char_inventory_total = 0
for char in chars_all:
    char_inventory_total += char.inventory.count()
print('Average number of items in characters inventories: %f' % (char_inventory_total / chars_count))


# Average number of weapons each character has
weapons_all = Weapon.objects.all()
weapons_total = 0
for weapon in weapons_all:
    weapons_total += weapon.character_set.count()
print('Average number of weapons in characters inventories: %f' % (weapons_total / chars_count))
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
