# Queries **********************************************************************

# - How many total Characters are there? ***************************************
from charactercreator.models import Character  #                               *
Character.objects.all().count()  # 302                                         *
# ******************************************************************************

# - How many of each specific subclass? ****************************************
from charactercreator.models  #                                                *
import Fighter  #                                                              *
import Mage  #                                                                 *
import Cleric  #                                                               *
import Thief  #                                                                *
import Necromancer  #                                                          *
Fighter.objects.all().count()  # 68                                            *
Mage.objects.all().count()  # 108                                              *
Cleric.objects.all().count()  # 75                                             *
Thief.objects.all().count()  # 51                                              *
Necromancer.objects.all().count()  # 11                                        *
#                                                                              *
Fighter.objects.all().count() +  #                                             *
Mage.objects.all().count() +  #                                                *
Cleric.objects.all().count() +  #                                              *
Thief.objects.all().count() +  #                                               *
Necromancer.objects.all().count()  # 313                                       *
#                                                                              *
# Note: that because the `Necromancer` class is a subclass of `Mage`,          *
# it does not get counted by `Character.objects.all()`.                        *
# 302 + 11 = 313                                                               *
# ******************************************************************************

# - How many total Items? ******************************************************
from armory.models import Item  #                                              *
Item.objects.all().count()  # 174                                              *
# ******************************************************************************

# - How many of the Items are weapons? How many are not? ***********************
Item.objects.filter(weapon__isnull=True).count()  # 137                        *
Item.objects.filter(weapon__isnull=False).count()  # 37                        *
# ******************************************************************************

# - On average, how many Items does each Character have? ***********************
(  #                                                                           *
  Item.objects.filter(  #                                                      *
    character__in=(x for x in Character.objects.all())).count() +  #           *
  Item.objects.filter(  #                                                      *
    character__in=(x for x in Necromancer.objects.all())).count()  #           *
)  #                                                                           *
/  #                                                                           *
(  #                                                                           *
  Character.objects.all().count() +  #                                         *
  Necromancer.objects.all().count()  #                                         *
)  # 2.9680511182108624                                                        *
#                                                                              *
# Not accounting for `Necromancer`s yields similar results (0.005 diff):       *
Item.objects.filter(  #                                                        *
  character__in=(x for x in Character.objects.all())).count()  #               *
/  #                                                                           *
Character.objects.all().count()  # 2.9735099337748343                          *
# ******************************************************************************

# - On average, how many Weapons does each character have? *********************

(  #                                                                           *
  Weapon.objects.filter(  #                                                    *
    character__in=(x for x in Character.objects.all())).count() +  #           *
  Weapon.objects.filter(  #                                                    *
    character__in=(x for x in Necromancer.objects.all())).count()  #           *
)  #                                                                           *
/  #                                                                           *
(  #                                                                           *
  Character.objects.all().count() +  #                                         *
  Necromancer.objects.all().count()  #                                         *
)  # 0.6741214057507987                                                        *
#                                                                              *
# Again, not accounting for `Necromancer`s yields very similar results:        *
Weapon.objects.filter(  #                                                      *
  character__in=(x for x in Character.objects.all())).count()  #               *
/  #                                                                           *
Character.objects.all().count()  # 0.6721854304635762                          *
# ******************************************************************************


# unformatted queries
from charactercreator.models import Character
Character.objects.all().count() # 302

from charactercreator.models import Fighter, Mage, Cleric, Thief, Necromancer
Fighter.objects.all().count() # 68
Mage.objects.all().count()  # 108
Cleric.objects.all().count()  # 75
Thief.objects.all().count()  # 51
Necromancer.objects.all().count()  # 11
Fighter.objects.all().count() + Mage.objects.all().count() + Cleric.objects.all().count() + Thief.objects.all().count() + Necromancer.objects.all().count()  # 313

from armory.models import Item
Item.objects.all().count()  # 174

Item.objects.filter(weapon__isnull=True).count()  # 137
Item.objects.filter(weapon__isnull=False).count()  # 37

(Item.objects.filter(character__in=(x for x in Character.objects.all())).count() + Item.objects.filter(character__in=(x for x in Necromancer.objects.all())).count()) / (Character.objects.all().count() + Necromancer.objects.all().count())  # 2.9680511182108624
Item.objects.filter(character__in=(x for x in Character.objects.all())).count() / Character.objects.all().count()  # 2.9735099337748343

(Weapon.objects.filter(character__in=(x for x in Character.objects.all())).count() + Weapon.objects.filter(character__in=(x for x in Necromancer.objects.all())).count()) / (Character.objects.all().count() + Necromancer.objects.all().count())  # 0.6741214057507987
Weapon.objects.filter(character__in=(x for x in Character.objects.all())).count() / Character.objects.all().count()  # 0.6721854304635762