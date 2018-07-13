#How many total Characters are there?
Character.objects.count()
#Ans: 302

#How many of each specific subclass?

##Fighters:
Fighter.objects.count()
#Ans: 68

##Mage:
Mage.objects.count()
#Ans: 108

##Cleric:
Cleric.objects.count()
#Ans: 75

##Thief:
Thief.objects.count()
#Ans: 51

##Necromancer:
Necromancer.objects.count()
#Ans: 11




#How many total Items?
##Items:
Item.objects.count()
#Ans: 174

#How many of the Items are weapons? How many are not?
##Weapons:
Weapon.objects.count()
#Ans: 37

#Not Weapons:
Item.objects.exclude(weapon__isnull=False).count()
#Ans: 137

#On average, how many Items does each Character have?

#Average Items per Character:
characters = (Characters.objects.all())
average = 0
for character in characters:
    average += character.inventory.count()
print(average / Character.objects.count())

#Ans: 2.9735099337748343

#On average, how many Weapons does each character have?

#Average Weapons per Character:
characters = Character.objects.all()
weapons = 0
for character in characters:
    weapons = character.inventory.exclude(weapon__isnull=False).count()
print(weapons / Character.objects.count())

#Ans: 0.013245033112582781