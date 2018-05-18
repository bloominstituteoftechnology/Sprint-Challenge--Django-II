from charactercreator.models import Character, Cleric, Fighter, Mage, Necromancer, Thief
from armory.models import Weapon, Item

Character.objects.count()

Fighter.objects.count()

Mage.objects.count()

Cleric.objects.count()

Thief.objects.count()

Necromancer.objects.count()

Item.objects.count()
#174 items total

Weapon.objects.count()
#37 items are weapons

weapons = Weapon.objects.count()
items = Item.objects.count()
diff = items - weapons
#137 are not weapons

total_chars = Character.objects.count()
inventory = [chars.inventory.count() for chars in Character.objects.all()]
ave_item = sum(inventory) / total_chars
# ave_item = 2.9735099337748343

characters = Character.objects.all()
for c in characters:
	sum += c.inventory.filter(weapon_isnull=False).count()

ave_weap = sum / characters.count()
# ave = 0.12251655629139073


