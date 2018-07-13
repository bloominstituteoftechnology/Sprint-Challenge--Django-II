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

