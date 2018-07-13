from django.db.models import Count, Avg
from charactercreator.models import *
from armory.models import *
char_models = [Fighter, Mage, Cleric, Thief, Necromancer]

def give_power():
    for weapon in Weapon.objects.all():
        weapon.power += 1
        weapon.save()
def count_characters():
    return Character.objects.count()
def count_each_char():
    for model in char_models:
        return model.objects.count()
def count_items():
    return Item.objects.count()
def count_weapons():
    return Weapon.objects.count()
def count_non_weapons():
    return Item.objects.count() - count_weapons()
def average_inventory():
    count = 0
    for character in Character.objects.all():
        count += character.inventory.count()
    return count//Character.objects.count()
def average_weapons():
    return Character.objects.all().annotate(count=Count('inventory__weapon')).aggregate(Avg('count'))