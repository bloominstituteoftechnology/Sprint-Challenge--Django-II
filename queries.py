from charactercreator.models import Character, Fighter, Mage, Thief, Cleric, Thief, Necromancer
from armory. models import Item, Weapon

c = Character.objects.all()
total_number_of_Characters = len(c)
total_number_of_Characters = 302

f = Fighter.objects.all()
total_number_of_Fighters = len(f)
total_number_of_Fighters = 68

m = Mage.objects.all()
total_number_of_Mages = len(m)
total_number_of_Mages = 108

cl = Cleric.objects.all()
total_number_of_Clerics = len(cl)
total_number_of_Clerics = 75

t = Thief.objects.all()
total_number_of_Thieves = len(t)
total_number_of_Thieves = 51

n = Necromancer.objects.all()
total_number_of_Necromaners = len(n)
total_number_of_Necromaners = 11
# Necromancers are Mages

#  Total number of Characters is 302
#  68 Fighters 
#  108 Mages ( 11 Mages are Necromancers)
#  75 Clerics
#  51 Theives


i = Item.objects.all()
total_number_of_Items = len(i) 
total_number_of_Items =  174

w = Weapon.objects.all()
total_number_of_Weapons = len(w) 
total_number_of_Weapons =  37
# Weapons are Items 


number_of_Items_that_are_not_Weapons = len(i) - len(w)
number_of_Items_that_are_not_Weapons = 137

# There all a total of 174 items
# 37 of these Items are Weapons
# 137 of these Items are not Weapons

average_amount_of_Items_for_each_Character = round((len(i)/len(c)), 2)
average_amount_of_Items_for_each_Character = 0.58

average_amount_of_Weapons_for_each_Character = round((len(w)/len(c)), 2)
average_amount_of_Weapons_for_each_Character = 0.12

average_amount_of_non_Weapon_Items_for_each_Character = round(((len(i) - len(w))/len(c)),2)
average_amount_of_non_Weapon_Items_for_each_Character = 0.45

# On average each character has a total of 0.58 Items
# On average each Character has 0.12 Weapons
# Ona average each character had 0.45 non-Weapon Items

## TODO: FIND A BETTER WAY OF FINDING THESE AVERAGES IN THE DATABASE? 
Characters_with_Items = Character.objects.filter(inventory=True)
Number_of_Characters_with_Items = len(Characters_with_Items)
Number_of_Characters_with_Items = 3
#??? so characters at indec 119,154, and 231 are the only ones with items???


