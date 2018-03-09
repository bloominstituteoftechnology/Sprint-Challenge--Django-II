from .models import Character, Fighter, Mage, Cleric, Thief, Necromancer


class Info():

    def total_characters(self):
        return Character.objects.count()

    def subclass_total(self):
        dict = {
            "Fighter's": Fighter.objects.count(),
            "Mage's": Mage.objects.count(),
            "Cleric's": Cleric.objects.count(),
            "Thief's": Thief.objects.count(),
            "Necromancer's": Necromancer.objects.count()
        }

        # print(dict)
        return dict

    def total_items(self):
        totalItems = 0
        all_characters = Character.objects.all()
        for c in all_characters:
            totalItems = totalItems + c.inventory.count()

            return totalItems

    def total_weapons(self):
        return {
            "Weapons": Character.inventory.through.objects.filter(item_id__gt=137).count(),
            "Non Weapons": Character.inventory.through.objects.filter(item_id__lt=138).count()}

    def character_item_average(self):
        return (Character.inventory.through.objects.filter(item_id__lt=138).count() / Character.objects.count())

    def character_weapon_average(self):
        return (Character.inventory.through.objects.filter(item_id__gt=137).count() / Character.objects.count())
