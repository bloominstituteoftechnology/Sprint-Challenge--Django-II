from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon


- How many total Characters are there?
len(Character.objects.all())
302
- How many of each specific subclass?
len(Fighter.objects.all())
68
len(Mage.objects.all())
108 of which 11 are Necromancers
len(Cleric.objects.all())
75
len(Thief.objects.all())
51
len(Necromancer.objects.all())
11
- How many total Items?
len(Item.objects.all())
174
- How many of the Items are weapons? How many are not?
len(Weapon.objects.all())
37
notWeapons=174-37 
137
- On average, how many Items does each Character have?
sum([character.inventory.count() for character in Character.objects.all()])/len(Character.objects.all())
2.9735099337748343

- On average, how many Weapons does each character have?
sum([char.inventory.filter(weapon__isnull=False).count() for char in Character.objects.all()])/len(Character.objects.all())
0.6721854304635762