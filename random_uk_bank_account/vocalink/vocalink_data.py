from random_uk_bank_account.client.vocalink import VocalinkApi
from random_uk_bank_account.utils.config import LOGGER_NAME
from random_uk_bank_account.vocalink.vocalink_model import \
    (VocalinkRule, VocalinkRuleCollection, VocalinkArrayMap, VocalinkSortCodeSubstitution,
     VocalinkSortCodeSubstitutionCollection)

import logging

log = logging.getLogger(LOGGER_NAME)


def vocalink_raw_to_array(raw_data: str) -> []:
    split_array = [entry.split() for entry in raw_data.splitlines()]
    return [entry for entry in split_array if len(entry) != 0]


def get_vocalink_data(version) -> VocalinkRuleCollection:
    raw_data = VocalinkApi().get_vocalink_modulus_media(version)
    array_data = vocalink_raw_to_array(raw_data)
    vocalink_rule_array = []

    for rule in array_data:
        try:
            exception = rule[VocalinkArrayMap.EXCEPTION]
        except:
            exception = 0

        vocalink_rule_array.append(
            VocalinkRule(
                sort_code_from=rule[VocalinkArrayMap.SORT_CODE_FROM],
                sort_code_to=rule[VocalinkArrayMap.SORT_CODE_TO],
                algorithm=rule[VocalinkArrayMap.ALGORITHM],
                sort_code_pos_1=rule[VocalinkArrayMap.SORT_CODE_RULE_1],
                sort_code_pos_2=rule[VocalinkArrayMap.SORT_CODE_RULE_2],
                sort_code_pos_3=rule[VocalinkArrayMap.SORT_CODE_RULE_3],
                sort_code_pos_4=rule[VocalinkArrayMap.SORT_CODE_RULE_4],
                sort_code_pos_5=rule[VocalinkArrayMap.SORT_CODE_RULE_5],
                sort_code_pos_6=rule[VocalinkArrayMap.SORT_CODE_RULE_6],
                account_number_pos_1=rule[VocalinkArrayMap.ACCOUNT_NUMBER_RULE_1],
                account_number_pos_2=rule[VocalinkArrayMap.ACCOUNT_NUMBER_RULE_2],
                account_number_pos_3=rule[VocalinkArrayMap.ACCOUNT_NUMBER_RULE_3],
                account_number_pos_4=rule[VocalinkArrayMap.ACCOUNT_NUMBER_RULE_4],
                account_number_pos_5=rule[VocalinkArrayMap.ACCOUNT_NUMBER_RULE_5],
                account_number_pos_6=rule[VocalinkArrayMap.ACCOUNT_NUMBER_RULE_6],
                account_number_pos_7=rule[VocalinkArrayMap.ACCOUNT_NUMBER_RULE_7],
                account_number_pos_8=rule[VocalinkArrayMap.ACCOUNT_NUMBER_RULE_8],
                exception=exception
            )
        )

    return VocalinkRuleCollection(rules=vocalink_rule_array)



def get_vocalink_substitutions(version) -> VocalinkSortCodeSubstitutionCollection:
    raw_data = VocalinkApi().get_vocalink_modulus_media(version)
    array_data = vocalink_raw_to_array(raw_data)

    vocalink_substitition_array = []

    for substitution in array_data:

        vocalink_substitition_array.append(
            VocalinkSortCodeSubstitution(
                original_sort_code=substitution[0],
                substituted_sort_code=substitution[1]
            )
        )
    return VocalinkSortCodeSubstitutionCollection(substitutions=vocalink_substitition_array)

