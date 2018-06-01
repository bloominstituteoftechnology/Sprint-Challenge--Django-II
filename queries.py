from charactercreator.models import Character, Cleric, Fighter, Mage, Necromancer, Thief
from armory.models import Item, Weapon

# All characters

len(Character.objects.all())

'''302'''

# Total in each subclass

len(Cleric.objects.all())

''' 75 '''

len(Fighter.objects.all())

''' 68 '''

len(Mage.objects.all())

''' 108 '''

len(Necromancer.objects.all())

''' 11 '''

len(Thief.objects.all())

''' 51 '''

# Items in Armory

len(Item.objects.all())

''' 174 '''

# Weapons

len(Weapon.objects.all())

''' 37 '''

# Average items for a Character

sum([character.inventory.count() for character in Character.objects.all()])/len(Character.objects.all())

''' 2.9735099337748343 '''

# Average weapons for a Character

sum([char.inventory.filter(weapon__isnull=False).count() for char in Character.objects.all()])/len(Character.objects.all())

''' 0.6721854304635762 '''




