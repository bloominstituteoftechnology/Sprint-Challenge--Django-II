#Answers

### How many total Characters are there?

302

#### Code:

> > > from charactercreator.models import Character
> > > len(Character.objects.all())

#### Comment:

First must import all Character instances
Next getting the length of a query of all Character instances

### How many of each specific subclass?

Fighter: 68
Mage: 108 - 11 = 97
Cleric: 75
Thief: 51
Necromancer: 11

#### Code:

> > > from charactercreator.models import [Class]
> > > len([Class].objects.all())

#### Comment:

Import all the character instances of a class
get the length of each query of Character

### How many total Items?

175

#### Code:

> > > from armory.models import Item
> > > len(Item.objects.all())

#### Comment:

Import all Items
get the length of a query of all Items

### How many of the Items are weapons? How many are not?

37
138

#### Code:

> > > from armory.models import Weapon
> > > len(Weapon.objects.all())
> > > len(Item.objects.filter(weapon\_\_isnull=True)

#### Comment:

Import all Weapon class objects
Get length of query of all Weapons
Get length of query of all Items excluding Weapons

### On average, how many Items does each Character have?

2.97

#### Code:

> > > items = len(Character.objects.filter(inventory\_\_isnull=False))
> > > characters = len(Character.objects.all())
> > > items / characters

#### Comment:

Get len of query of all characters that have at least 1 item
Get len of query of all characters
Divide first by second

### On average, how many Weapons does each character have?

.67

#### Code:

sum([len(char.inventory.filter(weapon__isnull=False)) for char in Character.objects.all()])/len(Character.objects.all())

#### Comment:

Divided the sum of of all characters with weapons by the total of all characters
