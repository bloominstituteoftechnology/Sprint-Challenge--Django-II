from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

# Total number of characters
print('Total characters:', Character.objects.count())

# Number of Mages (including Necromancers)
print('Number of Mages including Necromancers:', Mage.objects.count())

# Number of Mages (NOT including Necromancers)
print('Number of Mages not including Necromancers:', Mage.objects.exclude(necromancer__isnull=False).count())

# Number of Fighters
print('Number of Fighters:', Fighter.objects.count())

# Number of Clerics
print('Number of Clerics', Cleric.objects.count())

# Number of Thieves
print('Number of Thieves', Thief.objects.count())

# Number of Necromancers
print('Number of Necromancers', Necromancer.objects.count())

# Total number of items
print('Total number of Items:', Item.objects.count())

# Number of Weapons
print('Number of Weapons:', Weapon.objects.count())

# Number of Items that are not Weapons
print('Number of non-Weapon Items:', Item.objects.filter(weapon__isnull=True).count())

# Average Item per character
characters = list(Character.objects.all())
print(Weapon.objects.all()[0])

total = 0
for c in characters:
  total += c.inventory.count()
print('Average number of items:', round(total / len(characters)))

weapons_total = 0
for c in characters:
  weapons_total += c.inventory.filter(weapon__isnull=False).count()
print('Average number of weapons:', weapons_total / len(characters))
print(weapons_total)