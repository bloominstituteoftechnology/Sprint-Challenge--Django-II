How many total Characters are there?
>>> Total = Character.objects.count()
>>> print('How many total characters?', Total)
How many total characters? ```302```

How many total Items?
>>> totalItems = Item.objects.count()
>>> print('How many total Items?', totalItems)
How many total Items? ```174```

How many of each specific subclass?
>>> Fighters = Fighter.objects.count()
>>> Fighters
```68```
>>> Mages = Mage.objects.count()
>>> Mages
```108```
>>> Clerics = Cleric.objects.count()
>>> Clerics
```75```
>>> Thieves = Thief.objects.count()
>>> Thieves
```51```
>>> Necromancers = Necromancer.objects.count()
>>> Necromancers
```11```
>>> print('How many of each specific subclass?', Fighters + Mages + Clerics + Thieves + Necromancers)
How many of each specific subclass? ```313```

How many of the Items are weapons? How many are not?
>>> Weapons = Weapon.objects.count()
>>> Weapons
```37```
>>> print('How many of the Items are weapons?', Weapons, 'How many are not?', totalItems - Weapons)
How many of the Items are weapons? ```37``` How many are not? ```137```

On average, how many Items does each Character have?
>>> print('On average, how many Items does each Character have?', Item.objects.aggregate(Avg('character')))
On average, how many Items does each Character have? {'character__avg': ```148.6325167037862```} 

On average, how many Weapons does each character have?
>>> print('On average, how many Weapons does each Character have?', Weapon.objects.aggregate(Avg('character')))
On average, how many Weapons does each Character have? {'character__avg': ```149.64039408866995```}
>>>```149```
