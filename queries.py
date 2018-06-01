from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon
print("Total Characters: {}\n".format(Character.objects.all()))
# Total Characters: <QuerySet [<Character: Character object (1)>, <Character: Character object (2)>, <Character: Character object (3)>, <Character: Character object (4)>, <Character: Character object (5)>, <Character: Character object (6)>, <Character: Character object (7)>, <Character: Character object (8)>, <Character: Character object (9)>, <Character: Character object (10)>, <Character: Character object (11)>, <Character: Character object (12)>, <Character: Character object (13)>, <Character: Character object (14)>, <Character: Character object (15)>, <Character: Character object (16)>, <Character: Character object (17)>, <Character: Character object (18)>, <Character: Character object (19)>, <Character: Character object (20)>, '...(remaining elements truncated)...']>

print("Total Characters: {}\n".format(Character.objects.all().count()))
# Total Characters: 302

print("Total Characters: {}\n".format(Mage.objects.all().count()))
# Total Characters: 108

print("Total Characters: {}\n".format(Cleric.objects.all().count()))
# Total Characters: 75

print("Total Characters: {}\n".format(Thief.objects.all().count()))
# Total Characters: 51

print("Total Characters: {}\n".format(Necromancer.objects.all().count()))
# Total Characters: 11

