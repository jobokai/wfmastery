SCHEMA_MAP = dict()

SCHEMA_EQUIPMENT_CATEGORIES = SCHEMA_MAP["equipment_categorties"] = """
    CREATE TABLE equipment_categories
    (id, position, name, category_id, sub_category_id)
"""

"""
    Fields:
        id (int): non-nat key
        position(int): display position
        name (str): eg "Rifle" "Melee", etc
        category_id (int): if not null then record is for a category identifier
        sub_category_id (int): if not null then record is for a subcategory id

    Shit has gone wrong if both category_id and sub_category_id are non-null
"""

"""
    WIP

"""

SCHEMA_SPECIAL_IDS = SCHEMA_MAP["special_identifiers"] = """
    CREATE TABLE special_identifiers
    (id, name, description)
"""

"""
    Equipment schema
        Fields:
            id (int): Autogenerated non-natural primary key
            index (int): Storage and History identifier
            display_pos (int): Will mirror index initially but intention is to use this to
                re-order items so things like "HEK" and "Vaykor Hek" are adjacent despite not being
                alphabetically correct.
            name (str): Natural item name as sourced from wiki
            pretty_name (str): An override to reconcile with how Warframe names stuff
            wiki_url (str): Would point to wikia but possibly somewhere else as needed.
            id_category: TODO the integer identifiers data_v1
            id_subcategory: TODO see above
            id_special: if 0 or null it is not "special" if >0 it would be used to mark it as an event/prime/founder/etc item
                typically see this being 1 for primes, 2 for vandals, 3 wraths, 4-n for syndicates

            hidden (bool): For vault or dead stuff
            parent_id: Some things have child components needed to build them (Ember's neuro, chassis, systems, blueprint)
"""

SCHEMA_EQUIPMENT = SCHEMA_MAP["equipment"] = """
    CREATE TABLE equipment
    (id, index, display_pos, name, pretty_name, wiki_url, category_id, subcategory_id, hidden, is_special, parent_id)
"""


SCHEMA_RELIC_TIERS = SCHEMA_MAP["relic_tiers"] = """
    CREATE TABLE relic_tiers
    (id, name)
"""

SCHEMA_RELIC_NAMES = SCHEMA_MAP["relic_names"] = """
    CREATE TABLE relic_names
    (id, name)
"""

SCHEMA_RARITY = SCHEMA_MAP["rarity"] = """
    CREATE TABLE rarity
    (id, name)
"""

SCHEMA_PRIMES = SCHEMA_MAP["primes"] = """
    CREATE TABLE primes
    (id, id_parent, name, component, tier, relic, rarity);
"""

SCHEMA_FAMILIARS = SCHEMA_MAP["familiars"] = """
    CREATE TABLE familiars
    (index, display_pos, name, pretty_name, category_id, subcategory_id, hidden, is_special, parent_id)
"""
