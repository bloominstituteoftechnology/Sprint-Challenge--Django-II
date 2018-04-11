# Sprint-Challenge--Django-II

For this sprint challenge, you'll be exploring some test data in a Django RPG.
Start by pulling and checking out the `testdata` branch from the main repo:
https://github.com/lambdaschool/django-rpg

You can do so by just making a fresh clone of the single branch, as you don't
have to open a PR for Django-RPG (your PR will be in this repo instead):
`git clone -b testdata --single-branch https://github.com/LambdaSchool/Django-RPG.git`

In this branch, `rpg/db.sqlite3` has been populated with dozens-to-hundreds of
randomly generated characters across the base classes (Fighter, Mage, Cleric,
and Thief) as well as some a few Necromancers. Also generated are Items,
Weapons, and connections from characters to them. Note that, while the name
field was randomized, the numeric and boolean fields were left as defaults.

Another approach to getting this data - `db.sqlite3` has been added to this
repository, and if you just overwrite the same file you're using for the RPG
(located by default in `rpg/db.sqlite3`) you'll get the data.

Your main goal is to write Python code that uses the Django ORM to answer:

- How many total Characters are there?
- How many of each specific subclass?
- How many total Items?
- How many of the Items are weapons? How many are not?
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have?

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
