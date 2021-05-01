from random_uk_bank_account.vocalink import initialise as _initialise_vocalink
from random_uk_bank_account.generator.uk_account import RandomBankAccountGenerator as _RandomBankAccountGenerator, \
    RandomBankAccount
from random_uk_bank_account.vocalink.vocalink import \
    (
    get_vocalink_rules_for_sort_code as _vocalink_rules_for_sort_code,
    get_vocalink_sort_code_substitution_for_sort_code as _vocalink_substitutions_for_sort_code,
    get_all_vocalink_sort_code_substutions as _vocalink_all_sort_code_substitutions
)
from random_uk_bank_account.vocalink.vocalink_model import VocalinkRuleCollection, VocalinkSortCodeSubstitution, \
    VocalinkSortCodeSubstitutionCollection

from random_uk_bank_account.utils import config
from random_uk_bank_account.utils.config import LOGGER_NAME

import logging
import sys


def init_logger():
    logger = logging.getLogger(LOGGER_NAME)
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


class GenerateUkBankAccount:

    def __init__(
            self,
            log_level=logging.ERROR,
            cache_location=config.DEFAULT_VOCALINK_CACHE_LOCATION,
            vocalink_rules_version=config.DEFAULT_VOCALINK_VERSION_PATH,
            vocalink_substitution_version=config.DEFAULT_SORT_CODE_SUBSTITUTION_VERSION_PATH,
            recreate_vocalink_db=False,
            logger=init_logger()
    ):

        self._logger = logger
        self._logger.setLevel(log_level)
        self._cache_location, self._db_file_path = _initialise_vocalink(
            logger=self._logger, cache_location=cache_location, version=vocalink_rules_version,
            recreate=recreate_vocalink_db, sort_code_subs_version=vocalink_substitution_version
        )

        self.VOCALINK_VERSION = vocalink_rules_version
        self.VOCALINK_SUBSTITUTION_VERSION = vocalink_substitution_version

    def generate_for_sort_code(self, sort_code: str, total: int = 1) -> RandomBankAccount:
        return _RandomBankAccountGenerator(sort_code=sort_code, db_location=self._db_file_path) \
            .generate(total=total)

    def get_vocalink_rules(self, sort_code: str) -> VocalinkRuleCollection:
        return _vocalink_rules_for_sort_code(sort_code=sort_code, db_location=self._db_file_path)

    def get_vocalink_substitution(self, sort_code: str) -> VocalinkSortCodeSubstitution:
        return _vocalink_substitutions_for_sort_code(sort_code=sort_code, db_location=self._db_file_path)

    def get_all_vocalink_substitutions(self) -> VocalinkSortCodeSubstitutionCollection:
        return _vocalink_all_sort_code_substitutions(db_location=self._db_file_path)

    def validate(self, sort_code: str, account_number: str) -> bool:
        account_number_array = [int(digit) for digit in list(account_number)]
        return _RandomBankAccountGenerator(sort_code, db_location=self._db_file_path) \
            .validate(account_number_array=account_number_array)
