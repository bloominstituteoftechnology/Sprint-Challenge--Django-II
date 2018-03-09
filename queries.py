from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Item, Weapon

characterCount = Character.objects.count()
fighterCount = Fighter.objects.count()
clericCount = Cleric.objects.count()
theifCount = Theif.objects.count()
necromancerCount = Necromancer.objects.count()
mageCount = Mage.objects.filter(necromancer__isnull=True).count()

itemCount = Item.objects.count()
weaponCount = Weapon.objects.count()
nonWeaponItemCount = itemCount - weaponCount

averageItemCount = Character.objects.filter(inventory__isnull=False).count() / characterCount

averageCharacterItemCount = itemCount / characterCount
averageCharacterWeaponCount = weaponCount / characterCount