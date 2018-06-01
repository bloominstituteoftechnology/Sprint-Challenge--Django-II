# 1. How many total Characters are there?
# Answer: 302
# Code: Character.objects.count()

# 2. How many of each specific subclass?
# Answer: Figther (68), Mage (108), Cleric (75), Thief (51), Necromancer (11)
# Code: <Subclass>.objects.count()

# 3. How many total Items?
# Answer: 174
# Code: Item.objects.count()

# 4. How many of the Items are weapons? How many are not?
# Answer: 37 weapons, 137 not
# Code: Weapon.objects.count() (and then substracted that number from the total number of weapons)

# 5. On average, how many Items does each Character have?
# Answer: 2.9735099337748343
# Code: First I had to import Count and Avg from django.db.models. So `from django.db.models import Count, Avg`
# Then, I could use that to get the right amount `Character.objects.all().annotate(count=Count('inventory')).aggregate(Avg('count'))`

# 6. On average, how many Weapons does each character have?
# Answer: 0.6721854304635762
# Code: Character.objects.all().annotate(count=Count('inventory__weapon')).aggregate(Avg('count'))
