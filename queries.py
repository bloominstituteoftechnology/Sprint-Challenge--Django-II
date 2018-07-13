from charactercreator.models import Character
Character.objects
all_characters = Character.objects.all()
all_characters

# query to count the characters
count_char = Character.objects.count()
count_char
302