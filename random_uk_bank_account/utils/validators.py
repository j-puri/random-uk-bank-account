from random_uk_bank_account.vocalink.vocalink_model import VocalinkRuleCollection
from random_uk_bank_account.utils.exceptions import VocalinkUnsupportedSortCodeError, UnsupportVocalinkException
from random_uk_bank_account.utils.config import ACCEPTED_VOCALINK_EXCEPTIONS


def check_sort_code_correct_format(sort_code: str):
    if len(sort_code) != 6:
        raise AttributeError(f"{sort_code} does not meet condition: sort codes must be a 6 character numeric string.")
    else:
        sort_code_array = sort_code.split()
        for character in sort_code_array:
            try:
                int(character)
            except Exception as e:
                raise AttributeError(f"{sort_code} does not meet condition: sort codes must only contain numeric character.")


def check_vocalink_exists_for_sort_code(rules: VocalinkRuleCollection, sort_code):
    if len(rules.rules) == 0:
        raise VocalinkUnsupportedSortCodeError(sort_code=sort_code)


def check_vocalink_exception_is_handled(rules: VocalinkRuleCollection, sort_code):
    for rule in rules.rules:
        if int(rule.exception) not in ACCEPTED_VOCALINK_EXCEPTIONS:
            raise UnsupportVocalinkException(rule.exception, sort_code)
