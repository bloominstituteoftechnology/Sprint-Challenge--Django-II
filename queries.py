- How many total Characters are there?
        from charactercreator.models import Character
        len(Character.objects.all())
                           302
- How many of each specific subclass?
    
- How many total Items?
 from charactercreator.models import Item
 len(Item.objects.all())
 174

- How many of the Items are weapons? How many are not?
   from armory.models import Weapon, Item
   len(Weapon.objects.all())
   37
   len(Item.objects.filter(weapon__item_ptr_id__isnull=True))
   137
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have?