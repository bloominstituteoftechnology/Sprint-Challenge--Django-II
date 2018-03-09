#### Question 1: How many total Characters are there? ####

## Obtain all Characters in database
>>> from charactercreator.models import Fighter, Mage, Cleric, Thief, Necromancer, Character
## Set all characters to a variable
>>> all_entries = Character.objects.all()
## Got a count of all_entries
>>> all_entries.count()
### 302



#### Question 2: How many of each specific subclass? ####

# Get all Fighters
>>> fighters = Fighter.objects.all()
# Get count
>>> fighters.count()
### 68

# Get all Mage -- since Necromancer is a subclass of Mage, it needs to be filtered out
>>> mage = Mage.objects.filter(necromancer__isnull=True)
# Get count
>>> mage.count()
### 97

# Get all Clerics
>>> cleric = Cleric.objects.all()
# Get count
>>> cleric.count()
### 75

# Get all Thieves
>>> thieves = Thief.objects.all()
# Get count
>>> thieves.count()
### 51

# Get all Necromancers
>>> necromancer = Necromancer.objects.all()
# Get count
>>> necromancer.count()
### 11



#### Question 3: How many total Items? ####

# Import all items
>>> from armory.models import Item, Weapon
# Get all items
>>> all_items = Item.objects.all()
# Get a count
>>> all_items.count()
### 174



#### Question 4: How many of the Items are weapons? How many are not? ####

# Filter through items for weapons
>>> Item.objects.filter(weapon__isnull=False).count()
### 37

# Filter through items that are not weapon
>>> Item.objects.filter(weapon__isnull=True).count()
### 137

#### Question 5: On average, how many Items does each Character have? ####

## Gather number of items among all characters
>>> Character.inventory.through.objects.filter(item_id__lt=137).count()
## 689

# Take the total amount of items used between characters and divide by total characters
>>> Character.inventory.through.objects.filter(item_id__lt=137).count() / Character.objects.all().count()
### 2.281456953642384 ~ 2


#### Question 6: On average, how many Weapons does each character have?

## Gather the total amount of weapons among the characters
>>> Character.inventory.through.objects.filter(item_id__gt=137).count()
## 203

# Take the total of weapons and divide by the total of characters
>>> Character.inventory.through.objects.filter(item_id__gt=137).count() / Character.objects.all().count()
### 0.6721854304635762 ~ 1


#Sidenote: Total number of items for each character:

## Total number of items among ALL character
>>> Character.objects.filter(inventory__isnull=False).count()
## 898
>>> Character.objects.filter(inventory__isnull=False).count() / Character.objects.all().count()
### 2.9735099337748343 ~ 3