# 1. displays the whole character

list(Character.objects.all())

# 2. displays characters in each specific classes

subclassName.objects.all().count()

# 3. displays number of items

Item.objects.count()

# 4. displys itmes that are weapons or not

Item.objects.count() -  Weapon.objects.count()

# 5. avrage items in each character

total_Items = Item.objects.count()
total_characters = Character.objects.count()
avg_itm_in_char = total_Items/total_characters
avg_itm_in_char =  0.5761589403973509  

# 6. 

total_Weapons = Weapon.objects.count()
total_characters = Character.objects.count()
avg_wep_in_char = total_Weapons/total_characters
avg_wep_in_char = 0.12251655629139073
