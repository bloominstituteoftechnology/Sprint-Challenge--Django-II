from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
from armory.models import Weapon, Item


#NOTE: two methods are shown to query a total of specific items in a queryset.  using len() is the more efficient, however.
# display total number Characters (302 total)
def character_list():
    return len(Character.objects.all())
    

#display total number of Fighter subclass (68 total)
def fighter_count():
    return len(Fighter.objects.all())
   

#display total number of Mage subclass (108)
def Mage_count():
    return Mage.objects.count()

#display total number of Cleric subclass (75)
def Cleric_count():
    return Cleric.objects.count()

#display total number of Thief subclass (51)
def Thief_count():
    return Thief.objects.count()  

#display total number of Necromancer subclass (11)
def Necromancer_count():
    return Necromancer.objects.count() 

#display total number of Items (174)
def item_count():
    return Item.object.count()

#display how many weapons (37)
def weapon_count():
    return len(Weapon.objects.all())

#display how many are not weapons (136)
#we can use the attribute with boolean value for this query
def non_weapons():
    return len(Item.objects.filter(weapon__item_ptr_id__isnull=True))

#display average number of items each character has (2)
def average_items():
    items = sum([character.inventory.count() for character in Character.objects.count()])
    average = items//Character.objects.count()
    return average

#display how many average Weapons each character has (.122)
def average_Weapons():
    weapons = weapons_count()
    average = weapons//[character for character in Character.objects.count()]