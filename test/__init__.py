import pytest
from random_uk_bank_account import GenerateUkBankAccount
from random_uk_bank_account.utils.config import \
    (VOCALINK_URL, DEFAULT_VOCALINK_VERSION_PATH, DEFAULT_SORT_CODE_SUBSTITUTION_VERSION_PATH)
import os
import pathlib


def test_project_root() -> pathlib.Path:
    return pathlib.Path(__file__).parent


