from charactercreator.models import Character, Cleric, Fighter, Mage, Necromancer, Thief
from armory.models import Weapon, Item

def get_character_count():
    return Character.objects.count()
# Character count: 302


def get_subclass_counts():
    subclasses = (Cleric, Fighter, Mage, Necromancer, Thief)
    counts = {}
    for subclass in subclasses:
        counts[subclass] = subclass.objects.count()
    return counts
# Necromancer count: 11 (also count as mages)
# Fighter count:     68
# Cleric count:      75
# Thief count:       51
# Mage count:        108

def get_item_count():
    return Item.objects.count()
# Item count: 174

def get_weapon_count():
    return Weapon.objects.count()
# Weapon count: 38

def get_item_count_minus_weapons():
    return get_item_count() - get_weapon_count()
# Item count minus weapons: 136

def get_avg_item_per_character_count():
    item_inventory_count = [c.inventory.count() for c in Character.objects.all()]
    return sum(item_inventory_count) / get_character_count()
# Average item count per character: 2.9735 ....

def get_avg_weapon_per_character_count():
    weapon_inventory = []
    for c in Character.objects.all():
        for item in c.inventory.all():
            if hasattr(item, 'weapon'):
                weapon_inventory.append(item)
    return len(weapon_inventory) / get_character_count()
# Average weapon count per character: 0.6788 ....
# (couldn't figure out the ORM way to filter this)