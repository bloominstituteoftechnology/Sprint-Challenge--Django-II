#Using Django ORM, write Python code to answer the following:

# 1. How many total Characters are there?
# ANSWER: 302
# ORM:
# len(Character.objects.all())


# 2. How many of each specific subclass?
# ANSWER: cleric 75, fighter 68, mage 108, necromancer 0, thief 51
# ORM:
# >>> cleric = 0
# >>> fighter = 0
# >>> mage = 0
# >>> necromancer = 0
# >>> thief = 0
# >>> cleric, fighter, mage, necromancer, thief
# (0, 0, 0, 0, 0)
# >>> for ch in Character.objects.all():
# ...     if hasattr(ch, 'cleric'):
# ...             cleric += 1
# ...     elif hasattr(ch, 'fighter'):
# ...             fighter += 1
# ...     elif hasattr(ch, 'mage'):
# ...             mage += 1
# ...     elif hasattr(ch, 'necromancer'):
# ...             necromancer += 1
# ...     elif hasattr(ch, 'thief'):
# ...             thief += 1
# >>> cleric, fighter, mage, necromancer, thief
# (75, 68, 108, 0, 51)
# >>> sum = cleric + fighter + mage + necromancer + thief
# >>> sum
# 302




# 3. How many total Items?
# ANSWER: 174
# ORM:
# len(Item.objects.all())



# 4. How many of the Items are weapons? How many are not?
# ANSWER: 38 Weapons, 136 non-Weapon Items
# ORM:
# len(Weapon.objects.all())
# len(Item.objects.filter(weapon__item_ptr_id__isnull=True))


# 5. On average, how many Items does each Character have?
# ANSWER: 2.97
# ORM:
# >>> sum = 0
# >>> for ch in Character.objects.all(): sum += ch.inventory.count()
# >>> sum
# 898
# >>> sum//Character.objects.all().count()
# 2
# >>>sum/Character.objects.all().count()
# 2.9735099337748343 




# 6. On average, how many Weapons does each character have?
# ANSWER: 0.68
# ORM: 
# >>> for ch in Character.objects.all():
# ...     items = ch.inventory.all()
# ...     weapons = items.filter(weapon__isnull=False)
# ...     sum += weapons.count()
# >>> sum
# 206
# >>> sum//Character.objects.all().count()
# 0
# >>> sum/Character.objects.all().count()
# 0.6821192052980133
