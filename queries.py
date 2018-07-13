# from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
# from armory.models import Item, Weapon



## How many total Characters? ##
total_chars = len(Character.objects.all())
print("Total number of characters: " + str(total-chars)) # Answer=302


## How many of each specific subclass? ##

## Fighter ##
fighter_chars = len(Fighter.objects.all())
print("Total number of Fighter: " + str(fighter_chars)) # Answer= 68


## Mage ##
mage_chars = len(Mage.objects.all())
print("Total number of Mage: " + str(mage_chars)) # Answer= 108

## Cleric ##
cleric_chars = len(Cleric.objects.all())
print("Total number of Clerics: " + str(cleric_chars)) #Answer= 75

## Thief ##
theif_chars = len(Thief.objects.all())
print("Total number of Thiefs: " str(thief_chars)) # Answer= 51

## Necromancer ##
necromancer_chars = len(Necromancer.objects.all())
print("Total number of Necromancers: "+ str(necromancer_chars)) # Answer= 11



### How many total items ###

## How many total Characters? ##
total_chars = len(Character.objects.all())
print("Total number of characters: " + str(total-chars)) # Answer=302


## How many of each specific subclass? ##

## Fighter ##
fighter_chars = len(Fighter.objects.all())
print("Total number of Fighter: " + str(fighter_chars)) # Answer= 68


## Mage ##
mage_chars = len(Mage.objects.all())
print("Total number of Mage: " + str(mage_chars)) # Answer= 108

## Cleric ##
cleric_chars = len(Cleric.objects.all())
print("Total number of Clerics: " + str(cleric_chars)) #Answer= 75

## Thief ##
theif_chars = len(Thief.objects.all())
print("Total number of Thiefs: " str(thief_chars)) # Answer= 51

## Necromancer ##
necromancer_chars = len(Necromancer.objects.all())
print("Total number of Necromancers: "+ str(necromancer_chars)) # Answer= 11



### How many total items ###

Items:
    Item.objects.count()
    # Answer: 174

Weapons:
    Weapon.objects.count()
    # Answer: 37

Not Weapons:
    Item.objects.exclude(weapon__isnull=False).count()
    # Answer: 137


Average Items per Character:
    characters = (Character.objects.all())
    average = 0
    for character in characters:
       average += character.inventory.count()

    print(average / Character.objects.count())
    # Answer: 2.9735099337748343


Average Weapons per Character:
    characters = Character.objects.all()
     weapons = 0
    for character in characters:
        weapons = character.inventory.exclude(weapon__isnull=False).count()

    print(weapons / Character.objects.count())
    # Answer: 0.013245033112582781 
