# Queries **********************************************************************

# - How many total Characters are there? ***************************************
from charactercreator.models import Character  #                               *
Character.objects.count()  # 302                                               *
# ******************************************************************************

# - How many of each specific subclass? ****************************************
from charactercreator.models  #                                                *
import Fighter  #                                                              *
import Mage  #                                                                 *
import Cleric  #                                                               *
import Thief  #                                                                *
import Necromancer  #                                                          *
Fighter.objects.count()  # 68                                                  *
Mage.objects.count()  # 97                                                     *
Cleric.objects.count()  # 75                                                   *
Thief.objects.count()  # 51                                                    *
Necromancer.objects.count()  # 11                                              *
#                                                                              *
Fighter.objects.count() +  #                                                   *
Mage.objects.filter(necromancer__isnull=True).count() +  #                     *
Cleric.objects.count() +  #                                                    *
Thief.objects.count() +  #                                                     *
Necromancer.objects.count()  # 302                                             *
# ******************************************************************************

# - How many total Items? ******************************************************
from armory.models import Item  #                                              *
Item.objects.count()  # 174                                                    *
# ******************************************************************************

# - How many of the Items are weapons? How many are not? ***********************
from armory.models import Weapon  #                                            *
Item.objects.filter(weapon__isnull=True).count()  # 137                        *
Item.objects.filter(weapon__isnull=False).count()  # 37                        *
# ******************************************************************************

# - On average, how many Items does each Character have? ***********************
Item.objects.filter(  #                                                        *
  character__in=(x for x in Character.objects.all())).count()  #               *
/  #                                                                           *
Character.objects.count()  # 2.9735099337748343                                *
# ******************************************************************************

# - On average, how many Weapons does each character have? *********************
Weapon.objects.filter(  #                                                      *
  character__in=(x for x in Character.objects.all())).count()  #               *
/  #                                                                           *
Character.objects.count()  # 0.6721854304635762                                *
# ******************************************************************************


# unformatted queries
from charactercreator.models import Character
Character.objects.count() # 302

from charactercreator.models import Fighter, Mage, Cleric, Thief, Necromancer
Fighter.objects.count() # 68
Mage.objects.count()  # 97
Cleric.objects.count()  # 75
Thief.objects.count()  # 51
Necromancer.objects.count()  # 11
Fighter.objects.count() + Mage.objects.filter(necromancer__isnull=True).count() + Cleric.objects.count() + Thief.objects.count() + Necromancer.objects.count()  # 302

from armory.models import Item
Item.objects.count()  # 174

from armory.models import Weapon
Item.objects.filter(weapon__isnull=True).count()  # 137
Item.objects.filter(weapon__isnull=False).count()  # 37

Item.objects.filter(character__in=(x for x in Character.objects.all())).count() / Character.objects.count()  # 2.9735099337748343

Weapon.objects.filter(character__in=(x for x in Character.objects.all())).count() / Character.objects.count()  # 0.6721854304635762