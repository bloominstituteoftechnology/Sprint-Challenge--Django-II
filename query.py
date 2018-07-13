from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

char_amount = Character.objects.count()
print('Total amount of characters:', char_amount)

fighter_amount = Fighter.objects.count()
print ('Total Fighters:', fighter_amount)

cleric_amount = Cleric.objects.count()
print ('Total Clerics:', cleric_amount)

mage_amount = Mage.objects.count()
print ('Total Mages:', mage_amount)

thief_amount = Thief.objects.count()
print ('Total Thieves:', thief_amount)

necro_amount = Necromancer.objects.count()
print ('Total Necromancers:', necro_amount)

item_amount = Item.objects.count()
print ('Total Items:', item_amount)

weapon_amount = Weapon.objects.count()
print ('Total Weapons:', weapon_amount)

item_no_wep = item_amount - weapon_amount
print ('Items but no weapons:', item_no_wep)

characters = Character.objects.all()
charItems = 0
for character in characters:
    charItems += character.inventory.count()

avgItems = charItems / Character.objects.count()
print('Average number of items:', avgItems)

avgWeps = weapon_amount / char_amount
print('Average number of weapons per character:', avgWeps)