from random_uk_bank_account.vocalink.vocalink_db import VocalinkDataAccess
from random_uk_bank_account.vocalink.vocalink_model import \
    (VocalinkRuleCollection, VocalinkRule, VocalinkSortCodeSubstitution, VocalinkSortCodeSubstitutionCollection)
from random_uk_bank_account.utils import validators


def get_vocalink_rules_for_sort_code(sort_code: str, db_location: str) -> VocalinkRuleCollection:
    validators.check_sort_code_correct_format(sort_code)

    vocalink_db = VocalinkDataAccess(DB_LOCATION=db_location)
    rules = vocalink_db.get_rules_for_sort_code(sort_code)
    vocalink_rule_collection = VocalinkRuleCollection()

    if rules:
        for rule in rules:
            vocalink_rule_collection.rules.append(VocalinkRule(**rule))

    return vocalink_rule_collection


def get_vocalink_sort_code_substitution_for_sort_code(sort_code: str, db_location: str) -> VocalinkSortCodeSubstitution:
    vocalink_db = VocalinkDataAccess(DB_LOCATION=db_location)
    substitution = vocalink_db.get_sort_code_substitution(sort_code)

    if substitution:
        return VocalinkSortCodeSubstitution(**substitution[0])
    else:
        return VocalinkSortCodeSubstitution()

def get_all_vocalink_sort_code_substutions(db_location: str) -> VocalinkSortCodeSubstitutionCollection:
    vocalink_db = VocalinkDataAccess(DB_LOCATION=db_location)
    subs = vocalink_db.get_all_sort_code_substitutions()

    subsitution_collection = VocalinkSortCodeSubstitutionCollection()

    if subs:
        for sub in subs:
            subsitution_collection.substitutions.append(VocalinkSortCodeSubstitution(**sub))

    return subsitution_collection

if __name__=="__main__":
    test = get_vocalink_rules_for_sort_code('200412')
    print('break')