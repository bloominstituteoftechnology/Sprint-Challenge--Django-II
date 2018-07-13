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

### Items ###
total_items = len(Item.objecs.all())
print("Total number of items: " + str(total_items)) # Answer= 174

### Weapons ###
total_weapons = len(Weapon.objects.all())
print("Total number of weapons: " + str(total_weapons)) # Answer= 37

### Other Items ###
total_other_items = total_items - total_weapons
print("Total number of other items: " + str(total_other_items)) # Answer= 137


#### The average number of Items each Character has ####
average_items = (total_items / total_chars)
print("Average number of items for each character: " + str(average_items)) # Answer= 3

#### The average number of Weapons each Character has ####
average_weapons = (total_weapons / total_chars)
print("Average number of weapons for each character: " + str(average_weapons)) # Answer= 1