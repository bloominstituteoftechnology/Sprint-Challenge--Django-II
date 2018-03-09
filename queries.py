from django.http import HttpResponse
from .models import Character, Fighter, Mage, Cleric, Thief
from armory.models import Item, Weapon
characterCount = Character.objects.all().count()
def countCharacters(request):
    # returns 302 characters from the database using count method
    return HttpResponse(characterCount);
def countSubCharacters(request):
    mageCount = Mage.objects.all().count()
    fighterCount = Fighter.objects.all().count()
    clericCount = Cleric.objects.all().count()
    thiefCount = Thief.objects.all().count()
    # returns  mage count = 108; fighter count = 68; cleric count = 75; thief count = 51;
    allcount = 'mage count = %d; fighter count = %d; cleric count = %d; thief count = %d;' %(mageCount, fighterCount, clericCount, thiefCount)
    return HttpResponse(allcount)
def itemCount(request):
    # returns 174 items from the database using count method
    return HttpResponse(Item.objects.all().count())
def weaponCount(request):
    countTotal = Item.objects.all().count()
    countWeapon = Weapon.objects.all().count()
    notWeapon = countTotal - countWeapon
    # returns weapon count = 37; not weapon count = 137
    allcount = 'weapon count = %d; not weapon count = %d' %(countWeapon, notWeapon)
    return HttpResponse(allcount)
def averageItemCount(request):
    inventoryCount = Character.objects.values('inventory').count()
    # return and rounds out to 3 items for each character
    return HttpResponse(round(inventoryCount/characterCount))
def averageWeaponCount(reqest):
    weaponCount = Character.objects.values('')