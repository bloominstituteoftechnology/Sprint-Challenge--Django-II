#### Question 1: How many total Characters are there? ####

## Obtain all Characters in database
from charactercreator.models import Fighter, Mage, Cleric, Thief, Necromancer, Character
## Set all characters to a variable
all_entries = Character.objects.all()
## Got a count of all_entries
all_entries.count()
### 302

#### Question 2: How many of each specific subclass? ####

# Get all Fighters
fighters = Fighter.objects.all()
# Get count
fighters.count()
### 68

# Get all Mage -- since Necromancer is a subclass of Mage, it needs to be filtered out
mage = Mage.objects.filter(necromancer__isnull=True)
# Get count
mage.count()
### 97

# Get all Clerics
cleric = Cleric.objects.all()
# Get count
cleric.count()
### 75

# Get all Thieves
thieves = Thief.objects.all()
# Get count
thieves.count()
### 51

# Get all Necromancers
necromancer = Necromancer.objects.all()
# Get count
necromancer.count()
### 11

#### Question 3: How many total Items? ####

# Import all items
from armory.models import Item, Weapon
# Get all items
all_items = Item.objects.all()
# Get a count
all_items.count()
### 174

#### Question 4: How many of the Items are weapons? How many are not? ####

# Filter through items for weapons
Item.objects.filter(weapon__isnull=False).count()
### 37

# Filter through items that are not weapon
Item.objects.filter(weapon__isnull=True).count()
### 137

#### Question 5: On average, how many Items does each Character have? ####

# To do so get the entire total amount of items used between characters and divide by total characters
Character.objects.filter(inventory__isnull=False).count() / Character.objects.all().count()
### 2.9735099337748343

#### Question 6: On average, how many Weapons does each character have?