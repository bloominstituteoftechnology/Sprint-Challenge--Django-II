# Run commands in Django to access the DB with the Python ORM.

# How many total characters are there?
c = Character.objects.all()
print(len(c))

# How many member of each subclass are there?
classBreakdown = {}
classBreakdown['Fighter'] = len(Fighter.objects.all())
classBreakdown['Mage'] = len(Mage.objects.all())
classBreakdown['Thief'] = len(Thief.objects.all())
classBreakdown['Cleric'] = len(Cleric.objects.all())
classBreakdown['Necromancer'] = len(Necromancer.objects.all())
print(classBreakdown)

# How may items are there?
i = Item.objects.all()
print(len(i))

# How many weapons are there?
w = Weapon.objects.all()
print(len(w))

# How many items does each character have, on average?
counter = 0
for char in Character.objects.all():
  counter += len(char.inventory.all())

average = counter / len(Character.objects.all())
print(average)

# How many weapons does each character have, on average?
counter = 0
for char in Character.objects.all():
  counter += len(char.inventory.filter())

average = counter / len(Character.objects.all())
print(average)