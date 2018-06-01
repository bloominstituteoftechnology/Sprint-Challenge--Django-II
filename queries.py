# How many total Characters are there?
c = Character.objects.all()
len(c) # answer is 302


# How many of each specific subclass?


# How many total Items?
eyetums = Item.objects.all() # gets total number of items
len(eyetums) # shows 174 items

# How many of the Items are weapons? How many are not?
waypuns = Weapon.objects.all() # gets total number of weapons
len(waypuns) # shows 37 items
knotWaypuns = len(eyetums) - len(waypuns) # the answer is 137


# On average, how many Items does each Character have?
# len(eyetums)/len(c)

# On average, how many Weapons does each character have?
# 