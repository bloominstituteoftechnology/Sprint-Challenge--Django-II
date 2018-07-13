from charactercreator.models import *
from armory.models import *
char_models = [Character, Fighter, Mage, Cleric, Thief, Necromancer]

def give_power():
    for weapon in Weapon.objects.all():
        weapon.power += 1
        weapon.save()
def count_characters():
    return len(Character.objects.all())
def count_each_char():
    for model in char_models:
        return len(model.objects.all())
def count_items():
    return len(Item.objects.all())
def count_weapons():
    return len(Weapon.objects.all())
def count_non_weapons():
    return len(Item.objects.all()) - count_weapons()
def average_inventory():
    count = 0
    for character in Character.objects.all():
        count += character.inventory.count()
    return count