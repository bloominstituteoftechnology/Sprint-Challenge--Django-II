1. >> > from charactercreator.models import Character, Fighter, Mage, Cleric, Thief, Necromancer
    >> > Character.objects.all().count()
    302
    >> >
2. >> > Fighter.objects.all().count()
    68
    >> > Mage.objects.all().count()
    108
    >> > Cleric.objects.all().count()
    75
    >> > Thief.objects.all().count()
    51
    >> > Necromancer.objects.all().count()
    11
    >> >
3. >> > from armory.models import Item, Weapon
    >> > Item.objects.all().count()
    174
4. >> > Weapon.objects.all().count()
    37
5. >> > Item.objects.filter(weapon).count()
6. >> > Character.objects.all().aggregate(Items)
7. >> > Character.objects.all().aggregate(Items.Weapon)


I tried doing this:

>> > dir(Item.name)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_parent_chain',
 'field_name']
>> > dir(Item.weapon)
['RelatedObjectDoesNotExist', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__set__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 '__weakref__', 'get_prefetch_queryset', 'get_queryset', 'is_cached', 'related']
>> >

>> > dir(Weapon)
['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes',
    '_check_ordering', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', 'character_set', 'check', 'clean', 'clean_fields', 'date_error_message', 'delete', 'from_db', 'full_clean', 'get_deferred_fields', 'item_id', 'item_ptr', 'item_ptr_id', 'name', 'objects', 'pk', 'power', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'unique_error_message', 'validate_unique', 'value', 'weapon', 'weight']
>> >

and I tried indexing it differently... I tried using a dir on several Item.inserthere and nothing would yield how to index
weapon.  However, I could do Item.weapon and get the count.  I tried Item.objects.exclude(weapon).count() and that would produce
errors or return the total item count of 174.  I tried it as "weapon" as well.  Same result.
6 and 7 can be easily answered if you can get the answer to 5....just change the input in the().
