# Import Characters and subclasses
from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
# Import Items
from armory.models import Item, Weapon

# Find total number of characters
characters = Character.objects.all()
totalCharacters = characters.count()

# Find total of each subclass
fighters = Fighter.objects.all()
totalFighters = fighters.count()

mages = Mage.objects.all()
totalMages = mages.count()

clerics = Cleric.objects.all()
totalClerics = clerics.count()

thieves = Thief.objects.all()
totalThieves = thieves.count()

necromancers = Necromancer.objects.all()
totalNecromancers = necromancers.count()


# Find total Items
items = Item.objects.all()
items.count()

# Find total Weapons
weapons = Weapon.objects.all()
weapons.count()

# Find Items that are not Weapons
items.filter(weapon__isnull=True).count()
# or
items.exclude(weapon__isnull=False).count()

# Find average Items per Character
totalCharacters = characters.count()
totalItems = 0
totalWeapons = 0

for character in characters:
  totalItems += character.inventory.count()
  totalWeapons += character.inventory.filter(weapon__isnull=False).count()

averageItems = totalItems/totalCharacters

# Find average Weapons per Character
averageWeapons = totalWeapons/totalCharacters

"""

- How many total Characters are there?
  302

- How many of each specific subclass?
  Fighters - 68
  Mage - 108
  Cleric - 75
  Thief - 51
  Necromancer - 11

- How many total Items?
  174

- How many of the Items are weapons? How many are not?
  37 are weapons
  137 are not weapons

- On average, how many Items does each Character have?
  2.9735099337748343

- On average, how many Weapons does each character have?
  0.6721854304635762

"""