from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

characters = Character.objects.all()
totalCharacters = characters.count()

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

items = Item.objects.all()
items.count()

weapons = Weapon.objects.all()
weapons.count()

items.filter(weapon__isnull=True).count()
items.exclude(weapon__isnull=False).count()

characters = Character.objects.all()
characterItems = 0
for character in characters:
  characterItems += character.inventory.count()

avgItems = characterItems / characters

avgWeapons = weapons / characters