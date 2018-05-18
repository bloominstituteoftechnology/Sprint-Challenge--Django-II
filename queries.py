from charactercreator.model import Character, Mage, Cleric, Fighter, Thief, Necromancer
from armory.models import Item, Weapon
from django.db.models import Count, Avg

# 1. How many total Characters are there?
def get_characters():
  return Character.objects.count() # 302


# 2. How many of each specific subclass?
def get_subclasses():
  counts = {}
  counts[Mage] = Mage.objects.count()               # 108 including necromancers, 97 without
  counts[Cleric] = Cleric.objects.count()           # 75
  counts[Fighter] = Fighter.objects.count()         # 68
  counts[Thief] = Thief.objects.count()             # 51
  counts[Necromancer] = Necromancer.objects.count() # 11 
  return counts

# 3. How many total Items?
def get_items():
  return Item.objects.count() # 174

# 4. How many of the Items are weapons? How many are not?
def get_weapons():
  return Weapon.objects.count() # 37

def get_non_weapons():
  return get_items() - get_weapons() # 137 items are not weapons

# 5. On average, how many Items does each Character have?
def avg_item_per_character():
  inv_items = [char.inventory.count() for char in Character.objects.all()] # number of items each character has in inventory
  return (sum(inv_items) / get_characters()) # 2.973 items per character

  # OR

  return Character.objects.all().annotate(avg_items = Count('inventory')).aggregate(Avg('avg_items')) # 2.9735099337748343

# 6. On average, how many Weapons does each character have?
def avg_weapon_per_character():
  return Character.objects.all().annotate(avg_weapons = Count('inventory__weapon')).aggregate(Avg('avg_weapons')) # 0.6721854304635762
