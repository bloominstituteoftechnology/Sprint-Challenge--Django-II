from armory.models import *
from charactercreator.models import *
from django.db.models import Avg

# Query 1
def totalCharacters():
  count = Character.objects.count()
  return count                                        # 302

# Query 2
def totalSubclasses():
  print('Weapon: ', totalWeaponItems())               # 37
  print('Fighter: ', Fighter.objects.count())         # 68
  print('Mage: ', Mage.objects.count())               # 108
  print('Cleric: ', Cleric.objects.count())           # 75
  print('Thief: ', Thief.objects.count())             # 51
  print('Necromancer: ', Necromancer.objects.count()) # 11

# Query 3
def totalItems():
  count = Item.objects.count()
  return count                                        # 174

# Query 4
def totalWeaponItems():
  count = Weapon.objects.count()
  return count                                        # 37

def totalNonWeaponItems():
  count = totalItems() - totalWeaponItems()
  return count                                        # 137


# Query 5
# On average, how many Items does each Character have?
def avgItems():
  sum = 0
  Characters = Character.objects.all()

  for character in Characters:
    sum += character.inventory.count()

  return sum / Characters.count()                     # 2.9735099337748343


# Query 6
# On average, how many Weapons does each character have?
def avgWeapons():
  sum = 0
  Characters = Character.objects.all()

  for character in Characters:
    sum += character.inventory.filter(weapon__isnull=False).count()

  return sum / Characters.count()                     # 2.9735099337748343

