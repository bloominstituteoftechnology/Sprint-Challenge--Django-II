from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer

from armory.models import Item, Weapon


# Total characters
total_charc = Character.objects.count()
# 302

# each sub class
Fighter.objects.count()
# 68
Mage.objects.count()
# 108
Cleric.objects.count()
#  75
Thief.objects.count()
#  51
Necromancer.objects.count()
#  11

# Total items
Item.objects.count()
# 174

# items that are weapons
Weapon.objects.count()
# 37

# 174 - 37
# items that are not weapons = 137


# total items in character inventory
char_items = Character.objects.values('inventory').count()
#  898

# average of items on characters
char_items / total_charc
# = 2.97

# average weapons each charcters has
total_charc / 37  # total weapons
# 8.2 rounded up
