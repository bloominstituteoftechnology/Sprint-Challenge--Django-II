from armory.models import *
from charactercreator.models import *

# Query 1
# How many total Characters are there?
def totalCharacters():
  count = Character.objects.count()
  return count                                        # 302


# Query 2
# How many of each specific subclass?
def totalSubclasses():
  print('Weapon: ', totalWeaponItems())               # Weapon:       37
  print('Fighter: ', Fighter.objects.count())         # Fighter:      68
  print('Mage: ', Mage.objects.count())               # Mage:         108
  print('Cleric: ', Cleric.objects.count())           # Cleric:       75
  print('Thief: ', Thief.objects.count())             # Thief:        51
  print('Necromancer: ', Necromancer.objects.count()) # Necromancer:  11


# Query 3
# How many total Items?
def totalItems():
  count = Item.objects.count()
  return count                                        # 174


# Query 4
# How many of the Items are weapons?
def totalWeaponItems():
  count = Weapon.objects.count()
  return count                                        # 37

# How many of the Items are NOT weapons?
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

  return sum / Characters.count()                     # 0.6721854304635762
