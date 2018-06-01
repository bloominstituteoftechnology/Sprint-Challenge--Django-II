from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

#1  Total Characters in DB
def total_characters:
  total = len(Character.objects.all())
  print('Total Characters {total}'.format(total = total))

#2 How many characters per sub class

def subclass_count:
  Fighter = len(Fighter.objects.all())
  Mage = len(Mage.objects.all())
  Cleric = len(Cleric.objects.all())
  Thief = len(Thief.objects.all())
  Necromancer = len(Necromancer.objects.all())
  print('Here is the totals for each subclass:')
  print('Fighter: {Fighter}'.format(Fighter= Fighter))
  print('Mage: {Mage}'.format(Mage= Mage))
  print('Cleric: {Cleric}'.format(Cleric= Cleric))
  print('Thief: {Thief}'.format(Thief= Thief))
  print('Necromancer: {Necromancer}'.format(Necromancer= Necromancer))

#3 Total items

  def total_items:
    Item = len(Item.objects.all())
    print('Total items {Item}'.format(Item=Item))

#4 How many items are weapons and how many are not

  def total_weapon_item:
    itemTotal = len(Item.objects.all())
    weaponTotal = len(Weapon.objects.all())
    justItems = Item - Weapon
    print('Total Weapons {Weapon}'.format(Weapon=weaponTotal))
    print('Total Items that are not weapons {justItems}'.format(justItems=justItems))

#5 Average items charactor holds

  def avg_item_on_character:
    totalCharacters = len(Character.objects.all())
    totalItems = 0
    for char in totalCharacters:
      totalItems = totalItems + len(char.inventory.all())
    
    avg_items = totalItems / totalCharacters
    print('Average items characters hold {avg}'.format(avg=avg_items))

#6 Average weapons Charaters have 

  def avg_weapon_on_character
    totalWeapons = 0
    totalCharacters = len(Character.objects.all())
    for char in totalCharacters:
      for inventory in char.inventory.all():
        if ininstance(inventory, Weapon):
          totalWeapons = totalWeapons + 1
    
    avg_items = totalWeapons / totalCharacters
    print('Average wewapons characters hold {avg}'.format(avg=avg_items))