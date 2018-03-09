# Sprint-Challenge--Django-I

For this sprint challenge, you'll be exploring some test data in our Django RPG.
Start by pulling and checking out the `testdata` branch from the main repo:
https://github.com/lambdaschool/django-rpg

In this branch, `rpg/db.sqlite3` has been populated with dozens-to-hundreds of
randomly generated characters across the base classes (Fighter, Mage, Cleric,
and Thief) as well as some a few Necromancers. Also generated are Items,
Weapons, and connections from characters to them. Note that, while the name
field was randomized, the numeric and boolean fields were left as defaults.

Your main goal is to write Python code that uses the Django ORM to answer:

- How many total Characters are there? 302 not 313 because necromancers are mages
> from charactercreator.models import *
> characters = Character.objects.all()
> characters.__len__()
> or -> Character.objects.all().count()
- How many of each specific subclass?
* 68 fighters
* 108 mages
* 75 clerics
* 51 thieves
* 11 necromancers
> for each of these I did -> fighters = Fighter.objects.all() -> fighters.__len__()
- How many total Items? 174
> from armory.models import *
> items = Item.objects.all() -> items.__len__()
- How many of the Items are weapons? How many are not? 37 are weapons 137 are not
> weapons = Weapon.objects.all() -> weapons.__len__()
> notweapons = items.__len__() - weapons.__len__()
- On average, how many Items does each Character have? 0.5761589403973509
> avgItems = items.__len__() /characters.__len__()
- On average, how many Weapons does each character have? 0.12251655629139073
> avgWeapons = weapons.__len__() / characters.__len__()
> Limiting floats to two decimal points -> round(avgWeapons, 2)

You can experiment/execute our code using the Django shell. Please turn in a
file `queries.py` with your code along with comments for your answers.

Stretch goals:

- Answer the same questions using the Django db shell/SQL (turn in `queries.sql`)
- Add views/templates for a "dashboard" that reports the stats (pulling data
from the database, so it updates if that data changes)
- Using tables or charts, summarize answers to the above
- Slice the Items/Weapon distribution by Character subclass
- Play with populating your own test data - this data was generated using
https://github.com/volrath/django-autofixture (this fork is compatible with
Django 2.0 and is installed by the `requirements.txt` in the `testdata` branch,
but you may still need dependencies such as `gdal-bin` (search for how to
install this for your specific platform))

In general, this exercise is meant to test your ability to navigate and
investigate data in a Django application. If you get to the stretch goal of
using autofixture, the practical application here is testing - you can have
tests that generate unique random data each time, ensuring the robustness of
your application.
This sprint challenge is to create "from scratch" (using the appropriate
installed tools) a Django web application for a TODO list. You should do so in
your own fork of this repository, so you can turn it in via a pull request.
