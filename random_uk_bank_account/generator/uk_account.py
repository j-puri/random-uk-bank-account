from typing import List

from dataclasses_json import dataclass_json

from random_uk_bank_account.utils.random import get_random_number_array
from random_uk_bank_account.validator.modulus_checker import ModulusChecker
from random_uk_bank_account.vocalink.vocalink import \
    (get_vocalink_rules_for_sort_code, get_vocalink_sort_code_substitution_for_sort_code)
from random_uk_bank_account.utils import number
from random_uk_bank_account.utils import validators
from random_uk_bank_account.utils.config import LOGGER_NAME

from dataclasses import dataclass, field

import logging


@dataclass_json()
@dataclass(repr=True)
class RandomBankAccount:
    sort_code: str
    account_numbers: List = field(default_factory=lambda: [])

    def add_account_number(self, account_number):
        self.account_numbers.append(account_number)


class RandomBankAccountGenerator:

    def __init__(self, sort_code, db_location, logger=logging.getLogger(LOGGER_NAME)):
        self._logger = logger
        self.sort_code = sort_code
        self.sort_code_array = [int(digit) for digit in list(sort_code)]
        self.rules = get_vocalink_rules_for_sort_code(sort_code, db_location)
        self.substitution = get_vocalink_sort_code_substitution_for_sort_code(sort_code, db_location)
        self.modulus_checker = ModulusChecker(vocalink_rules=self.rules, substitution=self.substitution)
        self.max_attempts = 100

        self._logger.debug(f"Vocalink rules: {self.rules.to_json()}")
        self._logger.debug(f"Vocalink sort code substitutions: {self.substitution.to_json()}")

    def generate(self, total: int = 1) -> RandomBankAccount:
        random_bank_accounts = RandomBankAccount(sort_code=self.sort_code)
        attempts = 0

        while len(random_bank_accounts.account_numbers) != total and attempts < total * self.max_attempts:
            attempts += 1
            account_number = self._generate_bank_account(random_array=get_random_number_array(8))
            if account_number:
                random_bank_accounts.add_account_number(account_number)
                self._logger.debug(f"{len(random_bank_accounts.account_numbers)}/{total} account numbers generated")


        return random_bank_accounts

    def validate(self, account_number_array: []) -> bool:
        return self._satisfied(account_number=account_number_array)

    @property
    def sort_code(self):
        return self._sort_code

    @sort_code.setter
    def sort_code(self, _sort_code):
        validators.check_sort_code_correct_format(_sort_code)
        self._sort_code = _sort_code

    @property
    def rules(self):
        return self._rules

    @rules.setter
    def rules(self, _rules):
        validators.check_vocalink_exists_for_sort_code(_rules, self.sort_code)
        validators.check_vocalink_exception_is_handled(_rules, self.sort_code)
        self._rules = _rules

    @staticmethod
    def _get_fudging_indices(random_array: []):
        fudge_index_1 = number.get_indices_of_min_even_integer(random_array)
        fudge_index_2 = number.get_indices_of_min_odd_integer(random_array)

        if fudge_index_1 is None:
            fudge_index_1 = number.get_indices_of_min_odd_integer(random_array, level=2)
        if fudge_index_2 is None:
            fudge_index_2 = number.get_indices_of_min_even_integer(random_array, level=2)

        return [fudge_index_1, fudge_index_2]

    def _satisfied(self, account_number: []) -> bool:
        is_satisfied = self.modulus_checker.are_vocalink_rules_applied(
            sort_code_array=self.sort_code_array, account_array=account_number)

        return is_satisfied

    def _generate_bank_account(self, random_array=get_random_number_array(8)):
        self._logger.debug(f"Generating Bank Account for {self.sort_code}. Seed array: {random_array} ")
        fudging_indices = self._get_fudging_indices(random_array)
        mod_pass = self._satisfied(random_array)

        fudges = 0
        if not mod_pass:
            for replace_1 in range(0, 9):
                fudges +=1
                random_array[fudging_indices[0]] = (1 + random_array[fudging_indices[0]]) % 10
                for replace_2 in range(0, 9):
                    fudges +=1
                    random_array[fudging_indices[1]] = (1 + random_array[fudging_indices[1]]) % 10
                    mod_pass = self._satisfied(random_array)
                    if mod_pass:
                        break
                if mod_pass:
                    break
        if mod_pass:
            self._logger.debug(f"Account Number {random_array} satisfies checks after {fudges} numeric changes")
            return ''.join([str(num) for num in random_array])
        else:
            self._logger.debug(f"Account Number {random_array} does not satisfy checks after {fudges} numeric changes")
            return None
