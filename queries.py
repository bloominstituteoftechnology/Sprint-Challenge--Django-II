from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

print("Total Characters: {}\n".format(Character.objects.count())) # 302
print("Total Fighters: {}\n".format(Fighter.objects.count())) # 68
print("Total Mages: {}\n".format(Mage.objects.count())) # 108
print("Total Clerics: {}\n".format(Cleric.objects.count())) # 75
print("Total Thieves: {}\n".format(Thief.objects.count())) # 51
print("Total Necromancers: {}\n".format(Necromancer.objects.count())) # 11

all_items = Item.objects.count()
weapon_items = Weapon.objects.count()
non_weapon_items = all_items - weapon_items
print("Total Items: {}\n".format(all_items)) # 174
print("Total Weapons: {}\n".format(weapon_items)) # 37
print("Total Non-Weapon Items: {}\n".format(non_weapon_items)) # 137

characters = Character.objects.all()
total_characters = characters.count()
character_items = sum([character.inventory.count() for character in characters])
average_items = round(character_items / total_characters)
total_weapons = sum([character.inventory.filter(weapon__isnull=False).count() for character in characters])
average_weapons = round(total_weapons / total_characters)
print("Average Character Items: {}\n".format(average_items)) # 3
print("Average Character Weapons: {}\n".format(average_weapons)) # 1